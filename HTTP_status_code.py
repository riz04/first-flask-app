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
def home():
    cur = mysql.connection.cursor()
    if cur.execute("INSERT INTO user (user_name) VALUES (%s)" , ["Ben"]):
        mysql.connection.commit()
        return "success",201

    return render_template("/home.html")

@app.errorhandler(404)
def page_not_found(e):
    return 'This page was not found'



if __name__ == "__main__":
    app.run(debug = True,port = 5004)