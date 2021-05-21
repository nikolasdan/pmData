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

# logging with this account without our consent will be reported
# for those reviewing this code, we suggest not to log in

app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'pmdata.contact@gmail.com'
app.config['MAIL_PASSWORD'] = '39?ZTxVdG?-yD9CN+^Ny@xcD'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

injections_list = ["GenericBlind", "Generic_ErrorBased", "Generic_SQLI", "Generic_TimeBased", "Generic_UnionSelect"]

config = {
    "email": "pmdata.contact@gmail.com",
    "password": "39?ZTxVdG?-yD9CN+^Ny@xcD"
}

@app.route('/login', methods=["POST", "GET"])
def login(): 
    if request.method == 'GET':
        return render_template('login.html')
    else:
        f = login_apis(username=request.form['username'], password=request.form['password'], email=request.form['email'])
        if f == 200:
            return render_template('account.html', balance=balance(request.form['email']), account_type = get_role(request.form['email']), email=request.form['email'], user=request.form['username'])
        elif f == 526:
            return render_template('login.html', message='You created your account with success!')
        else:
            return render_template('login.html', message='Your credentials are invalid!')
        
@app.route('/injections/<injection>', methods=["GET"])
def payload_returner(injection):
    response = make_response(str(open('injections/{0}.txt'.format(str(injection)), 'r', encoding='utf-8').read()), 200)
    response.mimetype = "text/plain"
    return response

@app.route('/terms_of_service', methods=["GET"])
def terms_of_service():
    return render_template('terms_of_service.html')

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
        mytext = requests.post('http://127.0.0.1:5000/check', data=str(request.form['website-url']))
        stuff = mytext.text.replace("'", '"')
        email_info = Message('Results', sender = app.config['MAIL_USERNAME'], recipients = [request.form['email']]);email_info.body = render_template(
            'mail_results.html', 
            sql_bool='True' if re.search('"injected-url": "(.*?)"', str(stuff)).group(1) != 'unknown' else 'False',
            xss_bool=re.search('"xss": (.*?),', str(stuff)).group(1),
            adminer_bool=re.search('"adminer": (.*?),', str(stuff)).group(1),
            cms_bool='unknown',
            captcha_bool ='unknown',
            protection_bool = 'unknown',
            csrf_bool='unknown',
            ports_bool='unknown',
            hackable_bool='unknown',
            subdomains_bool='unknown',

            sql_url=re.search('"injected-url": "(.*?)"', str(stuff)).group(1),
            xss_url=re.search('"xss-url": "(.*?)"', str(stuff)).group(1),
            adminer_url=re.search('"adminer-version": "(.*?)"', str(stuff)).group(1),
            cms_name='unknown',
            ports='unknown',
            nmap_report='unknown',
            whois_report=str(whois.whois(re.search('"name": "(.*?)"', str(stuff)).group(1) + re.search('"domain_ends": "(.*?)"', str(stuff)).group(1))));email_info.html = render_template(
            'mail_results.html', 
            sql_bool='True' if re.search('"injected-url": "(.*?)"', str(stuff)).group(1) != 'unknown' else 'False',
            xss_bool=re.search('"xss": (.*?),', str(stuff)).group(1),
            adminer_bool=re.search('"adminer": (.*?),', str(stuff)).group(1),
            cms_bool='unknown',
            captcha_bool ='unknown',
            protection_bool = 'unknown',
            csrf_bool='unknown',
            ports_bool='unknown',
            hackable_bool='unknown',
            subdomains_bool='unknown',

            sql_url=re.search('"injected-url": "(.*?)"', str(stuff)).group(1),
            xss_url=re.search('"xss-url": "(.*?)"', str(stuff)).group(1),
            adminer_url=re.search('"adminer-version": "(.*?)"', str(stuff)).group(1),
            cms_name='unknown',
            ports='unknown',
            nmap_report='unknown',
            whois_report=str(whois.whois(re.search('"name": "(.*?)"', str(stuff)).group(1) + re.search('"domain_ends": "(.*?)"', str(stuff)).group(1))))
        mail.send(email_info)
        return render_template('result.html')

@app.route('/profile/<name>', methods=["GET"])
def user_profile(name):
    f = get_user(name)
    if f is None:
        return render_template_string('UNKNOWN')
    else:
        return render_template_string('Username: {} | Role: {}'.format(str(name), str(f)))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact') 
def contact():
    return render_template('contact.html')

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/profile/<user>/update_type', methods=["POST"])
def update_account(user):
    return render_template_string(change_role(user, request.get_data().decode()))

@app.route('/admin/<user>', methods=["POST"])
def admin_user(user):
    return render_template_string(adminer_test(user, request.get_data().decode()))

try:
    app.run(debug=True)
except Exception as error:
    print(error)
