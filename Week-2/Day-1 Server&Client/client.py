import requests

my_file={"username":"admin"}

response= requests.post("http://127.0.0.1:5000/login",json=my_file)

print(response.json())