from models import *

import mysql.connector, time, os
from mysql.connector import errorcode
from flask import Flask, request, jsonify
server = Flask(__name__)

def db_connect():
    config = {
        'user':'HHNAPP',
        'password':'password',
        'host':'172.28.238.10',
        'database':'HHNAPP'
    }
    conn = mysql.connector.connect(**config)
    c = conn.cursor()
    return c, conn

def db_disconnect(c, conn):
    c.close()
    conn.close()

def create_tables():
    try:
        c, conn = db_connect()
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                c.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        db_disconnect(c, conn)
        return False
    except Exception as e:
        return True





@server.route('/', methods = ['GET'])
def main():
    try:
        c, conn = db_connect()
        db_disconnect(c, conn)
        return 'Connected!!'
    except Exception as e:
        return str(e)

@server.route('/api/accounts', methods = ['POST'])
def accounts():    
    add_user = ("INSERT INTO _users (device_id) VALUES (%s)")

    data = request.get_json()
    data_user = (data['device_id'],)

    try:
        c, conn = db_connect()
        c.execute(add_user, data_user)

        conn.commit()
        db_disconnect(c, conn)
        return "device ID added!!"
    except Exception as e:
        return str(e)
        
if os.environ.get("WERKZEUG_RUN_MAIN") == None:
    print("connecting to DB...")
    while create_tables():
        time.sleep(1)

if __name__ == "__main__":
    server.run(host='0.0.0.0')