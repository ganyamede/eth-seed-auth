from flask import Blueprint
from flask_jwt_extended import jwt_required
from core.Application.api.Sign import LoginPost
from core.Application.api.CookieState import isAuth
from core.Application.api.HelloWorld import HelloWorld
from core.Application.api.Register import RegisterPost
from core.Application.api.AccessToken import NewAccessToken
from core.Application.views.Render import ( 
    Home,
    Login,
    Register
)


App = Blueprint('main', __name__, template_folder='core/Application/templates')

#GET
App.add_url_rule('/', 'Home', view_func=(Home), methods=['GET'])
App.add_url_rule('/login/', 'Login', view_func=isAuth('/')(Login), methods=['GET'])
App.add_url_rule('/register/', 'Register', view_func=isAuth('/')(Register), methods=['GET'])

#POST
App.add_url_rule('/login/', 'LoginPost', view_func=isAuth('/')(LoginPost), methods=['POST'])
App.add_url_rule('/register/', 'RegisterPost', view_func=isAuth('/')(RegisterPost), methods=['POST'])
App.add_url_rule('/new-access/', 'AccessToken', view_func=jwt_required()(NewAccessToken), methods=['POST'])
App.add_url_rule('/helloworld/', 'HelloWorld', view_func=jwt_required()(HelloWorld), methods=['POST'])