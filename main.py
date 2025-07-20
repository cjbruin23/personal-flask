import os

import psycopg2
from flask_cors import CORS
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.environ.get("CONNECTION_STRING")
app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(SECRET_KEY)
    return conn

@app.route("/", methods=['GET'])
def hello():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM community;')
    communities = cur.fetchall()
    cur.close()
    conn.close()
    return 'Hello World!'

@app.route('/community', methods=['GET'])
def get_all_families():
    return 'Hello'

if __name__ == '__main__':
        app.run(debug=True, port=5000) # Run Flask on port 5000