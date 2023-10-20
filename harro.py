from flask import Flask
app = Flask(__name__)

@app.route('/')
def harro_world():
    return 'Harrou Everynyan!'
