from flask import Flask, render_template, request
from markupsafe import escape


app = Flask(__name__, template_folder='templates')

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/upload_file", methods=['POST'])
def upload_file():
    allowed_extensions = ['.xls', '.csv', 'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'text/csv']
    file = request.files['file']

    file_ext = file.content_type
    is_valid_ext = False
    for extension in allowed_extensions:
        if file_ext == extension:
            is_valid_ext = True


    if is_valid_ext == True:
        return "has subido un archivo >w<"
    else:
        return render_template('index.html')
