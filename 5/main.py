from flask import Flask,render_template, request

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def feedback():
    if request.method=="POST":
        name=request.form.get("name")
        message=request.form.get("message")
        return render_template("t.html",name=name,message=message)
    return render_template("index.html")
    
app.run(debug=True)