from flask import Flask, render_template
# Installing with pip e.g. .conda/bin/pip install Flask

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
