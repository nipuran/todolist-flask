from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.models import Todo
from app.extensions import db


from . import dashboard_bp

@dashboard_bp.route("/")
@login_required
def dashboard():
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", todos=todos, username=current_user.username)
    

@dashboard_bp.route("/add", methods=["POST"])
@login_required
def add():
    name = request.form['name']
    new_todo = Todo(name=name, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("dashboard_bp.dashboard"))


@dashboard_bp.route("/edit/<int:todo_id>", methods=["GET", "POST"])
@login_required
def edit(todo_id):
    if request.method == "POST":
        name = request.form['name']
        todo = Todo.query.get(todo_id)
        todo.name = name
        db.session.commit()
        return redirect(url_for("dashboard_bp.dashboard"))
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template("edit.html", todos=todos, todo_id=todo_id, username=current_user.username)


@dashboard_bp.route("/delete/<int:todo_id>")
@login_required
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("dashboard_bp.dashboard"))


@dashboard_bp.route("/check/<int:todo_id>", methods=["POST"])
@login_required
def check(todo_id):
    todo = Todo.query.get(todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for("dashboard_bp.dashboard"))
