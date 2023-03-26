from flask import Flask, jsonify
from flask_cors import CORS
import os 
from model.database import SQLiteDatabase

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def server():
    # create an instance of the SQLiteDatabase class
    db = SQLiteDatabase('australian_operating_mines.db')
    mine_sites = db.fetch_mine_sites()
    db.close_connection()

    marks = [
        {'latitude': latitude, 'longitude': longitude} for latitude, longitude in mine_sites
    ]
        
    return jsonify({'marks': marks})

@app.route('/config')
def get_config():
    google_map_api = os.environ.get('GOOGLE_MAP_API')
    return jsonify({'google_map_api': google_map_api})
    
if __name__ == '__main__': 
    app.run(debug=True, port=5000)


