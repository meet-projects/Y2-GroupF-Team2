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

@app.route("/" ,methods=['GET', 'POST'])
def choice():
    if request.method =="GET":
        return render_template("")
    else: 
        if request.form['answer'] == "employer":
            return render_template('')
        else:
            return render_template("")
    


#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)