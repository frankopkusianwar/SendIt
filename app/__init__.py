from flask import Flask
from app.views import usersView


app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(usersView.bp)