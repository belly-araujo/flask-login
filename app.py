from flask import Flask, render_template, redirect, url_for, request
from login import login, login_manager, login_required, logout_user, login_user, users, User, current_user
from sensors import sensors
from actuators import actuators

app= Flask(__name__)
app.secret_key = 'chave_secreta_123'

app.register_blueprint(sensors, url_prefix='/')
app.register_blueprint(login, url_prefix='/')
app.register_blueprint(actuators, url_prefix='/')

login_manager.init_app(app)
login_manager.login_view = "login.login_form" 

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return render_template("login.html")

@app.route('/home')
@login_required
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)