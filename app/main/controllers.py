from flask import  Flask, Blueprint ,render_template, redirect, url_for, session, request, flash
from app import db
from app.main.models import Todo
from sqlalchemy import desc

main = Blueprint('main',__name__)

@main.route('/')
def index():
    todos = Todo.query.order_by(desc(Todo.id)).all()
    return render_template('main/index.html', todos=todos)


@main.route('/add', methods =['POST'])
def add():
    title = request.form.get('title')
    todo = Todo(title=title, completed=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/change/<int:id>')
def change(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo:
        todo.completed = not todo.completed
        db.session.commit()
    else:
        flash('error','danger')
    return redirect(url_for('main.index'))

@main.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
    else:
        flash('error','danger')
    return redirect(url_for('main.index'))


