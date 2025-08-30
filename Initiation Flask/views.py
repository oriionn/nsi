from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    date = datetime.now()
    h = date.hour
    m = date.minute
    s = date.second
    return render_template("index.html", heure=h, minute=m, seconde=s)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/convert')
def convert():
    return render_template("convert.html")

@app.route('/form/post')
def form_post():
    return render_template("form/post/index.html")

@app.route("/form/post/resultat", methods=['POST'])
def form_post_result():
    result = request.form
    n = result['nom']
    p = result['prenom']
    return render_template("form/post/resultat.html", nom=n, prenom=p)

@app.route('/form/get')
def form_get():
    return render_template("form/get/index.html")

@app.route("/form/get/resultat", methods=['GET'])
def form_get_result():
    result = request.args
    n = result['nom']
    p = result['prenom']
    return render_template("form/get/resultat.html", nom=n, prenom=p)

@app.route("/birthday")
def birthday():
    return render_template("birthday/index.html")

@app.route("/birthday/result", methods=['POST'])
def birthday_result():
    result = request.form
    date = result["date"];

    now = datetime.now()
    next_year = now.year
    d = datetime.strptime(date, "%Y-%m-%d")
    if now.month >= d.month and now.day > d.day:
        next_year = now.year + 1
    d = datetime.strptime(date.replace(str(d.year), str(next_year)), "%Y-%m-%d")

    return render_template("birthday/result.html", temps_restant=str(d - now).split(",")[0].replace("days", "jours"))



app.run(threaded=False, use_reloader=False, debug=True)
