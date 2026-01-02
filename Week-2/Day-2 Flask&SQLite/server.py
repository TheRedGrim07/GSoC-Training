from flask import Flask,request
from database import database

app=Flask(__name__)

@app.route("/add",methods=["POST"])
def add_user():
    data=request.get_json()

    name=data.get("name")
    score=data.get("score",0)

    db=database()

    db.add_student(name,score)
    db.close()
    return({"message":"User added successfully"})


@app.route("/results/<name>")
def results(name):
    db=database()
    n=name.capitalize()
    a=db.get_student(n)
    db.close()
    return a

if __name__=="__main__":
    app.run(debug=True)