from flask import Flask, render_template
from repository.models import db

mysql = 'mysql://root@localhost/crm'
sqlite = 'sqlite:///crm_flask.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

from repository import routes