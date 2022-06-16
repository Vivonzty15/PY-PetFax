# # config                    
# from flask import Flask
# app = Flask(__name__)

# # index route
# @app.route('/')
# def index(): 
#     return 'Hello, this is PetFax!'

# # pets index route
# @app.route('/pets')
# def pets(): 
#     return 'These are our pets available for adoption!'

# # To run a reloading flask application type 'flask run --reload' in the terminal


# if __name__ == '__main__':
#     app.run(debug=True)

from petfax import create_app
app = create_app()
