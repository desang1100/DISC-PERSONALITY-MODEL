from flask import Flask, render_template, request, redirect, url_for, session
from svm import predict, preprocess_and_train
from sklearn.preprocessing import LabelEncoder
import requests
import json
from flask_mysqldb import MySQLdb
from db import create_db

app = Flask(__name__)
app.secret_key = 'secrettt'

create_db()

def connection():
    try:
        conn = MySQLdb.connect(host="localhost", user="root", password="", db="disc_db")
        return conn
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        bithdate = request.form['birthdate']
        age = request.form['age']
        gender = request.form['gender']
        address = request.form['address']
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

        new_data = [name,email,birthdate,age,gender,address,question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19, question20, question21, question22, question23, question24, question25, question26, question27, question28, question29, question30, question31, question32]

        Classifier = preprocess_and_train()
        result = predict(new_data, Classifier)
        conn = connection()
        if conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO data (question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19, question20, question21, question22, question23, question24, question25, question26, question27, question28, question29, question30, question31, question32) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name,email,bithdate,age,gender,address,question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19, question20, question21, question22, question23, question24, question25, question26, question27, question28, question29, question30, question31, question32,result))
            conn.commit()

            message = 'Response predicted and added to database successfully'
        else:
            message = 'There was something wrong. Please try again'

        return render_template('result.html', message = message, result = result, new_data = new_data, name = name)



        return render_template('result.html', result=result)
    else:
        return render_template('result.html')

@app.route('/login_process')
def login_process():
    return render_template('login_process.html')

@app.route('/personality_test')
def personality_test():
    return render_template('form.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == "POST":
        email = request.form['email']
        fname = request.form['fname']
        mname = request.form['mname']
        lname = request.form['lname']
        password = request.form['password']

        conn = connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE email = %s", [email])
            account = cur.fetchall()
            if account:
                message = "Account already exist!"
            else:
                message = "Account created successfully!"
                cur.execute("INSERT INTO users VALUES(NULL,%s, %s, %s, %s, %s)", (email, fname, mname , lname, password))
                conn.commit()
        conn.close()

    return render_template('register.html', message = message)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
            user = cur.fetchone()
        conn.close()

        if user:
            session['user'] = user
            return redirect(url_for('personality_test'))
        else:
            message = 'Invalid email or password'
            return redirect(url_for('login', message = message))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
