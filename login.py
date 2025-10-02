from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

login = Blueprint("login", __name__ , template_folder="templates")

users = {
    "user1":"1234",
    "user2":"12345"
    }

class User(UserMixin):
    def __init__(self, id):
        self.id = id

login_manager = LoginManager()

@login.route('/login', methods=['GET', 'POST'])
def login_form():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if user in users and users[user] == password:
            user_obj = User(user)
            login_user(user_obj)
            return redirect(url_for("home"))
        else:
            return '<h1>Credenciais inválidas</h1>'
    return render_template("login.html")

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None
    
# Logout
@login.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login.login_form"))

@login.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if user in users and users[user] == password:
            user_obj = User(user)
            login_user(user_obj)
            return redirect(url_for("home"))  # rota do app.py
        else:
            return '<h1>Credenciais inválidas!</h1>'
    return render_template('login.html')
    
@login.route('/list_users')
@login_required
def list_users():
    global users
    return render_template("users.html", devices=users)

@login.route('/register_user')
@login_required
def register_user():
    return render_template("register_user.html")

@login.route('/add_user', methods=['GET','POST'])
@login_required
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    users[user] = password
    return render_template("users.html", devices=users)

@login.route('/remove_user')
@login_required
def remove_user():
    return render_template("remove_user.html", devices=users)

@login.route('/del_user', methods=['GET','POST'])
@login_required
def del_user():
    global users
    if request.method == 'POST':
       user = request.form['user']
    else:
        user = request.args.get('user', None)
    users.pop(user)
    return render_template("users.html", devices=users)
