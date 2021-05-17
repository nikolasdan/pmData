from flask import Flask, render_template, request, redirect, url_for, session, make_response
from flask import render_template
from flask.templating import render_template_string
from check import check
import re, uuid, hashlib, datetime, os
import json
import requests
import whois
import models
from models import *
app = Flask(__name__)

injections_list = ["GenericBlind", "Generic_ErrorBased", "Generic_SQLI", "Generic_TimeBased", "Generic_UnionSelect"]

@app.route('/login', methods=["POST", "GET"])
def login(): 
    if request.method == 'GET':
        return render_template('login.html')
    else:
        print(str(request.get_data()))
        f = login_apis(username=request.form['username'], password=request.form['password'], email=request.form['email'])
        if f == 200:
            return render_template('dashboard.html', user=request.form['username'], role=get_role(request.form['email']))
        elif f == 526:
            return render_template('login.html', message='CREATED')
        else:
            return render_template('login.html', message='BAD')
        

@app.route('/injections/<injection>', methods=["GET"])
def payload_returner(injection):
    response = make_response(str(open('injections/{0}.txt'.format(str(injection)), 'r', encoding='utf-8').read()), 200)
    response.mimetype = "text/plain"
    return response


@app.route('/check', methods=['POST'])
def check_stuff():
    if 'http' in str(request.get_data()) and '://' in str(request.get_data()) and '.' in str(request.get_data()):
        return '{}'.format(str(check(request.get_data().decode())))
    else:
        return 'url syntax'

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        mytext = requests.post('http://127.0.0.1:5000/check', data=str(request.form['website-url'])).text
        return render_template('result.html', result=mytext)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


try:
    app.run()
except Exception as error:
    print(error)
