import os, datetime
from flask import Flask, request, redirect, render_template, session
from lib.database_connection import get_flask_database_connection
from lib.post_repository import PostRepository
from lib.post import Post
from lib.user_repository import UserRepository
from lib.user import User

# Create a new Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"

# == Your Routes Here ==

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

#-------------
@app.route('/home', methods=['GET'])
def get_posts():
    connection = get_flask_database_connection(app)
    post_repository = PostRepository(connection)
    posts = post_repository.all()
    user_repository = UserRepository(connection)
    logged_in_as = "a guest"
    if 'user_id' in session:
        logged_in_as = user_repository.find_by_id(session['user_id']).username
    else:
        pass
    usernames = []
    for post in posts:
        user = user_repository.get_user_with_post_id(post.user_id)
        usernames.append(user.username)
    return render_template("home.html", posts=posts, usernames=usernames,
                        logged_in_as = logged_in_as)

@app.route('/home', methods=['POST'])
def create_post():
    connection = get_flask_database_connection(app)
    post_repository = PostRepository(connection)
    content = request.form['content']
    # TODO: add real user_id of the logged in user
    posted_time_list = str(datetime.datetime.now()).split(".")
    posted_time = "".join(posted_time_list[0])
    if 'user_id' in session:
        new_post = Post(None, posted_time, content, session['user_id'])
    else:
        new_post = Post(None, posted_time, content, 1)
    post_repository.create(new_post)
    return redirect(f"/home")

@app.route('/signup', methods = ['GET'])
def get_signup():
    return render_template("signup.html")

@app.route('/signup', methods=['POST'])
def sign_up_user():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    user_repository = UserRepository(connection)
    user = User(None, name, email, username, password)
    # if not user.is_valid():
    #     errors = user.generate_errors()
    #     return render_template("new_album.html", errors=errors)
    user_repository.create(user)
    return redirect(f"/home")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    password = request.form['password']
    user_repository = UserRepository(connection)
    if user_repository.check_password(email, password):
        user = user_repository.find_by_email(email)
        session['user_id'] = user.id
        return redirect(f"/home")
    else:
        return redirect(f"/home")
# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
