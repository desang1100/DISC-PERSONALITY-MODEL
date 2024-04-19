# import MySQLdb
from flask_mysqldb import MySQLdb

# MySQL Configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'disc_db'

def create_db():
    # Connect to MySQL
    conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME))
    conn.commit()

    # Switch to the database
    cursor.execute("USE {}".format(DB_NAME))

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(100) UNIQUE NOT NULL,
            fname VARCHAR(100) NOT NULL,
            mname VARCHAR(100) NOT NULL,
            lname VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()

    # Create categories table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            FOREIGN KEY (user_id) REFERENCES users(id),
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            birthdate VARCHAR(100) NOT NULL,
            age VARCHAR(100) NOT NULL,
            gender VARCHAR(100) NOT NULL,
            address VARCHAR(100) NOT NULL, 
            birthplace VARCHAR(100) NOT NULL,
            age VARCHAR(100) NOT NULL,
            question1 VARCHAR(100) NOT NULL,
            question2 VARCHAR(100) NOT NULL,
            question3 VARCHAR(100) NOT NULL,
            question4 VARCHAR(100) NOT NULL,
            question5 VARCHAR(100) NOT NULL,
            question6 VARCHAR(100) NOT NULL,
            question7 VARCHAR(100) NOT NULL,
            question8 VARCHAR(100) NOT NULL,
            question9 VARCHAR(100) NOT NULL,
            question10 VARCHAR(100) NOT NULL,
            question11 VARCHAR(100) NOT NULL,
            question12 VARCHAR(100) NOT NULL,
            question13 VARCHAR(100) NOT NULL,
            question14 VARCHAR(100) NOT NULL,
            question15 VARCHAR(100) NOT NULL,
            question16 VARCHAR(100) NOT NULL,
            question17 VARCHAR(100) NOT NULL,
            question18 VARCHAR(100) NOT NULL,
            question19 VARCHAR(100) NOT NULL,
            question20 VARCHAR(100) NOT NULL,
            question21 VARCHAR(100) NOT NULL,
            question22 VARCHAR(100) NOT NULL,
            question23 VARCHAR(100) NOT NULL,
            question24 VARCHAR(100) NOT NULL,
            question25 VARCHAR(100) NOT NULL,
            question26 VARCHAR(100) NOT NULL,
            question27 VARCHAR(100) NOT NULL,
            question28 VARCHAR(100) NOT NULL,
            question29 VARCHAR(100) NOT NULL,
            question30 VARCHAR(100) NOT NULL,
            question31 VARCHAR(100) NOT NULL,
            question32 VARCHAR(100) NOT NULL,
            results VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()


    cursor.close()
    conn.close()
