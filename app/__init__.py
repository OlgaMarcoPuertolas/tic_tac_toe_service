from flask import Flask
from app.routes.api import api_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix="/api")

    @app.route("/")
    def index():
        return "Tic Tac Toe Service"

    return app
