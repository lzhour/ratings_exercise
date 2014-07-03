from flask import Flask, render_template, redirect, request, flash
import model
import jinja2

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index():
    user_list = model.session.query(model.User).all()
    return render_template("user_list.html", users = user_list)

@app.route("/login")
def login():
    return render_template("login.html")
    
@app.route("/login", methods=["POST"])
def process_login():
    email = request.form.get('email')
    print email
    #print model.session
    row = model.session.query(model.User).filter_by(email=email).all()
    print row

    if row:
        flash("Log in successful")
    else:
        flash("Sorry we could not find your record")

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug = True)