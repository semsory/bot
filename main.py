from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)


@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    content = request.form.get("content")
    if content:
        db.session.add(Task(content=content))
        db.session.commit()
    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")


@app.route("/bogdan")
def bogdan_page():
    return render_template("bogdan.html")


@app.route("/bio")
def mihail_page():
    return render_template("bio.html")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

