import requests
import csv
from os import path 
import argparse

class ApiFetcher:

    def __init__(self, url,quiet=False,city=None):
        self.url=url
        self.users=[]
        self.quiet=quiet
        self.city=city
    
    def fetch_data(self):
        response=requests.get(self.url)
        if response.status_code==200:
            if not self.quiet:
                print("Data fetched successfully")
            self.users=response.json()
        else:
            if not self.quiet:
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
                if self.city:
                    if city.lower()==self.city.lower():
                        writer.writerow([name,email,city,lat])
                else:
                    continue

                
                
        if not self.quiet:
            print(f"Data saved to {filename} successfully.")
        

    def run(self, filename,location):

        self.fetch_data()
        self.save_to_csv(filename,location)



if __name__=="__main__":

    parse=argparse.ArgumentParser(description="Fetch user data from API and save to CSV")
    parse.add_argument('--output', type=str,default="users_data.csv", help="Name of the output CSV file")
    parse.add_argument('--quiet', action='store_true', help="Suppress output messages")
    parse.add_argument('--city', type=str, help="Mention the city to filter users")



    args=parse.parse_args()
    output=args.output

    url="https://jsonplaceholder.typicode.com/users"
    fetcher=ApiFetcher(url,args.quiet,args.city)
    fetcher.run(output,r'.')