import mysql.connector as mysql
from tabulate import tabulate

def login_apis(email, password, username):
    HOST = "localhost"
    DATABASE = ""
    USER = "root"
    PASSWORD = ""

    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    cursor.execute("create database if not exists vv")
    cursor.execute("use vv")
    cursor.execute("""create table if not exists accounts (
        `email` varchar(255) not null,
        `username` varchar(255) not null,
        `password` varchar(255) not null,
        `role` enum('Member','Admin') NOT NULL DEFAULT 'Member'
        )""")
    cursor.execute("""SELECT password FROM ACCOUNTS WHERE email = '{}';""".format(str(email)))
    if str(cursor.fetchall()).startswith('[]'):
        cursor.execute("""insert into accounts (email, password, username) values (%s, %s, %s)""", params=(email, password, username))
        db_connection.commit()
        return 526
    else:
        cursor.execute("""SELECT EMAIL, PASSWORD, USERNAME FROM ACCOUNTS WHERE EMAIL = '{}' AND PASSWORD = '{}' AND USERNAME = '{}';""".format(email, password, username))
        if str(cursor.fetchall()) == '[]':
            return 400
        else:
            return 200

def get_role(email):
    HOST = "localhost"
    DATABASE = ""
    USER = "root"
    PASSWORD = ""

    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    cursor.execute("create database if not exists vv")
    cursor.execute("use vv")
    cursor.execute("""create table if not exists accounts (
        `email` varchar(255) not null,
        `username` varchar(255) not null,
        `password` varchar(255) not null,
        `role` enum('Member','Admin') NOT NULL DEFAULT 'Member'
        )""")
    cursor.execute("""SELECT role FROM ACCOUNTS WHERE email = '{}';""".format(str(email)))
    return str(cursor.fetchall()).split('[(\'')[1].split('\'')[0]
