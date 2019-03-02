# Browser sent request to server, and this is the server file which gives response

from flask import Flask , render_template, url_for , redirect

# Name of the app
app = Flask(__name__)

# route helps to create various end points separated by /
# function needs to be defined under route to get a return value

@app.route("/")
def index():
    # return render_template("/index.html")
    return redirect(url_for("about")) 


@app.route("/about")
def about():
    return render_template("/about.html")
# (Debug = True) we do not have to manually restart server after every change
if __name__ == "__main__":
    app.run(debug = True)
