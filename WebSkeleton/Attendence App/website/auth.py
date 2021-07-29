from website.models import User
from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from .models import User
from flask import redirect
from flask import url_for
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user, current_user



auth=Blueprint("auth",__name__)

@auth.route("/Login",methods=['GET','POST'])
def login():
    if(request.method=="POST"):
        email=request.form.get("email")
        password=request.form.get("password")

        user=User.query.filter_by(email=email).first()
        if(user):
            if (check_password_hash(user.password,password)):
                flash("Logged In Sucessfully",category="success")
                login_user(user,remember=True)
            else:
                flash("Incorrect Password Try Again", category="error")
        else:
            flash("Account Does'nt Exist Create a New One",category="error")




    return render_template("login.html", user=current_user)

@auth.route("/Logout")
@login_required
def Logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/Signup",methods=['GET','POST'])
def Signup():
    if(request.method=="POST"):
        email=request.form.get("email")
        firstname=request.form.get("firstname")
        lastname=request.form.get("lastname")
        password1=request.form.get("password1")
        password2=request.form.get("password2")
        
        user=User.query.filter_by(email=email).first()

        if(user):
            flash("Email Already Exist !!",category="error")
        elif(len(email)<4):
            flash("Invalid Email Address",category="error")
        elif(len(firstname)<2):
            flash("Name Should Be Much Longer",category="error")
        elif(len(lastname)<1):
            flash("Name Should Be Much Longer",category="error")
        elif(password1!=password2):
            flash("Enter Passwords Correctly",category="error")
        elif(len(password1)<7):
            flash("Follow The Password Rules",category="error")
        else:
            newuser = User(email=email,firstname=firstname, password=generate_password_hash(password1, method='sha256'))
            db.session.add(newuser)
            db.session.commit()
            flash("Account Created Successfully",category="success")
            return redirect(url_for("auth.login"))


    return render_template("signup.html", user=current_user)