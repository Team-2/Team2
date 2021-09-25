from flask import Flask

app = Flask(__name__)
client = app.test_client()

from request import ship

app.register_blueprint(ship)
