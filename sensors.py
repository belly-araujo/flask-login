from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required

sensors = Blueprint("sensores", __name__ , template_folder="templates")

sensores = {'Umidade':22, 'temperatura':23, 'luminosidade':1034}

@sensors.route('/remove_sensors')
@login_required
def remove_sensors():
    return render_template("remove_sensors.html", sensores=sensores)

@sensors.route('/del_sensor', methods=['GET','POST'])
@login_required
def del_sensor():
    global sensores
    if request.method == 'POST':
       sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor')
    sensores.pop(sensor)
    return render_template("sensors.html", sensores=sensores)

@sensors.route('/sensors')
@login_required
def show_sensors():
    return render_template("sensors.html", sensores=sensores)


@sensors.route('/list_sensors')
@login_required
def list_sensors():
    global sensores
    return render_template("sensors.html", sensores=sensores)

@sensors.route('/add_sensors', methods=['GET','POST'])
@login_required
def add_sensors():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
        valor = request.form['valor'] 
    else:
        sensor = request.args.get('sensor', None)
        valor = request.args.get('valor', None)
    sensores[sensor] = valor
    return render_template("sensors.html", sensores=sensores)

@sensors.route('/register_sensors')
@login_required
def register_sensors():
    return render_template("register_sensors.html")