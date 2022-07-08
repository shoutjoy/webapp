from flask import Flask

def creat_app():
    app = Flask(__name__)
    @app.route('/')
    def hello():
        return 'Hello. world'
    return app
    
    