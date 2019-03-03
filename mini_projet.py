from flask import Flask , render_template , request
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap

import yaml


app = Flask(__name__)
Bootstrap(app)

# CONFIGURE DB

db = yaml.load(open("dbms.yaml"))
app.config["MYSQL_HOST"] = db["mysql_host"]
app.config["MYSQL_USER"] = db["mysql_user"]
app.config["MYSQL_PASSWORD"] = db["mysql_password"]
app.config["MYSQL_DB"] = db["mysql_db"]
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)
 
@app.route("/", methods = ["GET","POST"])
def project():
    if request.method == 'POST':
        form = request.form
        name = form["name"]
        age = form["age"]
        cur = mysql.connection.cursor()
        cur.execute ("INSERT INTO employees (name, age) VALUES (%s , %s)", (name,age))
        mysql.connection.commit()
    return render_template("/project.html")

@app.route("/employees")
def employees():
    cur = mysql.connection.cursor()
    result_value = cur.execute ("SELECT * FROM employees")
    if result_value > 0:
        employees = cur.fetchall()
        return render_template ("employees.html" , employees = employees)



if __name__ == "__main__":
    app.run(debug = True, port = 5001)