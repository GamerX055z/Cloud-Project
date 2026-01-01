from flask import Flask, render_template
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home page accessed")
    return render_template("index.html")

@app.route("/about")
def about():
    app.logger.info("About page accessed")
    return render_template("about.html")

if __name__ == "__main__":
    app.run()

