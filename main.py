from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_process')
def login_process():
    render_template('login_process.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
