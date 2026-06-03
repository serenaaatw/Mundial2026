from flask import Flask
from models.db import db
from config.config import DATABASE_CONNECTION_URI
#from routes.routes import routes_blueprint 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app.register_blueprint()

db.init_app(app)

with app.app_context():
    #from models.  import
    #db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)