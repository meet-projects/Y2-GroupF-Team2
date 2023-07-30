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
storage = firebase.storage()
#Code goes below here


@app.route("/" ,methods=['GET', 'POST'])#choice between company and alum route
def choice():
    if request.method =="GET":

        login_session['user'] = "None"
        return render_template("choice.html")
    else: 
        if request.form['answer'] == "employer":
            return redirect(url_for("employer_login"))
        else:
            return redirect(url_for("alum_login"))
        


#-----------------------
# alum routes starts here 
# ----------------------



@app.route("/alum_login" ,methods=['GET', 'POST'])#alum login page route
def alum_login():
    if request.method =="GET":
        login_session['user'] = "None"
        return render_template("alum_login.html")
    else: 
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            print("succses")
            return redirect(url_for("alum_profile"))
        except:
            #login fail code goes here
            print("fail")
            return render_template("alum_login.html")
        


@app.route("/alum_signup" ,methods=['GET', 'POST'])#alum signup page route
def alum_signup():
    if request.method =="GET":
        login_session['user'] = "None"
        return render_template("alum_signup.html")
    else:
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email,password)
            UID = login_session['user']['localId']
            user = {"email": email, "name":name}
            db.child("Alums").child(UID).set(user)
            return redirect(url_for("alum_home"))
        except:
            return redirect(url_for("alum_signup"))

@app.route("/alum_home" ,methods=['GET', 'POST'])#alum home page route
def alum_home():
    if request.method =="GET":
        company_list = db.child("Companies").get().val()


        return render_template("alum_home.html", company_list = company_list)
    else: 
        # code goes here
        return render_template("employer_home.html")

@app.route("/alum_profile" ,methods=['GET', 'POST'])#alum profile page route
def alum_profile():
    if request.method =="GET":
        CV = db.child("Users").child(login_session['user']['localId']).child("CV").get().val()
        degree = db.child("Users").child(login_session['user']['localId']).child("degree").get().val()
        name = db.child("Users").child(login_session['user']['localId']).child("name").get().val()
        user = db.child("Alums").child(login_session['user']["localId"]).get().val()
        applications = db.child("Alums").child(login_session['user']["localId"]).child("Applications").get().val()
        print(user["name"])
        return render_template("alum_profile.html", CV=CV, degree=degree,name=name, user=user, applications=applications)
    else: 
        CV = db.child("Users").child(login_session['user']['localId']).child("CV").get().val()
        degree = db.child("Users").child(login_session['user']['localId']).child("degree").get().val()
        name = db.child("Users").child(login_session['user']['localId']).child("name").get().val()
        # db.child("Alums").child(login_session['user']["localId"]).child("CV").set(request.form['CV'])
        user = db.child("Alums").child(login_session['user']["localId"]).get().val()
        applications = db.child("Alums").child(login_session['user']["localId"]).child("Applications").get().val()

        cv_file = request.files['CV']
        UID = login_session['user']['localId']
        upload_cv(cv_file,UID, name)

        return render_template("alum_profile.html", CV=CV, degree=degree,name=name, user=user, applications=applications)




def upload_cv(cv_file, UID, name):
    name = "oded"
    path = f"cv_uploads/{UID}/{name}_cv.docx"

    storage.child(path).put(cv_file)

    # --------------------
# company routes starts here
# -------------------



@app.route("/employer_login" ,methods=['GET', 'POST'])#employer login page route
def employer_login():
    if request.method =="GET":
        login_session['user'] = "None"
        return render_template("employer_login.html")
    else: 
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            print("success")
            return render_template("employer_home.html")
        except:
            return render_template("employer_login.html")
    
@app.route("/employer_signup" ,methods=['GET', 'POST'])#employer signup page route
def employer_signup():
    if request.method =="GET":
        login_session['user'] = "None"
        return render_template("employer_signup.html")
    else: 
        email = request.form['email']
        password = request.form['password']
        name  = request.form['name']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            company = {"email":email, "name":name}
            db.child("Companies").child(UID).set(company)
            return render_template("employer_home.html")
        except:
            return render_template("employer_signup.html")
            
    

@app.route("/employer_home" ,methods=['GET', 'POST'])#employer login page route
def employer_home():
    if request.method =="GET":
        return render_template("employer_home.html")
    else: 
        # code goes here
        return render_template("employer_home.html")


#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)