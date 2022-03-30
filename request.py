import requests as r
import os

url = 'http://127.0.0.1:8080/'
filename = 'test.jpg'
file = {'file': open(filename, 'rb')}

re = r.post(url, files=file)
print(re.content)


