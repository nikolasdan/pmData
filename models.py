import mysql.connector as mysql
from tabulate import tabulate

secret_key = '6969696969696969696969'


def login_apis(email, password, username):
    HOST = "localhost"
    DATABASE = ""
    USER = "root"
    PASSWORD = ""

    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    cursor.execute("create database if not exists ssssssssssssssssssssssss")
    cursor.execute("use ssssssssssssssssssssssss")
    cursor.execute("""create table if not exists accounts (
        `email` varchar(255) not null,
        `username` varchar(255) not null,
        `password` varchar(255) not null,
        `balance` varchar(255) not null,
        `account_type` char(255) NOT NULL,
        `role` varchar(255) NOT NULL,
        `profile_picture` varchar(255) NOT NULL
    )""")
    cursor.execute("""SELECT password FROM accounts WHERE email = '{}';""".format(str(email), str(username)))
    if str(cursor.fetchall()).startswith('[]'):
        cursor.execute("""insert into accounts (email, password, username, account_type, balance, role, profile_picture) values (%s, %s, %s, %s, 0, 'Member', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.CzXGij1NaAy5LLNUbvw5hwHaHa%26pid%3DApi&amp;f=1')""", params=(email, password, username, 'Trial'))
        db_connection.commit()
        return 526
    else:
        cursor.execute("""SELECT EMAIL, PASSWORD, USERNAME FROM accounts WHERE EMAIL = '{}' AND PASSWORD = '{}' AND USERNAME = '{}';""".format(email, password, username))
        if str(cursor.fetchall()) == '[]':
            return 400
        else:
            return 200

def ifadmin(email):
    HOST = "localhost"
    DATABASE = ""
    USER = "root"
    PASSWORD = ""

    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    cursor.execute("create database if not exists ssssssssssssssssssssssss")
    cursor.execute("use ssssssssssssssssssssssss")
    cursor.execute("""create table if not exists accounts (
        `email` varchar(255) not null,
        `username` varchar(255) not null,
        `password` varchar(255) not null,
        `balance` varchar(255) not null,
        `account_type` varchar(255) NOT NULL,
        `role` varchar(255) NOT NULL,
        `profile_picture` varchar(255) NOT NULL
    )""")
    cursor.execute("""SELECT role FROM accounts WHERE email = '{}';""".format(str(email))) 
    f = str(cursor.fetchall())
    print(f)
    if f == '[]':
        return 'unknown'
    else:
        return f.split('[(\'')[1].split('\',)]')[0]

def edit_password(email, password, new_password):
    HOST = "localhost"
    DATABASE = ""
    USER = "root"
    PASSWORD = ""

    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    cursor.execute("create database if not exists ssssssssssssssssssssssss")
    cursor.execute("use ssssssssssssssssssssssss")
    cursor.execute("""create table if not exists accounts (
        `email` varchar(255) not null,
        `username` varchar(255) not null,
        `password` varchar(255) not null,
        `balance` varchar(255) not null,
        `account_type` varchar(255) NOT NULL,
        `role` varchar(255) NOT NULL,
        `profile_picture` varchar(255) NOT NULL
    )""")
    cursor.execute("""SELECT role FROM accounts WHERE email = '{}' AND password = '{}';""".format(str(email), str(password))) 
    f = cursor.fetchall()
    if f == '[]':
        return 'unknown'
    else:
        print(f)
        if 'Admin' in f:
            return 'admin_error'
        else:
            cursor.execute("UPDATE accounts SET password = '{}' WHERE email = '{}' AND password = '{}';".format(str(new_password), str(email), str(password))) 
            db_connection.commit()
            f = str(cursor.fetchall())
            if f == '[]':
                return 'cannot change'
            else:
                return f

def delete_user(email, secret):
    if secret != secret_key:
        return 120
    HOST = "localhost"
    DATABASE = ""
    USER = "root"
    PASSWORD = ""

    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    cursor.execute("create database if not exists ssssssssssssssssssssssss")
    cursor.execute("use ssssssssssssssssssssssss")
    cursor.execute("""create table if not exists accounts (
        `email` varchar(255) not null,
        `username` varchar(255) not null,
        `password` varchar(255) not null,
        `balance` varchar(255) not null,
        `account_type` varchar(255) NOT NULL,
        `role` varchar(255) NOT NULL,
        `profile_picture` varchar(255) NOT NULL
    )""")
    cursor.execute("""DELETE FROM accounts WHERE email = '{}';""".format(str(email))) 
    db_connection.commit()
    return str(cursor.fetchall())

def get_role(email):
    HOST = "localhost"
    DATABASE = ""
    USER = "root"
    PASSWORD = ""

    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    cursor.execute("create database if not exists ssssssssssssssssssssssss")
    cursor.execute("use ssssssssssssssssssssssss")
    cursor.execute("""create table if not exists accounts (
        `email` varchar(255) not null,
        `username` varchar(255) not null,
        `password` varchar(255) not null,
        `balance` varchar(255) not null,
        `account_type` varchar(255) NOT NULL,
        `role` varchar(255) NOT NULL,
        `profile_picture` varchar(255) NOT NULL
    )""")
    cursor.execute("""SELECT account_type FROM accounts WHERE email = '{}';""".format(str(email)))
    f = str(cursor.fetchall())
    if f == '[]':
        return 'unknown'
    else:
        print(f)
        return f.split('[(\'')[1].split('\',)')[0]

def get_user(user):
    HOST = "localhost"
    DATABASE = ""
    USER = "root"
    PASSWORD = ""

    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    cursor.execute("create database if not exists ssssssssssssssssssssssss")
    cursor.execute("use ssssssssssssssssssssssss")
    cursor.execute("""create table if not exists accounts (
        `email` varchar(255) not null,
        `username` varchar(255) not null,
        `password` varchar(255) not null,
        `balance` varchar(255) not null,
        `account_type` char(255) NOT NULL,
        `role` varchar(255) NOT NULL,
        `profile_picture` varchar(255) NOT NULL
    )""")
    cursor.execute("""SELECT role FROM accounts WHERE email = '{}';""".format(str(user)))
    g = str(cursor.fetchall())
    if g == '[]':
        return None
    else:
        
        return g.split('[(\'')[1].split('\'')[0]


def change_role(email, secret):
    if secret != secret_key:
        return 120
    HOST = "localhost"
    DATABASE = ""
    USER = "root"
    PASSWORD = ""

    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    cursor.execute("create database if not exists ssssssssssssssssssssssss")
    cursor.execute("use ssssssssssssssssssssssss")
    cursor.execute("""create table if not exists accounts (
        `email` varchar(255) not null,
        `username` varchar(255) not null,
        `password` varchar(255) not null,
        `balance` varchar(255) not null,
        `account_type` char(255) NOT NULL,
        `role` varchar(255) NOT NULL,
        `profile_picture` varchar(255) NOT NULL
    )""")
    cursor.execute("""SELECT account_type FROM accounts WHERE email = '{}';""".format(str(email)))
    f = str(cursor.fetchall())
    if f == '[]':
        return 'unknown'
    else:
        if f.split('[(\'')[1].split('\',)')[0] == 'Member':
            cursor.execute("""UPDATE accounts SET account_type = 'Premium' WHERE email = '{}';""".format(str(email)))
            db_connection.commit()
        else:
            cursor.execute("""UPDATE accounts SET role = 'Member' WHERE email = '{}';""".format(str(email)))
            db_connection.commit()
        return str(cursor.fetchall())


def adminer_test(email, secret):
    if secret != secret_key:
        return 120
    HOST = "localhost"
    DATABASE = ""
    USER = "root"
    PASSWORD = ""

    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    cursor.execute("create database if not exists ssssssssssssssssssssssss")
    cursor.execute("use ssssssssssssssssssssssss")
    cursor.execute("""create table if not exists accounts (
        `email` varchar(255) not null,
        `username` varchar(255) not null,
        `password` varchar(255) not null,
        `balance` varchar(255) not null,
        `account_type` char(255) NOT NULL,
        `role` varchar(255) NOT NULL,
        `profile_picture` varchar(255) NOT NULL
    )""")
    cursor.execute("""SELECT role FROM accounts WHERE email = '{}';""".format(str(email)))
    f = str(cursor.fetchall())
    if f == '[]':
        return 'unknown'
    else:
        if f.split('[(\'')[1].split('\',)')[0] == 'Member':
            cursor.execute("""UPDATE accounts SET role = 'Admin' WHERE email = '{}';""".format(str(email)))
            db_connection.commit()
        else:
            cursor.execute("""UPDATE accounts SET role = 'Member' WHERE email = '{}';""".format(str(email)))
            db_connection.commit()
        return str(cursor.fetchall())


def balance(email):
    HOST = "localhost"
    DATABASE = ""
    USER = "root"
    PASSWORD = ""

    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    cursor.execute("create database if not exists ssssssssssssssssssssssss")
    cursor.execute("use ssssssssssssssssssssssss")
    cursor.execute("""create table if not exists accounts (
        `email` varchar(255) not null,
        `username` varchar(255) not null,
        `password` varchar(255) not null,
        `balance` varchar(255) not null,
        `account_type` char(255) NOT NULL,
        `role` varchar(255) NOT NULL,
        `profile_picture` varchar(255) NOT NULL
    )""")
    cursor.execute("""SELECT balance FROM accounts WHERE email = '{}';""".format(str(email)))
    f = str(cursor.fetchall())
    if f == '[]':
        return "unknown"
    else:
        return f.split('[(\'')[1].split('\',)')[0]

def pfp(email):
    HOST = "localhost"
    DATABASE = ""
    USER = "root"
    PASSWORD = ""

    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    cursor.execute("create database if not exists ssssssssssssssssssssssss")
    cursor.execute("use ssssssssssssssssssssssss")
    cursor.execute("""create table if not exists accounts (
        `email` varchar(255) not null,
        `username` varchar(255) not null,
        `password` varchar(255) not null,
        `balance` varchar(255) not null,
        `account_type` char(255) NOT NULL,
        `role` varchar(255) NOT NULL,
        `profile_picture` varchar(255) NOT NULL
    )""")
    cursor.execute("""SELECT profile_picture FROM accounts WHERE email = '{}';""".format(str(email)))
    f = str(cursor.fetchall())
    if f == '[]':
        return 'unknown'
    else:
        return str(f.split('[(\'')[1].split('\',)]')[0])

def change_pfp(email, password, pfp):
    pass