from flask import session, redirect, request, url_for, render_template, Response, jsonify, flash
from app import app, cnxpool

@app.route('/')
def index():
    # If the session contains the loggedin variable, we can assume the user is logged in.
    if 'loggedin' in session:
        userid = session['id']

        # Get the user's gender and username
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM users WHERE userid = %s", (userid,))
        user = cursor.fetchone()
        cursor.close()
        cnx.close()

        username = user[3]
        gender = user[8]

        if gender == 0:
            gender = "M"
        else:
            gender = "W"

        return render_template('home.html', title='QuizPro - Főoldal', logged_in=True, name=username, gender=gender)
    else:
        return render_template('home.html', title='QuizPro - Főoldal', logged_in=False)