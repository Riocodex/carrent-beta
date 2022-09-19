#here we import blueprint..its a package that allows us to inherit different views from different files
#render_template to import html files

from flask import Blueprint , render_template
from flask_login import login_required , current_user

#setting the blueprint for our flask application
views=Blueprint('views' , __name__)

 #setting navigations 
 
 #defining root
@views.route('/')
@login_required
#defining function that will be returned when root is called
def home():
    #returning the webpage to be displayed
    return render_template("home.html" , user=current_user)