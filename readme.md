## Flask Stuff
### Notes from 6/28

#### Today's tasks:
+ Use flask-migrate to manage db state
+ manage flash messages with session
+ hash + salt with flask bcrypt


#### Setup instructions
+ mkvirtualenv flask_migrate 
+ structure: root
  + templates
    + base.html
    + index.html
    + new.html
  + app.py
+ pip install flask flask_sqlalchemy psycopg2 flask_migrate
+ pip freeze > requirements.txt
+ createdb learn-flask-migrate


#### Making the application

```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/learn-flask-migrate'


if __name__ == '__main__':
  app.run(debug=True, port=3000)

```
Make a model next. At this point, the password is still insecure, but we will refactor later. 

```
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.Text, nullable=False)
  password = db.Column(db.Text, nullable=False)

  def __init__(self, username, password):
    self.username = username
    self.password = password

```

Create a new file, `manage.py`
<br>
In manage.py, insert the following:

```
from app import app, db

from flask_script import Manager # this class handles command line script initialization

from flask_migrate import Migrate, MigrateCommand
# Migrate - handles migration initialization
# MigrateCommand - specifies what command line task runs our migrations

# Initialize flask_migrate
  # Need to specify the application and db you are using
migrate = Migrate(app, db)

# Initialize flask_script
manager = Manager(app)


# Specify what string gets attached to the MigrateCommand
manager.add_command('db', MigrateCommand)




if __name__ == '__main__':
  manager.run()
```

Now, `python manage.py db` in the terminal will bring up a list arguments available to flask_migrate

#### Steps

1 Run `python manage.py db init` to create a migrations folder with alembic setup files
2 `python manage.py db migrate`
3 `python manage.py db upgrade`


You can then upgrade or downgrade as necessary.

<hr>
## Notes
+ flask_migrate is an extension of something called "alembic"
+ flask_script allows you to run shell scripts out of flask