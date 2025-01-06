from flask import Flask, render_template
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

app.run(threaded=False, use_reloader=False, debug=True)