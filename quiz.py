from flask import session, redirect, request, url_for, render_template, Response, jsonify, flash
from app import app, cnxpool
import uuid

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

def sendQuiz(quizz, username, gender):
        # Get the quiz contents catetories
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT categname FROM quizcategories WHERE id = %s", (quizz[3],))
        quizcategory = cursor.fetchone()[0]
        cursor.close()
        cnx.close()

        # Get the quiz contents
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM quizcontents WHERE quizid = %s", (quizz[1],))
        quizcontents = cursor.fetchall()
        cursor.close()
        cnx.close()

        # Remove the first two elements from the list
        for i in range(len(quizcontents)):
            quizcontents[i] = quizcontents[i][2:]

        # Get who created the quiz
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT username FROM users WHERE userid = %s", (quizz[6],))
        quizcreator = cursor.fetchone()[0]
        cursor.close()
        cnx.close()

        if username and gender is not None:
            # Handle errors
            if quizcategory is None:
                flash('Hiba történt! 0x007')
                return render_template('error.html', title='QuizR - Hiba történt', logged_in=True, name=username, gender=gender)
            if len(quizcontents) == 0:
                flash('Hiba történt! 0x009')
                return render_template('error.html', title='QuizR - Hiba történt', logged_in=True, name=username, gender=gender)
            
            return render_template('learnquiz.html', title='QuizR - ' + quizz[2], logged_in=True, name=username, gender=gender, quiz=quizz, quizcategory=quizcategory, quizcontents=quizcontents, quizcreator=quizcreator)
        else:
            # Handle errors
            if quizcategory is None:
                flash('Hiba történt! 0x008')
                return render_template('error.html', title='QuizR - Hiba történt', logged_in=False)
            if len(quizcontents) == 0:
                flash('Hiba történt! 0x010')
                return render_template('error.html', title='QuizR - Hiba történt', logged_in=False)

            return render_template('learnquiz.html', title='QuizR - ' + quizz[2], logged_in=False, quiz=quizz, quizcategory=quizcategory, quizcontents=quizcontents, quizcreator=quizcreator)

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

        # Get categories list
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM quizcategories")
        categories = cursor.fetchall()
        cursor.close()
        cnx.close()

        return render_template('createquiz.html', title='QuizR - Új Quiz pakli készítése', logged_in=True, name=username, gender=gender, categories=categories)
    else:
        flash('Quiz pakli készítéséhez jelentkezz be vagy regisztrálj! 0x013')
        return redirect(url_for('login'))
    
@app.route('/createquiz', methods=['POST'])
def createquiz_post():
    if 'loggedin' not in session:
        return Response(status=403)
    else:
        # If the form doesnt have the required fields, return error
        if 'quizname' not in request.form or 'category' not in request.form or 'ispublic' not in request.form:
            return Response(status=400)
        else:
            # Get the form data
            quizname = request.form['quizname']
            category = request.form['category']
            ispublic = request.form['ispublic']
            if 'appearinsearch' in request.form:
                appearinsearch = request.form['appearinsearch']
            else:
                appearinsearch = 0
            ownerid = session['id']
            quizid = str(uuid.uuid4())
            seqcount = request.form['seqcount']

            # Append the quiz to the database
            cnx = cnxpool.get_connection()
            cursor = cnx.cursor()
            cursor.execute("INSERT INTO quizlist (quizid, quizname, quizcateg, creationdate, lastedit, ownerid, seqcount, ispublic, appearonsearch) VALUES (%s, %s, %s, NOW(), NOW(), %s, %s, %s, %s)", (quizid, quizname, category, ownerid, seqcount, ispublic, appearinsearch))

            # Commit the changes
            cnx.commit()
            cursor.close()
            cnx.close()

            # Append the cards to quizcontents
            for i in range(int(seqcount)):
                seqnum = i
                sideonetype = request.form['card' + str(i) + 'side1type']
                sideonecontent = request.form['card' + str(i) + 'side1text']
                sidetwotype = request.form['card' + str(i) + 'side2type']
                sidetwocontent = request.form['card' + str(i) + 'side2text']
                
                cnx = cnxpool.get_connection()
                cursor = cnx.cursor()
                cursor.execute("INSERT INTO quizcontents (quizid, seqnum, sideonetype, sidetwotype, sideone, sidetwo) VALUES (%s, %s, %s, %s, %s, %s)", (quizid, seqnum, sideonetype, sidetwotype, sideonecontent, sidetwocontent))

                # Commit the changes
                cnx.commit()
                cursor.close()
                cnx.close()

            # Redirect to the quiz page
            return redirect(url_for('quiz', quizid=quizid))

@app.route('/quiz/<quizid>')
def quiz(quizid):
    # Search quiz in database
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM quizlist WHERE quizid = %s", (quizid,))
    quiz = cursor.fetchone()
    cursor.close()
    cnx.close()

    if 'loggedin' in session:
        userid = session['id']
        username, gender = getUserData(userid)[0], getUserData(userid)[1]

    # If the quiz doesnt exist, return error
    if quiz is None:
        # If the user is logged in, return the error page with the logged in template
        if 'loggedin' in session:
            flash('A kért quiz nem található! 0x002')
            return render_template('error.html', title='QuizR - Quiz nem található', logged_in=True, name=username, gender=gender)
        else:
            flash('A kért quiz nem található! 0x003')
            return render_template('error.html', title='QuizR - Quiz nem található', logged_in=False)
    else:
        # If quiz is private and the user is not logged in, return error
        if quiz[8] == 0:
            if 'loggedin' in session:
                # If the owner is not the user, return error
                if quiz[6] != userid:
                    flash('A kért quiz nem nyilvános! 0x004')
                    return render_template('error.html', title='QuizR - Quiz nem nyilvános', logged_in=True, name=username, gender=gender)
                else:
                    flash('A quized mások számára nem megtekinthető! 0x006')
                    return sendQuiz(quiz, username, gender)
            else:
                flash('A kért quiz nem nyilvános! 0x005')
                return render_template('error.html', title='QuizR - Quiz nem nyilvános', logged_in=False)
        else:
            return sendQuiz(quiz, None, None)