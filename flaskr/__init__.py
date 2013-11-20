# all the imports
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# create our application
app = Flask(__name__)


#configuration
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db',
    # DATABASE='/tmp/flaskr.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

db = SQLAlchemy(app)

# class DB:
#     def connect_db(self):
#         return sqlite3.connect(app.config['DATABASE'])
#
#     def init_db(self):
#         with closing(self.connect_db()) as db:
#             with app.open_resource('schema.sql', mode='r') as f:
#                 db.cursor().executescript(f.read())
#             db.commit()

import flaskr.views
import flaskr.models

if __name__ == '__main__':
    # making any changes to our schema will
    # necessitate reinitializing the database
    # init_db()
    app.run()