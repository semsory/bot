from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    print(f"Имя: {name}")
    return f"Привет, {name}!"

if __name__ == "__main__":
    app.run(debug=True)