import requests
import time

urls = [
    'https://www.facebook.com',
    'https://www.google.com',
    'https://www.fortinet.com',
    'https://radiocanada.ca',
    'https://lotoquebec.ca'
]

while True:
    for u in urls:
        print("Getting: "+u)
        r = requests.get(u, allow_redirects=True)
    time.sleep(2)