from app import *

# Get categ foreach
def getCategForeach(quizzes):
    categnames = []

    # Get category name for each quiz
    for i in quizzes:
        # Get category name for each quiz
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT categname FROM quizcategories WHERE id = %s", (i[3],))
        category = cursor.fetchone()
        cursor.close()
        cnx.close()

        categnames.append(category[0])

    return categnames

# Get user's quizzes
def getUserQuizzes(userid, self):
    # If self is true then get all quizzes else get only the public ones
    if self:
        # Get the user's quizzes
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM quizlist WHERE ownerid = %s", (userid,))
        quizzes = cursor.fetchall()
        cursor.close()
        cnx.close()
    else:
        # Get the user's quizzes except the private ones
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM quizlist WHERE ownerid = %s AND ispublic = 1", (userid,))
        quizzes = cursor.fetchall()
        cursor.close()
        cnx.close()

    return quizzes

@app.route('/profile/<userid>')
def profile(userid):
    description = "A felhasználók profiljának megtekintése. A profil oldalon a felhasználók megtekinthetik a saját adataikat, a saját quiz paklijaikat, a saját kedvenc quiz paklijaikat, a saját kedvenc kategóriáikat és a saját kedvenc felhasználóikat vagy másokét."
    descerror = "Valami hiba történt. A hiba leírása mellett megjelenik a hiba kódja is. A hiba kódját a fejlesztőknek kell elküldeniük, hogy javítsák a hibát vagy utánajárjanak a problémának."

    # Get the profile
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users WHERE userid = %s", (userid,))
    profile = cursor.fetchone()
    cursor.close()
    cnx.close()

    # If the profile exists
    if profile:
        if 'loggedin' in session:
            userid = session['id']
            username, gender = getUserData(userid)[0], getUserData(userid)[1]

            # If the profile is the user's profile
            if userid == profile[1]:
                quizzes = getUserQuizzes(userid, True)
                quizzescount = len(quizzes)

                if quizzes:
                    categnames = getCategForeach(quizzes)

                    return render_template('profile/profile.html', title=f"QuizR - {profile[3]}", logged_in=True, name=username, gender=gender, description=description, self=True, profile=profile, quizzes=quizzes, categnames=categnames, quizzescount=quizzescount)
                else:
                    return render_template('profile/profile.html', title=f"QuizR - {profile[3]}", logged_in=True, name=username, gender=gender, description=description, self=True, profile=profile, quizzes=False, categnames=False)    
            else:
                quizzes = getUserQuizzes(userid, False)
                quizzescount = len(quizzes)

                if quizzes:
                    categnames = getCategForeach(quizzes)

                    return render_template('profile/profile.html', title=f"QuizR - {profile[3]}", logged_in=True, name=username, gender=gender, description=description, profile=profile, quizzes=quizzes, categnames=categnames, quizzescount=quizzescount)
                else:
                    return render_template('profile/profile.html', title=f"QuizR - {profile[3]}", logged_in=True, name=username, gender=gender, description=description, profile=profile, quizzes=False, categnames=False)
        else:
            quizzes = getUserQuizzes(userid, False)
            quizzescount = len(quizzes)

            if quizzes:
                categnames = getCategForeach(quizzes)

                return render_template('profile/profile.html', title=f"QuizR - {profile[3]}", logged_in=False, description=description, profile=profile, quizzes=quizzes, categnames=categnames, quizzescount=quizzescount)
            else:
                return render_template('profile/profile.html', title=f"QuizR - {profile[3]}", logged_in=False, description=description, profile=profile, quizzes=False, categnames=False)
    else:
        if 'loggedin' in session:
            flash('Nem találhatü a felhasználó profilja. 0x014')
            return render_template('error.html', title='QuizR - Quiz nem található', logged_in=True, name=username, gender=gender, description=descerror)
        else:
            flash('Nem találhatü a felhasználó profilja. 0x015')
            return render_template('error.html', title='QuizR - Quiz nem található', logged_in=False, description=descerror)