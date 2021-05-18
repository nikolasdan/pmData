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
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'extremedevalt@gmail.com'
app.config['MAIL_PASSWORD'] = 'TG)-DAu^4s7q-5I)6P#T*C_R1p3t@x98'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

injections_list = ["GenericBlind", "Generic_ErrorBased", "Generic_SQLI", "Generic_TimeBased", "Generic_UnionSelect"]

config = {
    "email": "extremedevalt@gmail.com",
    "password": "TG)-DAu^4s7q-5I)6P#T*C_R1p3t@x98"
}

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


"""
    setup = {
        "search": "",
        "http": "",
        "name": "",
        "subdomain": "",
        "domain_ends": "",
        "parameters": [],
        "db": "",
        "os": "",
        "emails": [],
        "passwords": [],
        "usernames": [],
        "other-data": [],
        "url": url,
        "adminer": False,
        "adminer-version": "unknown",
        "injection-type": "unknown",
        "injected-url": "unknown",
        "xss": False,
        'xss-url': ""
    }
"""

"""
{"search": "/cat_podrobno2.php?id=3&main_category_id=6&category_id=7", 
"http": "https", 
"name": "zelenastrandja", 
"subdomain": "www", 
"domain_ends": "com", 
"parameters": [], 
"db": "", 
"os": "", 
"emails": [], 
"passwords": [], 
"usernames": [], 
"other-data": [], 
"url": "https://www.zelenastrandja.com/cat_podrobno2.php?id=3&main_category_id=6&category_id=7", 
"adminer": False, 
"adminer-version": "unknown",
"injection-type": "Generic_SQLI", 
"injected-url": "https://www.zelenastrandja.com/cat_podrobno2.php?id=3&main_category_id=6&category_id=7(sqlattempt2)", 
"xss": True, 
"xss-url": "https://www.zelenastrandja.com/cat_podrobno2.php?id=3&main_category_id=6&category_id=%22%3E%3Cscript%3Ealert(%27XSS%27)%3C/script%3E"}"""
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        mytext = requests.post('http://127.0.0.1:5000/check', data=str(request.form['website-url']))
        stuff = mytext.text.replace("'", '"')
        email_info = Message('Results', sender = app.config['MAIL_USERNAME'], recipients = ['lucian.volanschi29@yahoo.com']);email_info.body = render_template(
            'mail_results.html', 
            sql_bool='True' if re.search('"injected-url": "(.*?)"', str(stuff)).group(1) != 'unknown' else 'False',
            xss_bool=re.search('"xss": (.*?),', str(stuff)).group(1),
            adminer_bool=re.search('"adminer": (.*?),', str(stuff)).group(1),
            cms_bool=re.search('"xss": (.*?),', str(stuff)).group(1),
            captcha_bool =re.search('"xss": (.*?),', str(stuff)).group(1),
            protection_bool = re.search('"xss": (.*?),', str(stuff)).group(1),
            csrf_bool=re.search('"xss": (.*?),', str(stuff)).group(1),
            ports_bool=re.search('"xss": (.*?),', str(stuff)).group(1),
            hackable_bool=re.search('"xss": (.*?),', str(stuff)).group(1),
            subdomains_bool=re.search('"xss": (.*?),', str(stuff)).group(1),

            sql_url=re.search('"injected-url": "(.*?)"', str(stuff)).group(1),
            xss_url=re.search('"xss-url": "(.*?)"', str(stuff)).group(1),
            adminer_url=re.search('"adminer-version": "(.*?)"', str(stuff)).group(1),
            cms_name=re.search('"injected-url": "(.*?)"', str(stuff)).group(1),
            ports=re.search('"injected-url": "(.*?)"', str(stuff)).group(1),
            nmap_report=re.search('"injected-url": "(.*?)"', str(stuff)).group(1),
            whois_report=str(whois.whois(re.search('"name": "(.*?)"', str(stuff)).group(1) + re.search('"domain_ends": "(.*?)"', str(stuff)).group(1)))
            );email_info.html = render_template(
            'mail_results.html', 
            sql_bool='True' if re.search('"injected-url": "(.*?)"', str(stuff)).group(1) != 'unknown' else 'False',
            xss_bool=re.search('"xss": (.*?),', str(stuff)).group(1),
            adminer_bool=re.search('"adminer": (.*?),', str(stuff)).group(1),
            cms_bool=re.search('"xss": (.*?),', str(stuff)).group(1),
            captcha_bool =re.search('"xss": (.*?),', str(stuff)).group(1),
            protection_bool = re.search('"xss": (.*?),', str(stuff)).group(1),
            csrf_bool=re.search('"xss": (.*?),', str(stuff)).group(1),
            ports_bool=re.search('"xss": (.*?),', str(stuff)).group(1),
            hackable_bool=re.search('"xss": (.*?),', str(stuff)).group(1),
            subdomains_bool=re.search('"xss": (.*?),', str(stuff)).group(1),

            sql_url=re.search('"injected-url": "(.*?)"', str(stuff)).group(1),
            xss_url=re.search('"xss-url": "(.*?)"', str(stuff)).group(1),
            adminer_url=re.search('"adminer-version": "(.*?)"', str(stuff)).group(1),
            cms_name=re.search('"injected-url": "(.*?)"', str(stuff)).group(1),
            ports=re.search('"injected-url": "(.*?)"', str(stuff)).group(1),
            nmap_report=re.search('"injected-url": "(.*?)"', str(stuff)).group(1),
            whois_report=str(whois.whois(re.search('"name": "(.*?)"', str(stuff)).group(1) + re.search('"domain_ends": "(.*?)"', str(stuff)).group(1))))
        mail.send(email_info)
        return render_template('result.html')

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
