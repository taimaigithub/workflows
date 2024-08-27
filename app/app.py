from flask import Flask, jsonify
import mysql.connector
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/users')
def get_users():
    try:
        connection = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="testdb"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(users)
    except Exception as e:
        return str(e)
@app.route('/time')
def time():
    time_now = datetime.now('%Y/%m/%d - %H:%M:%S')
    return jsonify
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
