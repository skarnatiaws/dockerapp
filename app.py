from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hellow SIRI World'

if __name__ == '__main':
    app.run(host='0.0.0.0')
