from flask import Flask,request
from database import database

app=Flask(__name__)

@app.route('/students',methods=['GET','POST','DELETE'])
def manage_server():
    db=database()
    # Read data
    if(request.method=='GET'):
        name=request.args.get('name')
        if name:
            result=db.get_student(name)
            if len(result)>0:
                db.close()
                return {"students":result},200
            else:
                db.close()
                return {"Error":"No Entry in DataBase"},404
        else:
            db.close()
            return {"Error":"No Name in Argument"},404
        
        

    #Add students
    elif(request.method=='POST'):
        data=request.get_json()
        name=data.get('name',"")
        score=data.get('score',0)
        db.add_student(name,score)
        db.close()
        return {"Name":"Added successfully"},201
    #Delete Name
    elif(request.method=='DELETE'):

        data=request.get_json()
        success=db.delete_student(data.get('name'))
        db.close()
        if success:
            return {'deleted':'successfully'},200
        else:
            return{'error':'not found'},404




if __name__=="__main__":
    app.run(debug=True,port=5001)