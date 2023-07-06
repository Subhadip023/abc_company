# from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash  # Import password hashing functions
# import bcrypt

# # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///User_data_base.db"
# # db = SQLAlchemy(app)
# # hashed_password = "pbkdf2:sha256:600000$bqx804hvyBCDgPKe$07ece25e7b1c7059d23ec5cfd95cb654164e6e5c5632bdebacc08010e502a4ae"
# # password = 123456

# # if check_password_hash(hashed_password, password):
# #     # Password is correct
# #     print("Password is correct")
# # else:
# #     # Password is incorrect
# #     print("Password is incorrect")

# # password = "123456"
# # hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
# # # print(hashed_password)


# # password = "123456"
# # # 
# # if check_password_hash(hashed_password, password):
# #     # Password is correct
# #     print("Password is correct")
# # else:
# #     # Password is incorrect
# #     print("Password is incorrect")
    
# def check(password,hashed_password):
    
#     if check_password_hash(hashed_password, password):
#     # Password is correct
#         print("Password is correct")
#     else:
#     # Password is incorrect
#         print("Password is incorrect")
        
# if __name__ == '__main__':
#     password = "123456"
#     password1 = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
#     # print(password1)
#     hashed_password="pbkdf2:sha256:600000$5tyj7YDQ$6fc5996ce79e6018643021c21a0ecec4331abb051ae32cdf6d3bc60476494ca0"
#     print(generate_password_hash(password1, method='pbkdf2:sha256', salt_length=8))
#     hashed_password = generate_password_hash(password1, method='pbkdf2:sha256', salt_length=8)
#     print(hashed_password)
#     # check(password=password,hashed_password=hashed_password)
x='home.jpg'
print('.',x.split('.')[1])