from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process",methods=['POST'])
def process():
    return render_template("process.html",name = request.form["name"])
    name = request.form["name"]
    print name
    return redirect(url_for("/"))

app.run(debug=True)
