from flask import Flask
from app.views import sendItViews


app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(sendItViews.bp)