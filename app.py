from flask import Flask, render_template, send_from_directory

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

@app.route("/images/<path:path>")
def static_dir(path):
    return send_from_directory("images", path)

if __name__ == "__main__":
    app.run(debug=True)
    