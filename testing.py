import requests

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"75",
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"127.0.0.1:5000",
    "Origin":"http://127.0.0.1:5000",
    "Referer":"http://127.0.0.1:5000/login",
    "Sec-Fetch-Dest":"document",
    "Sec-Fetch-Mode":"navigate",
    "Sec-Fetch-Site":"same-origin",
    "Sec-Fetch-User":"?1",
    "Sec-GPC":"1",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

print(requests.post('http://127.0.0.1:5000/reset', data='password=test1&email=test1%40gmail.com&new_password=test2', headers=headers).text)