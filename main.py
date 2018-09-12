from flask import Flask ,render_template, redirect, url_for, session, request, flash
from todo import app, db, Todo

@app.route('/')
def index():
    todos = Todo.query.order_by('id desc').all()
    return render_template('index.html', todos=todos)


@app.route('/add', methods =['POST'])
def add():
    title = request.form.get('title')
    todo = Todo(title=title, completed=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/change/<int:id>')
def change(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo:
        todo.completed = not todo.completed
        db.session.commit()
    else:
        flash('error','danger')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)