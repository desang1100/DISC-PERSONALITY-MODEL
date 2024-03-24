from flask import Flask,render_template,requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! This is my Flask app.'

if __name__ == '__main__':
    app.run(debug=True)
