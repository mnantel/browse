import requests
import time

urls = [
    'https://www.facebook.com',
    'https://www.google.com',
    'https://www.fortinet.com',
    'https://cbc.ca',
    'https://lotoquebec.com',
    'http://192.168.10.3'
]

while True:
    for u in urls:
        print("Getting: "+u)
        r = requests.get(u, allow_redirects=True)
    time.sleep(2)