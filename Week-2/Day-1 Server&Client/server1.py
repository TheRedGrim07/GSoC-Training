from flask import Flask, request

app= Flask(__name__)

@app.route("/")
def home():
    return({"status": "online", "message": "GSoC Training Server"})

@app.route("/hello/<name>")
def admin(name):
    return({"greeting": f"Hello, {name}!", "name_length": len(name)})

@app.route("/square/<number>")
def square(number):
    X=int(number)
    Y=X*X
    return({"number": X, "square": Y})


@app.route("/add")
def adder():
    a=int(request.args.get('a',0))
    b=int(request.args.get('b',0))
    c=a+b
    return({"a": a, "b": b, "result": c})

@app.route('/login', methods=['Post'])
def login():

    data=request.get_json()

    if data["username"]=="admin":
        return({"Access":"Granted"})

if __name__=="__main__":
    app.run()

