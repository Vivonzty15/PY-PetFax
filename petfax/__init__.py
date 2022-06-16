from flask import Flask, request

def create_app(): 
    app = Flask(__name__)

    @app.route('/<silly_string>', methods=('GET', 'POST'))
    def index(silly_string): 
        if (request.method == "GET"):
            return silly_string;
        elif (request.method == "POST"):
            return 'Posted to silly string'
        return 'Hello, PetFax!'

    from . import pet
    app.register_blueprint(pet.bp)

    return app
