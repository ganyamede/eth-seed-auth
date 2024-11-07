from core.storage.database import DataService, MongoDBRepository
from core.Application.api.CookieState import isAuth
from flask import render_template, session

def Home():
    state = 'address' in session
    if state:
        repository = MongoDBRepository(db_name="mydatabase", collection_name="auth")
        service = DataService(repository=repository)
        result = service.get_data({'address': session['address']})

    return render_template('home.html', state=state, jwt=None if not state else result[0]['jwt'])

def Login():
    return render_template('login.html')

def Register():
    return render_template('register.html')