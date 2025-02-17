from flask import Flask, render_template, request, url_for, redirect, flash, session, jsonify
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

#from models import db, Usuario, Visita, MeGusta 

app = Flask(__name__)
app.secret_key = '@Admin123'

# Configuración de la base de datos MySQL usando la variable de entorno MYSQL_URL
#app .config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:uatqmVilKDcIqIAblPMDtLPmxoRowowr@mysql-05hd.railway.internal:3306/railway"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Cambia esto si usas otro servidor SMTP
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sustentoyrefugio2025@gmail.com'  # Tu dirección de correo
app.config['MAIL_PASSWORD'] = 'aiof ccau scxy jgrv'  # Tu contraseña de correo
app.config['MAIL_DEFAULT_SENDER'] = 'sustentoyrefugio2025@gmail.com'  # Remitente por defecto

mail = Mail(app)

db = SQLAlchemy()
db.init_app(app)
with app.app_context():
    db.create_all()

# Ruta principal
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Crear el mensaje
        msg = Message(subject, recipients=['marcoo.espinozaa@gmail.com'])  # Cambia esto por tu correo
        msg.body = f"Nombre: {name}\nEmail: {email}\n\nMensaje:\n{message}"
        
        try:
            # Enviar el mensaje
            mail.send(msg)
            flash('Mensaje enviado con éxito!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            flash(f'Error al enviar el mensaje: {str(e)}', 'error')
            # Volver a renderizar la plantilla con los datos del formulario
            return render_template('contact.html', name=name, email=email, subject=subject, message=message)

    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/portfolio_item')
def portfolio_item():
    return render_template('portfolio-item.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog_post')
def blog_post():
    return render_template('blog-post.html')

@app.route('/ui_elements')
def ui_elements():
    return render_template('ui_elements.html')


if __name__ == '__main__':
    app.run(debug=True)
