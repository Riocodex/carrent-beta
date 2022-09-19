from flask import Flask


def create_app():
    app = Flask(__name__);
    
    app.config['SECRET_KEY'] = 'fdajdpf djpf' #this code here is the secret key to the website..
   
    
  
    
    from .views import views
    from .auth import auth
    
    #in this we are registering the path..in the url prefix here to access
    
    app.register_blueprint(views , url_prefix = '/')
    app.register_blueprint(auth , url_prefix = '/')
    
   