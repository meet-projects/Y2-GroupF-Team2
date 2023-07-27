from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyCklxmQCE2Wz2mmup_r5cXGh1MD98Wlf_g",
  "authDomain": "placeilhiring.firebaseapp.com",
  "databaseURL": "https://placeilhiring-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "placeilhiring",
  "storageBucket": "placeilhiring.appspot.com",
  "messagingSenderId": "495542849224",
  "appId": "1:495542849224:web:780f033b9628d0629a9ffd",
  "measurementId": "G-NHVPDTDCXX"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
#Code goes below here

@app.route("/" ,methods=['GET', 'POST'])#choice between company and alum route
def choice():
    if request.method =="GET":
        return render_template("choice.html")
    else: 
        if request.form['answer'] == "employer":
            return render_template('company_login.html')
        else:
            return render_template("alum_login.html")
        


#-----------------------
# alum routes starts here 
# ----------------------



@app.route("/alum_login" ,methods=['GET', 'POST'])#alum login page route
def alum_login():
    if request.method =="GET":
        return render_template("alum_login.html")
    else: 
        try:
            # login code goes here
            print("succses")
            return render_template("employer_login.html")
        except:
            #login fail code goes here
            print("fail")
            return render_template("employer_login.html")
        


@app.route("/alum_signup" ,methods=['GET', 'POST'])#alum signup page route
def alum_signup():
    if request.method =="GET":
        return render_template("alum_signup.html")
    else: 
        # code goes here
        return render_template("employer_home.html")


@app.route("/alum_home" ,methods=['GET', 'POST'])#alum home page route
def alum_home():
    if request.method =="GET":
        return render_template("alum_home.html")
    else: 
        # code goes here
        return render_template("employer_home.html")

@app.route("/alum_profile" ,methods=['GET', 'POST'])#alum profile page route
def alum_profile():
    if request.method =="GET":
        return render_template("alum_profile.html")
    else: 
        # code goes here
        return render_template("employer_home.html")



# --------------------
# company routes starts here
# -------------------



@app.route("/employer_login" ,methods=['GET', 'POST'])#employer login page route
def employer_login():
    if request.method =="GET":
        return render_template("employer_login.html")
    else: 
        # code goes here
        return render_template("employer_home.html")
    
@app.route("/employer_signup" ,methods=['GET', 'POST'])#employer signup page route
def employer_signup():
    if request.method =="GET":
        return render_template("employer_signup.html")
    else: 
        # code goes here
        return render_template("employer_home.html")
    

@app.route("/employer_home" ,methods=['GET', 'POST'])#employer login page route
def employer_home():
    if request.method =="GET":
        return render_template("employer_home.html")
    else: 
        # code goes here
        return render_template("employer_home.html")


#Code goes above here

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")