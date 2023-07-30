import flask
from flask import Flask, request, escape

# app instance
app = Flask(__name__)


# handle incoming web requests and send responses

# main URL
@app.route('/')
def hello():
    print(flask.__version__)
    return 'Hello, World! from Pj...'


@app.route('/greet')
# Sample Usage: http://127.0.0.1:5000/greet?name=Pratik
def greet():
    name = request.args['name']
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <h1>Hi {}</h1>
    </body>
    </html>'''.format(escape(name))
