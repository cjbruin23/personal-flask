import os

from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.environ.get("CONNECTION_STRING")
app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = SECRET_KEY

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class=Base)

with app.app_context():
    db.reflect()

class Family(db.Model):
    __table__ = db.metadata.tables["families"]
@app.route("/", methods=['GET'])
def hello():
    return 'Hello World!'

@app.route('/family', methods=['GET'])
def get_all_families():
    family_data = []
    families = Family.query.all()
    for family in families:
        family_data.append({
            "id": family.id,
            "name": family.name,
            "size": family.size,
            "income": family.income,
        })
    return family_data

if __name__ == '__main__':
        app.run(debug=True, port=5000) # Run Flask on port 5000