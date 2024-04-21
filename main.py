from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQLdb
from sklearn.preprocessing import LabelEncoder
from svm import predict, preprocess_and_train
import requests
import json
from db import create_db, DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

app = Flask(__name__)
app.secret_key = 'secrettt'

create_db()

def connection():
    try:
        conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)
        return conn
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/personality_test')
def personality_test():
    return render_template('form.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    message = ''
    result = None
    if not 'logged_in' in session:
        message = 'Please login first'
        return render_template('login.html', message = message)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        birthdate = request.form['birthDate']
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

        new_data = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19, question20, question21, question22, question23, question24, question25, question26, question27, question28, question29, question30, question31, question32]
        Classifier = preprocess_and_train()
        results = predict(new_data, Classifier)

        conn = connection()
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO data
                VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (session['user_id'], name, email, birthdate, age, gender, address, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19, question20, question21, question22, question23, question24, question25, question26, question27, question28, question29, question30, question31, question32, results))
            conn.commit()
        conn.close()
        message = 'Response predicted and added to database successfully'

        return render_template('result.html', message = message, result = results, new_data = new_data, name = name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/history', methods=['GET', 'POST'])
def history():
    if not 'logged_in' in session:
        message = 'Please login first'
        return render_template('login.html', message = message)

    conn = connection()
    with conn.cursor() as cur:
        cur.execute("""
                SELECT u.id, u.email, u.fname, u.mname, u.lname, d.name, d.email, d.birthDate, d.age, d.gender, d.address, d.question1, d.question2, d.question3, d.question4, d.question5, d.question6, d.question7, d.question8, d.question9, d.question10, d.question11, d.question12, d.question13, d.question14, d.question15, d.question16, d.question17, d.question18, d.question19, d.question20, d.question21, d.question22, d.question23, d.question24, d.question25, d.question26, d.question27, d.question28, d.question29, d.question30, d.question31, d.question32, d.results
                FROM users u
                JOIN data d ON u.id = d.user_id
            """)
        data = cur.fetchall()
    conn.close()
    return render_template('history.html', data=data)

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
            session['logged_in'] = True
            session['user_id'] = user[0]
            session['user_email'] = user[1]
            session['user_fname'] = user[2]
            session['user_mname'] = user[3]
            session['user_lname'] = user[4]
            session['user_password'] = user[5]
            return redirect(url_for('personality_test'))
        else:
            message = 'Invalid email or password'
            return redirect(url_for('login', message = message))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    success = ''
    failed = ''
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
                failed = "Account already exist!"
                return render_template('register.html', message = failed)
            else:
                success = "Account created successfully!"
                cur.execute("INSERT INTO users VALUES(NULL,%s, %s, %s, %s, %s)", (email, fname, mname , lname, password))
                conn.commit()
        conn.close()

    return render_template('register.html', message = success)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
