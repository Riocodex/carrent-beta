#import the app details from the website folder
from website import create_app
#to run our application
app = create_app()
#this code allows the file to be run directly only when i run it on main.py
if __name__ == '__main__':
    #to continue debuggin whenever we reset the server we set the debuggin to true
    app.run(debug=True)
    