import requests

r = requests.get(url="https://desavfio-pro.herokuapp.com/resp?r=RW0gdGVycmEgZGUgcXVlbSB0ZW0gdW0gb2xobyBlIHJlaQ==")
print(r.text)