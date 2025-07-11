from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def profile():
    return render_template("index.html",
                            name="Meet",is_topper=True,
                           subjects=["maths","sci","che"])

app.run(debug=True)
