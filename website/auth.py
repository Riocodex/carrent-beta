#here we import blueprint..its a package that allows us to inherit different views from different files
#render_template to import html files

from flask import Blueprint , render_template

#setting the blueprint for our flask application
auth=Blueprint('auth' , __name__)

 #setting navigations 
 
 #defining root
@auth.route('/login')
#defining function that will be returned when root is called
def login():
    #returning the webpage to be displayed
    return render_template("login.html")

 #defining root
@auth.route('/sign-up')
#defining function that will be returned when root is called
def sign_up():
    #returning the webpage to be displayed
    return render_template("sign_up.html")
    