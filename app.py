from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contactospersonas'
mysql = MySQL(app)

#settings
app.secret_key = 'mysecretkey'



@app.route('/')
def Index(): 
 cursor = mysql.connection.cursor()
 cursor.execute("SELECT * FROM contactos")
 data = cursor.fetchall()
 return render_template('index.html', contacts = data)

@app.route('/agregarContacto', methods=['POST'])
def agregarContacto():
 if request.method == 'POST':
   nombre = request.form['nombre']
   apellido = request.form['apellido']
   telefono = request.form['telefono']
   correo = request.form['correo']
   cursor = mysql.connection.cursor()
   cursor.execute("INSERT INTO contactos (nombre, apellido, telefono, correo) VALUES (%s, %s, %s, %s)", (nombre, apellido, telefono, correo))
   mysql.connection.commit()
   flash('Contacto agregado exitosamente')
   return redirect(url_for('Index'))
 

@app.route('/EditarContactos/<id>')
def get_contact(id):
 cursor = mysql.connection.cursor()
 cursor.execute("SELECT * FROM contactos WHERE id = %s", (id))
 data = cursor.fetchall()
 return render_template('editar.html', contact = data[0])

@app.route("/update/<id>", methods = ["POST"])
def update_contact(id):
 if request.method == 'POST':
  nombre = request.form['nombre']
  apellido = request.form['apellido']
  telefono = request.form['telefono']
  correo = request.form['correo']
  cursor = mysql.connection.cursor()
  cursor.execute("""
                 UPDATE contactos
                 SET nombre = %s,
                 apellido = %s,
                 telefono = %s,
                 correo = %s
                 WHERE id = %s
                 """, (nombre,apellido,telefono,correo, id))
  mysql.connection.commit()
  flash('Contacto editato correctamente')
  return redirect(url_for('Index'))

@app.route('/eliminarContacto/<string:id>')
def eliminarContacto(id):
 cursor = mysql.connection.cursor()
 cursor.execute("DELETE FROM contactos WHERE id = {0}".format(id))
 mysql.connection.commit()
 flash('Contacto eliminado exitosamente')
 return redirect(url_for('Index'))

if __name__ == '__main__':
 app.run(port = 3000, debug=True)