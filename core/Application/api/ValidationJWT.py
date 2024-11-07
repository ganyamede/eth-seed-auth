# from functools import wraps
# from flask import jsonify

# # Декоратор для проверки JWT токена
# def token_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         token = None

#         # Получаем токен из заголовков
#         if 'Authorization' in request.headers:
#             token = request.headers['Authorization'].split(" ")[1]

#         if not token:
#             return jsonify({'message': 'Token is missing!'}), 403

#         try:
#             # Проверяем токен
#             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
#             current_user = data['user_id']
#         except jwt.ExpiredSignatureError:
#             return jsonify({'message': 'Token has expired!'}), 403
#         except jwt.InvalidTokenError:
#             return jsonify({'message': 'Invalid token!'}), 403

#         return f(current_user, *args, **kwargs)

#     return decorated_function