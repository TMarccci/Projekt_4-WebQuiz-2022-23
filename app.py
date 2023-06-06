from flask import Flask, render_template, request, redirect, url_for, session, flash, Response, jsonify
from flask_squeeze import Squeeze
from dotenv import load_dotenv
import mysql.connector as mysql
from mysql.connector import pooling
import os, uuid, json

load_dotenv()
app = Flask(__name__)
squeeze = Squeeze()
squeeze.init_app(app)

app.config['SECRET_KEY'] = os.getenv('secret')

# Database Settings
dbHost = os.getenv('dbHost')
dbUser = os.getenv('dbUser')
dbPass = os.getenv('dbPass')
dbName = os.getenv('dbName')

cnxpool = mysql.pooling.MySQLConnectionPool(pool_name="mypool", pool_size=30, host=dbHost, user=dbUser, password=dbPass, database=dbName)

# Get user data
def getUserData(userid):
    # Get the user's gender and username
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users WHERE userid = %s", (userid,))
    user = cursor.fetchone()
    cursor.close()
    cnx.close()

    # If found continue else return error
    if user is None:
        flash('Felhasználó nem található az adatbázisban azonosító alapján! Távolítson el minden sütiket és jelentkezzen be újra!')
        return render_template('error.html', title='QuizR - Hiba', logged_in=True)
    
    username = user[3]
    gender = user[8]

    if gender == 0:
        gender = "M"
    else:
        gender = "W"

    return username, gender

import auth
import quiz
import alpage
import profiles
import pagesearch