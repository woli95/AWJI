from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import auth, credentials
import json

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
data = None

cred = credentials.Certificate("awji-e562b-firebase-adminsdk-hh6wn-1afe6b8ff9.json")
firebase = firebase_admin.initialize_app(cred)
import routes

if __name__ == "__main__":
    app.run()