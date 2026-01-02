import sqlite3
class database:
    def __init__(self,db_name="user.db"):
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()
        query='''Create table if not exists user
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    score REAL  
                    )'''
        self.cursor.execute(query)
        self.conn.commit()
        print("Table created")
    def add_student(self,name, score):
        query='''INSERT INTO user (name,score) VALUES (?,?)'''
        self.cursor.execute(query,(name.capitalize(),score))
        self.conn.commit()
        print("User Inserted")

    def get_student(self,name):
        query='''SELECT * FROM user WHERE name=?'''
        self.cursor.execute(query,(name.capitalize(),))

        result=self.cursor.fetchall()
        return result
    def close(self):
        self.conn.close()

if __name__=="__main__":
    db=database()
    db.add_student("aYUSH",92)
    db.add_student("rohit",59)
    db.add_student("teJas",41)

    a=db.get_student("Bismay")
    print (a)
    db.close()
