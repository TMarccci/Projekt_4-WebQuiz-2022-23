from flask import session, redirect, request, url_for, render_template, Response, jsonify, flash
from app import app, cnxpool

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

@app.route('/')
def index():
    # If the session contains the loggedin variable, we can assume the user is logged in.
    if 'loggedin' in session:
        userid = session['id']
        username, gender = getUserData(userid)[0], getUserData(userid)[1]

        return render_template('home.html', title='QuizR - Főoldal', logged_in=True, home=True, name=username, gender=gender)
    else:
        return render_template('home.html', title='QuizR - Főoldal', logged_in=False, home=True)
    
@app.route('/policy')
def policy():
    # If the session contains the loggedin variable, we can assume the user is logged in.
    if 'loggedin' in session:
        userid = session['id']
        username, gender = getUserData(userid)[0], getUserData(userid)[1]

        return render_template('policy.html', title='QuizR - Adatkezelési tájékoztató', logged_in=True, name=username, gender=gender)
    else:
        return render_template('policy.html', title='QuizR - Adatkezelési tájékoztató', logged_in=False)
    
@app.route('/howtomakequiz')
def howtomakequiz():
    # If the session contains the loggedin variable, we can assume the user is logged in.
    if 'loggedin' in session:
        userid = session['id']
        username, gender = getUserData(userid)[0], getUserData(userid)[1]

        return render_template('howtomakequiz.html', title='QuizR - Quiz pakli készítés útmutató', logged_in=True, name=username, gender=gender)
    else:
        return render_template('howtomakequiz.html', title='QuizR - Quiz pakli készítés útmutató', logged_in=False)

@app.route('/createquiz')
def createquiz():
    # If the session contains the loggedin variable, we can assume the user is logged in.
    if 'loggedin' in session:
        userid = session['id']

        username, gender = getUserData(userid)[0], getUserData(userid)[1]

        return render_template('createquiz.html', title='QuizR - Új Quiz pakli készítése', logged_in=True, name=username, gender=gender)
    else:
        flash('Quiz pakli készítéséhez be kell jelentkezned!')
        return redirect(url_for('login'))