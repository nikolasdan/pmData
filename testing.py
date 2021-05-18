import requests, json

mytext = requests.post('http://127.0.0.1:5000/check', data=str('https://test.com/teastaegfae'))

import re
print(json.loads(mytext.text.replace("'", "\"").replace('None', 'null').replace('False', 'false').replace('True', 'true'))['search'])
 