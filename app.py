from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'  # Dirección del servidor de la base de datos
app.config['MYSQL_USER'] = 'root'       # Usuario de la base de datos
app.config['MYSQL_PASSWORD'] = ''       # Contraseña del usuario de la base de datos
app.config['MYSQL_DB'] = 'contactospersonas'  # Nombre de la base de datos
mysql = MySQL(app)  # Inicializa la extensión Flask-MySQLdb con la configuración de la app

# Configuración de la clave secreta para la aplicación Flask
app.secret_key = 'mysecretkey'

# Ruta principal de la aplicación, método GET por defecto
@app.route('/')
def Index(): 
    cursor = mysql.connection.cursor()  # Crear un cursor para interactuar con la base de datos
    cursor.execute("SELECT * FROM contactos")  # Ejecutar una consulta SQL para obtener todos los contactos
    data = cursor.fetchall()  # Obtener todos los resultados de la consulta
    return render_template('index.html', contacts=data)  # Renderizar la plantilla index.html con los datos obtenidos

# Ruta para agregar un nuevo contacto, método POST
@app.route('/agregarContacto', methods=['POST'])
def agregarContacto():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo = request.form['correo']
        
        # Crear un cursor para interactuar con la base de datos
        cursor = mysql.connection.cursor()
        # Ejecutar una consulta SQL para insertar el nuevo contacto
        cursor.execute("INSERT INTO contactos (nombre, apellido, telefono, correo) VALUES (%s, %s, %s, %s)", 
                       (nombre, apellido, telefono, correo))
        mysql.connection.commit()  # Confirmar los cambios en la base de datos
        flash('Contacto agregado exitosamente')  # Mostrar un mensaje flash
        return redirect(url_for('Index'))  # Redirigir a la ruta principal

# Ruta para obtener los detalles de un contacto para editarlo
@app.route('/EditarContactos/<id>')
def get_contact(id):
    cursor = mysql.connection.cursor()  # Crear un cursor para interactuar con la base de datos
    cursor.execute("SELECT * FROM contactos WHERE id = %s", (id,))  # Ejecutar una consulta SQL para obtener un contacto por ID
    data = cursor.fetchall()  # Obtener el resultado de la consulta
    return render_template('editar.html', contact=data[0])  # Renderizar la plantilla editar.html con los datos obtenidos

# Ruta para actualizar los detalles de un contacto, método POST
@app.route("/update/<id>", methods=["POST"])
def update_contact(id):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo = request.form['correo']
        
        # Crear un cursor para interactuar con la base de datos
        cursor = mysql.connection.cursor()
        # Ejecutar una consulta SQL para actualizar el contacto
        cursor.execute("""
                       UPDATE contactos
                       SET nombre = %s,
                           apellido = %s,
                           telefono = %s,
                           correo = %s
                       WHERE id = %s
                       """, (nombre, apellido, telefono, correo, id))
        mysql.connection.commit()  # Confirmar los cambios en la base de datos
        flash('Contacto editado correctamente')  # Mostrar un mensaje flash
        return redirect(url_for('Index'))  # Redirigir a la ruta principal

# Ruta para eliminar un contacto
@app.route('/eliminarContacto/<string:id>')
def eliminarContacto(id):
    cursor = mysql.connection.cursor()  # Crear un cursor para interactuar con la base de datos
    cursor.execute("DELETE FROM contactos WHERE id = {0}".format(id))  # Ejecutar una consulta SQL para eliminar un contacto por ID
    mysql.connection.commit()  # Confirmar los cambios en la base de datos
    flash('Contacto eliminado exitosamente')  # Mostrar un mensaje flash
    return redirect(url_for('Index'))  # Redirigir a la ruta principal

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(port=3000, debug=True)  # Ejecutar la aplicación en el puerto 3000 con el modo de depuración activado
