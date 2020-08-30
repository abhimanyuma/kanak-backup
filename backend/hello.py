from flask import Flask
from typing import Dict

app = Flask(__name__)

@app.route('/')
def index() -> Dict:
    return {
        "status": True
    }

@app.route('/hello')
def hello() -> Dict:
    return {
        "status": True,
        "data": "Hello, World",
    }
