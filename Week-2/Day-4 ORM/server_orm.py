from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///Students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

class students(db.Model):

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    score=db.Column(db.Integer,default=0)

    def __repr__(self):
        return f'Student <{self.name}>'
    
with app.app_context():
    db.create_all()
    print("Database Created Successfully")

if __name__=="__main__":
    app.run(debug=True,port=5002)
