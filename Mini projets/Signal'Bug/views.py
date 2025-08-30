from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from os import path
from id import generate_id
from data import add_report, get_reports, remove_report

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./static/uploads"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/report", methods=['POST'])
def report():
    data = request.form
    if 'name' not in data or 'email' not in data or 'version' not in data or 'description' not in data:
        return render_template("bad_request.html")

    screenshots = []
    if 'screenshots' in request.files:
        files = request.files.getlist("screenshots")
        for file in files:
            _, extension = path.splitext(file.filename)
            if ',' in extension:
                extension = extension.replace(",", "")
            filename = f"{generate_id()}{extension}";
            screenshots.append(filename)
            file.save(path.join(app.config['UPLOAD_FOLDER'], filename))

    add_report(data["name"], data["email"], data["description"], data["version"], screenshots)
    return render_template("result.html")

@app.route("/reports", methods=["GET", "POST"])
def reports():
    if request.method == "POST":
        data = request.form
        if 'id' in data:
            remove_report(data["id"])
        else:
            render_template("bad_request.html")
    data = get_reports()
    return render_template("reports.html", data=data)

app.run(threaded=False, use_reloader=False, debug=True)
