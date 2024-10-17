from flask import Flask
from flask_cors import CORS
from routes import register_routes
import logging

def create_app():
    app = Flask(__name__, static_folder='static')
    CORS(app)
    register_routes(app)
    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(host='0.0.0.0', port=3001, debug=True)  # Correctly set to listen on all interfaces
