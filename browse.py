import requests
import time

urls = [
    'https://www.facebook.com',
    'https://www.google.com'
]

while True:
    for u in urls:
        r = requests.get(u, allow_redirects=True)
    time.sleep(2)