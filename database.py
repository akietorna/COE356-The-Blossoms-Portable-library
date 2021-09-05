from flask import Flask
from flask_mysqldb import MySQLdb
import MySQLdb.cursors


# app=Flask(__name__)


#app.config['SECRET_KEY'] = 'hispresence123@'

def connection():
    connect = MySQLdb.connect(host="theblossoms.mysql.pythonanywhere-services.com",
                              user="theblossoms",
                              passwd="hispresence123@",
                              db="theblossoms$library")
# innitializing the cursor
    curs = connect.cursor()

    return curs, connect
