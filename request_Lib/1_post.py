import requests


payload = {'username':'aziz','password':'test'}
response = requests.post("https://httpbin.org/post",data=payload)


print(response.json()) # return python dict
