from  flask import Flask
#initializing our app
def create_app():
    app= Flask( __name__)
    #website secret key
    app.config['SECRET_KEY'] = 'hjsfahah'