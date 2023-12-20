from flask import Flask
from flask_cors import CORS
from src.test import predict

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    if test_config is None:
        app.config.from_mapping(
            # your config settings...
        )
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(predict)

    return app
