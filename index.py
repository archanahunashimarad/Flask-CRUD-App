from flask import Flask, request, url_for, render_template,redirect,session
import sql1 as db
app = Flask(__name__)
app.secret_key="archana"


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == "admin":
            session['admin'] = True
            return render_template("comment.html",customers=db.get_feedbacks())
        else:
            return redirect(url_for('index',msg="Wrong credentials"))
        

@app.route("/add_feedback",methods=['POST'])
def add_feedback():
	name = request.form['name']
	email = request.form['email']
	
	status = db.add_feedback(name,email)
	return redirect(url_for('addUserView',msg=status))

@app.route("/feedback", methods=['GET','POST'])
def addUserView():
    if request.method == 'GET':
        return render_template("feedback.html",customers=db.get_feedbacks())

@app.route("/logout/") 
def logout():
    session.clear()
    return redirect(url_for('index',msg="You have successfully logged out"))

if __name__ == "__main__":
    app.run(debug=True)