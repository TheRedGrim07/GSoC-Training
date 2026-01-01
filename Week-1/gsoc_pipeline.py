import sqlite3
import requests
import argparse

class DBHandler:

    def __init__(self,db_name="users.db"):
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()
        self.create_table()
        print("Database connected and table ready.")

    def create_table(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT,
                              email TEXT,
                              city TEXT,
                              latitude REAL)''')
        self.conn.commit()
    
    def insert_user(self,name,email,city,latitude):
            check_query = 'SELECT id FROM users WHERE email=?'
            self.cursor.execute(check_query, (email,))
            existing_user = self.cursor.fetchone()

            if existing_user:
                print("User already exists.")
                return None
            
            count=0
            if '@' in email and '.' in email:
                query='''INSERT INTO users (name, email, city, latitude) 
                                    VALUES(?,?,?,?)'''
                self.cursor.execute(query,(name,email,city,latitude))
                self.conn.commit()
                print("User inserted successfully.")
            else:
                print("Invalid email format. User not inserted.")

    def total_users(self):
        self.cursor.execute('SELECT COUNT(*) FROM users')
        count=self.cursor.fetchone()[0]
        return count
    
    def Northernmost_user(self):
        self.cursor.execute('SELECT * FROM users ORDER BY latitude DESC LIMIT 1')
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()


class Apifetcher:
    def __init__(self,url):
         self.url=url

    

    def fetch_data(self):
         response=requests.get(self.url)
         if response.status_code==200:
            return response.json()
         else:
            print("Failed to retrieve data")
            return None

if __name__=="__main__":
    db=DBHandler()
    api_url="https://jsonplaceholder.typicode.com/users"
    fetcher=Apifetcher(api_url)
    data=fetcher.fetch_data()
    parser=argparse.ArgumentParser()
    parser.add_argument('--report',action='store_true',help="Fetch data from API and store in database")
    args=parser.parse_args()

    if args.report:
        print(f'Total users: {db.total_users()}')
        print(f'Northernmost user: {db.Northernmost_user()}')

    elif data:
        for user in data:
            name=user.get('name')
            email=user.get('email')
            city=user.get('address',{}).get('city')
            latitude=user.get('address',{}).get('geo',{}).get('lat')
            db.insert_user(name,email,city,latitude)
    
    
    db.close()

        
    

    
