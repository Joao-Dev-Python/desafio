import requests

r = requests.get(url="http://127.0.0.1:5000/resp?r=RW0gdGVycmEgZGUgcXVlbSB0ZW0gdW0gb2xobyBlIHJlaQ==")
print(r.text)