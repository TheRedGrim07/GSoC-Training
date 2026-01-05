from flask_cors import CORS
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///Students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

class students(db.Model):

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    score=db.Column(db.Integer,default=0)

    def __repr__(self):
        return f'Student <{self.name}>'
    
    def to_json(self):
        return {"id": self.id, "name": self.name, "score": self.score}

@app.route("/students",methods=['POST','GET','DELETE'])
def manage_student():
    if request.method=='GET':
        name_query=request.args.get('name')
        if name_query:
            found_student=students.query.filter_by(name=name_query.capitalize()).all()
        
        else:
            found_student=students.query.all()
        

        output_list=[s.to_json() for s in found_student]
        return {"Student":output_list}, 200
    

    elif request.method=='POST':
        data=request.get_json()
        Name=data.get('name',"")
        result=data.get('score',0)

        new_student=students(name=Name.capitalize(),score=result)
        try:
            db.session.add(new_student)
            db.session.commit()
            return{"Message":"Added new student"},201
        except:
            return{"Error":"No new student added"},500


    elif request.method=='DELETE':
        data=request.get_json()
        Name=data.get('name',"")
        Name=Name.capitalize()
        student_to_delete=students.query.filter_by(name=Name).all()
        if student_to_delete:
            try:
                for student in student_to_delete:
                    db.session.delete(student)
                    
                db.session.commit()
                return{"Message":"Deleted student"},200
            except:
                return{"Error":"No student deleted"},404
            
        else:
            return{"Error":"No student deleted"},404




if __name__=="__main__":
    with app.app_context():
        db.create_all()
        print("Database Created Successfully")
    app.run(debug=True,port=5002)
