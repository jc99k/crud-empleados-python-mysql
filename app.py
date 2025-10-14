from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
app.config['MYSQL_PORT'] = 3306

print(f"Connecting to MySQL host: {os.environ.get('MYSQL_HOST')}")

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employees")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', employees = data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        birthday = request.form['birthday']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employees (name, email, phone, birthday) VALUES (%s, %s, %s, %s)", (name, email, phone, birthday))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employees WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        birthday = request.form['birthday']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE employees SET name=%s, email=%s, phone=%s, birthday=%s
        WHERE id=%s
        """, (name, email, phone, birthday, id_data))
        flash("Data Updated Successfully")
        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)