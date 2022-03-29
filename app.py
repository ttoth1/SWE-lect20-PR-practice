from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<b>ERROR<b>"

app.run()