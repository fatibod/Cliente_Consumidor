from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cliente_consumidor'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"


# routes
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM signo') 
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts = data)

@app.route('/add_sign', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        pregunta1 = request.form['pregunta1']
        pregunta2 = request.form['pregunta2']
        pregunta3 = request.form['pregunta3']
        pregunta4 = request.form['pregunta4']
        pregunta5 = request.form['pregunta5']
        pregunta6 = request.form['pregunta6']
        pregunta7 = request.form['pregunta7']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO signo (nombre, edad, pregunta1, pregunta2, pregunta3,pregunta4,pregunta5,pregunta6,pregunta7) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (nombre, edad, pregunta1, pregunta2, pregunta3,pregunta4,pregunta5,pregunta6,pregunta7))
        mysql.connection.commit()
        flash('Se envio la informacion correctamente, Gracias!!')
        return redirect(url_for('Index'))
    


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)