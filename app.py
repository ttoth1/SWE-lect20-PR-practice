from flask import Flask

app = Flask(__name__)

@app.route("/")
def function():
    text = 'random'
    return "<b>ERROR<b>"

app.run()