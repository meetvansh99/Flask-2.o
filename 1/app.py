from flask import Flask,request,session,render_template,Response,redirect,url_for

app=Flask(__name__)
app.secret_key="super"

# home page 
@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        if username=="Meet" and password=="9898":
            session["user"]=username
            return redirect(url_for("welcome"))
            # return render_template("wel.html")
        else:
            return Response("invalid credantials,try again!" , mimetype="text/plain")
        
    return render_template("login.html")

@app.route("/welcome")
def welcome():
    if "user" in session:
        return render_template("wel.html")

@app.route("/logout")
def logout():

    session.pop("user",None)

    return redirect(url_for("login"))
    
    


app.run(debug=True)