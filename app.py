from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("RippleRockWebsite.html")

@app.route("/projects")
def projects():
    return render_template("Projects/Projects.html")

if __name__ == "__main__":
    app.run(debug=True)
    