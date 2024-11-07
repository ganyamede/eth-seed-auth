from abc import ABC, abstractmethod
from pymongo import MongoClient
from pymongo.collection import Collection
from typing import List, Dict, Any
from core.env.config import MONGO_URL


# CRUD
class IDataRepository(ABC):
    @abstractmethod
    def insert(self, data: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def select(self, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def delete(self, query: Dict[str, Any]) -> int:
        pass

    @abstractmethod
    def update(self, query: Dict[str, Any], update_data: Dict[str, Any]) -> int:
        pass


# Реализация для MongoDB
class MongoDBRepository(IDataRepository):
    def __init__(self, db_name: str, collection_name: str):
        self.client = MongoClient(MONGO_URL)  # Создаем постоянное подключение
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert(self, data: Dict[str, Any]) -> str:
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def select(self, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        return list(self.collection.find(query))

    def delete(self, query: Dict[str, Any]) -> int:
        result = self.collection.delete_many(query)
        return result.deleted_count

    def update(self, query: Dict[str, Any], update_data: Dict[str, Any]) -> int:
        result = self.collection.update_many(query, {'$set': update_data})
        return result.modified_count

    def close(self):
        self.client.close()  # Закрывает подключение


# Класс сервиса (инъекция зависимости)
class DataService:
    def __init__(self, repository: IDataRepository):
        self.repository = repository

    def add_data(self, data: Dict[str, Any]) -> str:
        return self.repository.insert(data)

    def get_data(self, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        return self.repository.select(query)

    def remove_data(self, query: Dict[str, Any]) -> int:
        return self.repository.delete(query)

    def update_data(self, query: Dict[str, Any], update_data: Dict[str, Any]) -> int:
        return self.repository.update(query, update_data)


# Example

    
#     repository = MongoDBRepository(db_name="mydatabase", collection_name="auth")
#     service = DataService(repository=repository)

    # Вставка данных
    # new_data = {'name': 'Alice', 'age': 28, 'city': 'Paris'}
    # inserted_id = service.add_data(new_data)
    # print(f'Вставлен: {inserted_id}')

    # Выбор данных
    # query = {'name': 'Alice'}
    # documents = service.get_data(query)
    # print("Найденные:", documents)

    # Удаление данных
    # deleted_count = service.remove_data(query)
    # print(f'Удалено: {deleted_count}')

    