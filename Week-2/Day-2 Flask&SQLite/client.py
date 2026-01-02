import requests

print("------Adding User------")
my_file={"name":"AmAn","score":0}
response=requests.post("http://127.0.0.1:5000/add",json=my_file)
print(response.json())

print("------Getting User------")
response=requests.get("http://127.0.0.1:5000/results/Ayush")
print("Response: ",response.json())