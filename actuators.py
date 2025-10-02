from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required

actuators = Blueprint("actuators", __name__ , template_folder="templates")

atuadores = {'Servo motor': 0, 'Lâmpada':1}

@actuators.route('/remove_actuators')
@login_required
def remove_actuators():
    return render_template("remove_actuators.html", atuadores=atuadores)

@actuators.route('/del_actuator', methods=['GET','POST'])
@login_required
def del_actuador():
    global atuadores
    if request.method == 'POST':
       atuador = request.form['atuador']
    else:
        atuador = request.args.get('atuador')
    atuadores.pop(atuador)
    return render_template("actuators.html", atuadores=atuadores)

@actuators.route('/list_actuators')
@login_required
def list_actuators():
    global atuadores
    return render_template("actuators.html", atuadores=atuadores)

@actuators.route('/register_actuators')
@login_required
def register_actuators():
    return render_template("register_actuators.html")

@actuators.route('/add_actuators', methods=['GET','POST'])
@login_required
def add_atuators():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
        valor = request.form['valor']
    else:
        atuador = request.args.get('atuador', None)
        valor = request.args.get('valor', None)

    atuadores[atuador] = valor
    return render_template("actuators.html", atuadores=atuadores)

@actuators.route('/actuators')
@login_required
def show_actuators():
    return render_template("actuators.html", atuadores=atuadores)