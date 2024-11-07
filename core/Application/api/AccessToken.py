from flask_jwt_extended import create_access_token, get_jwt_identity
from core.storage.database import DataService, MongoDBRepository
from flask import jsonify, request, session

def NewAccessToken():
    auth_header = request.headers.get('Authorization', None)

    try:
        current_user = get_jwt_identity() 
        repository = MongoDBRepository(db_name="mydatabase", collection_name="auth")
        service = DataService(repository=repository)
        get_bearer = service.get_data({'address': current_user})[0]['jwt']
        print(get_bearer, auth_header)
        if get_bearer != auth_header[7:]:
            return jsonify({"msg": "Token existence has ended"}), 401
    
        new_access_token = create_access_token(identity=current_user)
        service.update_data({'address': current_user}, {'jwt': new_access_token})    

        return jsonify({"msg": "Token is created", "token": new_access_token}), 200
    except Exception as e:
        return jsonify({"msg": "Invalid or expired token", "error": str(e)}), 401