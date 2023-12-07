FROM python
#FROM python:3.8-alpine3.17

LABEL maintainer="pythonFlask_APIrest"
LABEL version="2.0"

ENV FLASK_ENV=development

# Instalar dependencias
RUN pip install flask
RUN pip install flask-wtf
RUN pip install Flask-SQLAlchemy
RUN pip install flask_migrate
# Crear una carpeta para la aplicación
RUN mkdir /app
# Establecer la carpeta de trabajo
WORKDIR /app
# Copiar la aplicación a la imagen
COPY . /app
# Exponer el puerto 5000
EXPOSE 5000
# Ejecutar la aplicación
CMD flask run --host=0.0.0.0 --port=5000 --reload
