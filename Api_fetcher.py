import requests
import csv

url=r"https://jsonplaceholder.typicode.com/users"
response=requests.get(url)

if response.status_code==200:
    print('File Fetched')
    users=response.json()
else:
    print('Error')


with open("Users.csv",mode="w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(['Name','Email','City'])

    for user in users:
        name=user.get('name',"N/A")
        email=user.get('email',"N/A")
        city=user.get("address",'{}').get("city","N/A")

        writer.writerow([name," || ",email," || ",city])

print("Success")
