from flask import Flask , render_template
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)

# CONFIGURE DB

db = yaml.load(open("db.yaml"))
app.config["MYSQL_HOST"] = db["mysql_host"]
app.config["MYSQL_USER"] = db["mysql_user"]
app.config["MYSQL_PASSWORD"] = db["mysql_password"]
app.config["MYSQL_DB"] = db["mysql_db"]

mysql = MySQL(app)
 
@app.route("/home")
def index():
    cur = mysql.connection.cursor()
    # cur.execute("INSERT INTO user (user_name) VALUES (%s),(%s)", ["jony","shina"])
    # mysql.connection.commit()
    #To fetch values from database

    result_value = cur.execute("SELECT * FROM user")
    if result_value > 0:
        users = cur.fetchall()

        print(users[0])
        # return str(users[0])
        return users[0][0]
    return render_template("/home.html")


@app.route("/about")
def about():
    return render_template("/about.html")

@app.route("/contact")
def contact():
    return render_template("/contact.html")



if __name__ == "__main__":
    app.run(debug = True)