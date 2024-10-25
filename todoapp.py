from flask import Flask,render_template,redirect,url_for,request,session
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.secret_key = 'saad4346'
db=SQLAlchemy(app)

class Users(db.Model):
    id=db.Column("id",db.Integer,primary_key=True)
    username=db.Column(db.String(100))
    password=db.Column(db.String(100))
    






@app.route("/",methods=["POST",'GET'])
def hello():
    if request.method=="POST":
        user=request.form['nm']
        
        
        founduser=Users.query.filter_by(username=user).first()
        if founduser:
            session['username']=founduser.username

        else:
         usr=Users(username=user, password="")
         db.session.add(usr)
         db.session.commit()
        return redirect(url_for('welcome'))
        
    else: 
      return render_template('base.html',content="username")
@app.route("/todopage")

def welcome():
    return render_template("index.html")


    
if __name__=="__main__":
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)