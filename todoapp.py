from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.secret_key = 'saad4346'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    user = db.relationship('Users', backref='todos')

@app.route("/", methods=["POST", 'GET'])
def hello():
    if request.method == "POST":
        user = request.form['nm']
        password = request.form['password']
        
        founduser = Users.query.filter_by(username=user).first()
        if founduser:
            if check_password_hash(founduser.password, password):
                session['username'] = founduser.username
                return redirect(url_for('welcome'))
            else:
                return "Incorrect password. Please try again."

        else:
            hashed_password = generate_password_hash(password)
            usr = Users(username=user, password=hashed_password)
            db.session.add(usr)
            db.session.commit()
            session['username'] = usr.username
            return redirect(url_for('welcome'))
        
    return render_template('base.html')

@app.route("/todopage")
def welcome():
    if 'username' in session:
        user = Users.query.filter_by(username=session['username']).first()
        todos = Todo.query.filter_by(user_id=user.id).all()
        return render_template("index.html", todos=todos)
    return redirect(url_for('hello'))

@app.route("/add_todo", methods=["POST"])
def add_todo():
    if 'username' in session:
        user = Users.query.filter_by(username=session['username']).first()
        todo_content = request.form['todo_content']
        new_todo = Todo(user_id=user.id, content=todo_content)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('welcome'))

@app.route("/toggle_todo/<int:todo_id>")
def toggle_todo(todo_id):
    if 'username' in session:
        todo = Todo.query.get(todo_id)
        if todo and todo.user_id == Users.query.filter_by(username=session['username']).first().id:
            todo.completed = not todo.completed
            db.session.commit()
    return redirect(url_for('welcome'))

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('hello'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


    
if __name__=="__main__":
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)
