import requests
import time
from fake_useragent import UserAgent

url = "https://webscraper.io/test-sites" 
session = requests.Session()

headers = {
    "User-Agent": UserAgent().random,
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, pr",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/",
} 
 

time.sleep(2)  # Sleep to mimic human behavior

r = session.get(url , headers=headers)
# print(r.text)

with open("file.html", "w") as f:
    f.write(r.text)