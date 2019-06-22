from flask import Flask, render_template, request
# from firebase import firebase
import configurations
from pyrebase import pyrebase

app = Flask(__name__)
email = "null"

firebsevar = pyrebase.initialize_app(config=configurations.config)
db = firebsevar.database()

@app.route('/')
def Base_qstn_paper_set():
    return render_template('first.html')



@app.route('/foo', methods=['POST', 'GET'])
def foo():
    if request.method == 'POST':
        first = request.form['first']
        second = request.form['second']
        third = request.form['third']
        fourth = request.form['fourth']
        fifth = request.form['fifth']
        sixth = request.form['sixth']
        seventh = request.form['seventh']
        eighth = request.form['eighth']
        ninth = request.form['ninth']
        tenth = request.form['tenth']

        email = request.form['emailID']

        ans = {"a1": first, "a2": second, "a3": third,"a4": fourth,"a5":fifth ,"a6":sixth,"a7":seventh ,"a8":eighth ,"a9":ninth,"a10":tenth,"email": email}

        result = db.child("/answers").push(ans)
    return render_template('first.html')


