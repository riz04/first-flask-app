from flask import Flask , render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/home")
def index():
    return render_template("/home.html")

@app.route("/css")
def css():
    return render_template("/css.html")
 

@app.route("/about")
def about():
    return render_template("/about.html")

@app.route("/contact")
def contact():
    return render_template("/contact.html")



if __name__ == "__main__":
    app.run(debug = True,port = 5002)  