from flask import Flask,render_template, request

app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about")
def he():
    return render_template("about.html")

app.run(debug=True)