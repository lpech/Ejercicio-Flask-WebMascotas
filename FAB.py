from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

# FAB Form Alta Baja

class FormularioAlta(FlaskForm):
    nombre = StringField('Nombre de la mascota')
    boton = SubmitField('Agregar')

class FormularioBaja(FlaskForm):
    id = IntegerField('Identificador de la mascota')    
    boton = SubmitField('Eliminar')