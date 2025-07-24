import os

import psycopg2
from flask_cors import CORS
from flask import Flask
from dotenv import load_dotenv

from database.select import Select
from models.community import Community

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
    selectBuilder = Select("*", "community")

    cur.execute(selectBuilder.__str__())
    communities = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]

    communityObjects = []
    for i in range(len(communities)):
        community = communities[i]
        data_obj = {}
        for x in range(len(colnames)):
            col_name = colnames[x]
            data_obj[col_name] = community[x]

        communityObjects.append(data_obj)

    cur.close()
    conn.close()
    return communityObjects

@app.route('/community', methods=['GET'])
def get_all_families():
    return 'Hello'

if __name__ == '__main__':
        app.run(debug=True, port=5000) # Run Flask on port 5000