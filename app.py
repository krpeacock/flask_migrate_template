from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/learn-flask-migrate'

class User(db.Model):
  
  __tablename__='users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.Text, nullable = False)
  password =  db.Column(db.Text, nullable = False)

  def __init__(self, username, password):
    self.username = username
    self.password = password



if __name__ == '__main__':
  app.run(debug=True, port=3000)
