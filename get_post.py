from flask import Flask , render_template , request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/check",methods = ["GET","POST"])
def check():
    if request.method == "POST":
        return request.form ["password"]
        # return "Successfully registered"


    return render_template("/check.html")


if __name__ == "__main__":
    app.run(debug = True,port = 5003)  