from flask import Flask, render_template, request, redirect, url_for, session
from svm import predict, preprocess_and_train
from sklearn.preprocessing import LabelEncoder
import requests
import json
from db import create_db, DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

app = Flask(__name__)
app.secret_key = 'secrettt'

create_db()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        question1 = request.form['question1']
        question2 = request.form['question2']
        question3 = request.form['question3']
        question4 = request.form['question4']
        question5 = request.form['question5']
        question6 = request.form['question6']
        question7 = request.form['question7']
        question8 = request.form['question8']
        question9 = request.form['question9']
        question10 = request.form['question10']
        question11 = request.form['question11']
        question12 = request.form['question12']
        question13 = request.form['question13']
        question14 = request.form['question14']
        question15 = request.form['question15']
        question16 = request.form['question16']
        question17 = request.form['question17']
        question18 = request.form['question18']
        question19 = request.form['question19']
        question20 = request.form['question20']
        question21 = request.form['question21']
        question22 = request.form['question22']
        question23 = request.form['question23']
        question24 = request.form['question24']
        question25 = request.form['question25']
        question26 = request.form['question26']
        question27 = request.form['question27']
        question28 = request.form['question28']
        question29 = request.form['question29']
        question30 = request.form['question30']
        question31 = request.form['question31']
        question32 = request.form['question32']

        new_data = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19, question20, question21, question22, question23, question24, question25, question26, question27, question28, question29, question30, question31, question32]

        Classifier = preprocess_and_train()
        result = predict(new_data, Classifier)
        return render_template('result.html', result=result)
    else:
        return render_template('result.html')

@app.route('/login_process')
def login_process():
    return render_template('login_process.html')

@app.route('/personality_test')
def personality_test():
    return render_template('form.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
