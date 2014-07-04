from flask import Flask, render_template, redirect, request, flash, session
import model
import jinja2

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index():
    user_list = model.dbsession.query(model.User).all()
    return render_template("user_list.html", users = user_list)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/sign_up", methods=["POST"])
def process_signup():
    email = request.form.get('email')
    password = request.form.get('password')
    age = request.form.get('age')
    zipcode = request.form.get('zipcode')
    #print email
    user_object = model.User(email=email,
                            password=password,
                            age=age, 
                            zipcode=zipcode)
    #call DB commit function
    user_object.add_user()
    #print user_object.id
    #store userid in browser session and redirect user to logged in page
    session['userid'] = user_object.id
    return redirect("/movie_ratings")

@app.route("/movie_ratings")
def movie_ratings():
    ratings_object = model.dbsession.query(model.Ratings).filter_by(user_id=session['userid']).all() 
    return render_template("movie_ratings.html", ratings_object=ratings_object)

@app.route("/login", methods=["POST"])
def process_login():
    email = request.form.get('email')
    print email
    #print model.session
    row = model.dbsession.query(model.User).filter_by(email=email).one()
    print row
    session['userid'] = row.id
    if row:
        flash("Log in successful")
    else:
        flash("Sorry we could not find your record")
        return render_template("login.html")
    #return render_template("movie_ratings.html", ratings_object=ratings_object)
    return redirect("/movie_ratings")

if __name__ == "__main__":
    app.run(debug = True)