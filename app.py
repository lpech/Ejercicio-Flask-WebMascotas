import os
from FAB import FormularioAlta, FormularioBaja
from flask import Flask, url_for, redirect, render_template, request, session, flash, g, abort, jsonify, make_response, Response, send_file, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

directorio = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = '!92&y6#X9%a45=7*+@8j:w'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio, 'mascotas_vistas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Modelo de la base
bd = SQLAlchemy(app)
app.app_context().push()
Migrate(app, bd)

class Mascota(bd.Model):
    __tablename__ = 'mascotas'
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.Text(50))

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        texto = f'Mascota: nombre {self.nombre} - id {self.id}'
        return texto

@app.route('/')
def inicio():
    return render_template('Vista_Inicio.html')

@app.route('/lista')
def lista():
    mascota = Mascota.query.all()
    return render_template('VistaLista.html', mascota=mascota)

@app.route('/alta', methods=['GET', 'POST'])
def alta():
    formulario = FormularioAlta()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        mascota = Mascota(nombre)
        bd.session.add(mascota)
        bd.session.commit()
        flash('Mascota agregada con éxito')
        return redirect(url_for('lista'))
    return render_template('Vista_Alta.html', formulario=formulario)

@app.route('/baja', methods=['GET', 'POST'])
def eliminar():
    formulario = FormularioBaja()
    if formulario.validate_on_submit():
        id = formulario.id.data
        mascota = Mascota.query.get(id)
        bd.session.delete(mascota)
        bd.session.commit()
        flash('Mascota eliminada con éxito')
        return redirect(url_for('lista'))
    return render_template('Vista_Baja.html', formulario=formulario)

@app.errorhandler(404)
def page_not_found(error):
    return '<h1>[E] - Error 404, página no encontrada. </h1>'

if __name__ == '__main__':
    app.run(debug=True)