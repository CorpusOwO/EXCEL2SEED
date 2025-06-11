from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__, template_folder='templates')

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')