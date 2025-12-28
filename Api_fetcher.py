import requests
import csv
from os import path


def fetch_api_data(url,location):
    response=requests.get(url)

    if response.status_code==200:
        print('File Fetched')
        users=response.json()
    else:
        print('Error')


    nw_location=path.join(location,"Users.csv")
    with open(nw_location,mode="w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(['Name','Email','City'])

        for user in users:
            name=user.get('name',"N/A")
            email=user.get('email',"N/A")
            city=user.get("address",'{}').get("city","N/A")

            writer.writerow([name," || ",email," || ",city])

    print("Success")


url=input("Enter URL: ")
location=input("Enter Location to save file: ")

fetch_api_data(url,location)

