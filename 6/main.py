from flask import Flask,render_template,request,redirect,flash,url_for

app=Flask(__name__)
app.secret_key="hi"
@app.route("/",methods=["GET","POST"])
def form():
    if request.method=="POST":
        name=request.form.get("name")
        if not name :
            flash("Name cannot be empty")
            return redirect(url_for("form"))
        flash(f"thank you {name} for your feedback")
        return render_template("t.html",name=name)
    return render_template("index.html")
             

    



app.run(debug=True)

