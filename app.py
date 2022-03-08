from flask import Flask, render_template, send_file


app = Flask(__name__)


# Pages 

@app.route("/")
def home():
    return render_template("RippleRockWebsite.html")

@app.route("/projects")
def projects():
    return render_template("Projects/Projects.html")

@app.route("/programs")
def programs():
    return render_template("Programs/Programs.html")

@app.route("/events")
def events():
    return render_template("Events/Events.html")

@app.route("/resourses")
def resourses():
    return render_template("Resourses/Resourses.html")

@app.route("/partners")
def partners():
    return render_template("Partners/Partners.html")

@app.route("/supportus")
def supportus():
    return render_template("Get Involved/Get Involved.html")

# Gifs

@app.route('/bird')
def bird():   
    return send_file('bird.gif', mimetype='image/gif')

@app.route('/vortex')
def vortex():   
    return send_file('vortex.gif', mimetype='image/gif')



if __name__ == "__main__":
    app.run(debug=True)
    