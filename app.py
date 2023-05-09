from flask import Flask
from dotenv import load_dotenv
import mysql.connector.pooling, os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('secret')

# Database Settings
dbHost = os.getenv('dbHost')
dbUser = os.getenv('dbUser')
dbPass = os.getenv('dbPass')
dbName = os.getenv('dbName')

cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool", pool_size=10, host=dbHost, user=dbUser, password=dbPass, database=dbName)

import auth
import quiz