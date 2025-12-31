import sqlite3
import argparse

class DBHandler:

    def __init__(self,db_name="users.db"):
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()
        self.create_table()
    
    def create_table(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT,
                              email TEXT,
                              city TEXT,
                              latitude REAL)''')
        self.conn.commit()
    
    def insert_user(self,name,email,city,latitude):
            
            query='''INSERT INTO users (name, email, city, latitude) 
                                VALUES(?,?,?,?)'''
            self.cursor.execute(query,(name,email,city,latitude))
            self.conn.commit()
    
    def display_users(self,search_id=None):
        if search_id:
            self.cursor.execute('SELECT * FROM users WHERE id=?',(search_id,))
            row=self.cursor.fetchone()
            if row:
                print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, City: {row[3]}, Latitude: {row[4]}")
            else:
                print("User not found.")

        else:
            self.cursor.execute('SELECT * FROM users')
            rows=self.cursor.fetchall()
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, City: {row[3]}, Latitude: {row[4]}")
        


    def close(self):
        self.conn.close()
    
if __name__=="__main__":
    db=DBHandler()

    parser=argparse.ArgumentParser(description="Database Handler")
    parser.add_argument('--insert',action='store_true',help="Insert in database file")
    parser.add_argument('--display',action='store_true',help="Display database contents")
    parser.add_argument('--search_id', type=int, help="Find a specific user by ID")

    args=parser.parse_args()
    if args.insert:
        count = input("Enter no. of users to insert: ")
        for i in range(int(count)):
            name = input("Enter name: ")
            email = input("Enter email: ")
            city = input("Enter city: ")
            
            latitude = float(input("Enter latitude: ")) 
            
            db.insert_user(name, email, city, latitude)
        

    if args.display or args.search_id:
        db.display_users(search_id=args.search_id)
    db.close()