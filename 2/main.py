from flask import Flask,request,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        valid_user={
            "Meet":"9898",
            "Ankur":"9898"
        }

        if username in valid_user and password==valid_user[username]:
            return render_template("wel.html",name=username)
        else:
            return "Invalid credantial"
    return render_template("index.html")
    

app.run(debug=True)
