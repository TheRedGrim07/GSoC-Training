import sqlite3
from flask import Flask, render_template, redirect, url_for, request,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)

app.config['SECRET_KEY']="Thisisasecretkey"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///taskmaster.db"
db=SQLAlchemy(app)

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(UserMixin,db.Model):

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),unique=True,nullable=False)
    password_hash=db.Column(db.String(150),nullable=False)

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
with app.app_context():
    db.create_all()

#---Routes----
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        new_username=request.form.get('username')
        new_password=request.form.get('password')
        remember_me=request.form.get('remember')

        user=User.query.filter_by(username=new_username).first()
        if user and user.check_password(new_password):
            login_user(user,remember=(remember_me is not None))
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid login, enter Again")
            return redirect(url_for('login'))
            

    return render_template('login.html')

@app.route('/register',methods=['POST','GET'])
def register():
    
    
    if request.method=='POST':
        new_username=request.form.get('username')
        new_password=request.form.get('password')
        if User.query.filter_by(username=new_username).first():
            flash("User Already Exist")
            return redirect(url_for('login'))
            
        
        new_user=User(username=new_username)
        new_user.set_password(new_password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html',name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__=="__main__":
    app.run(debug=True)