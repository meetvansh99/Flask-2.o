from flask import Flask,render_template,request,redirect,url_for,flash
from model import Registration

app=Flask(__name__)
app.secret_key="kk"

@app.route("/",methods=["GET","POST"])
def reg():
    form=Registration()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        flash(f"Thank you {name}! for registration","success")
        return render_template("wel.html",name=name)
    return render_template("index.html",form=form)



app.run(debug=True)


