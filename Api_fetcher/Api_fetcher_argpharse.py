import requests
import csv
from os import path 
import argparse

class ApiFetcher:

    def __init__(self, url):
        self.url=url
        self.users=[]
    
    def fetch_data(self):
        response=requests.get(self.url)
        if response.status_code==200:
            print("Data fetched successfully")
            self.users=response.json()
        else:
            print("Failed to fetch data. Status code:", response.status_code)
    
    def save_to_csv(self,filename,location):
        filename=path.join(location, filename)
        with open(filename, mode='w', newline='') as file:
            writer=csv.writer(file)
            writer.writerow(['Name', 'Email', 'City','Latitude'])
            for user in self.users:
                name=user.get('name', 'n/a')
                email=user.get('email','n/a')
                city=user.get('address',{}).get('city','n/a')
                lat=user.get('address',{}).get('geo',{}).get('lat','0.000000')
                writer.writerow([name,email,city,lat])
                
        
        print(f"Data saved to {filename} successfully.")

    def run(self, filename,location):
        self.fetch_data()
        self.save_to_csv(filename,location)



if __name__=="__main__":

    parse=argparse.ArgumentParser(description="Fetch user data from API and save to CSV")
    parse.add_argument('--output', type=str,default="users_data.csv", help="Name of the output CSV file")
    args=parse.parse_args()
    output=args.output

    url="https://jsonplaceholder.typicode.com/users"
    fetcher=ApiFetcher(url)
    fetcher.run(output,r'.')