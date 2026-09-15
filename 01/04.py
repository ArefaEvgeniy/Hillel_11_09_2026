import requests

res = requests.get("https://lms.ithillel.ua/")
print(res.status_code)
print(res.content.decode())

a = 100
print(a - 50)
