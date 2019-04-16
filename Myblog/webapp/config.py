import os

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') #'bb50d77d96818c8236a8c17acb15250c'
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') #'sqlite:///site.db'
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_USE_TLS = True
	MAIL_PORT = 587
	MAIL_USERNAME = os.environ.get('EMAIL_USER') #'mydevops2019@gmail.com'#
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS') #'Sammy100!'#
