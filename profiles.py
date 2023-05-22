from app import *
from werkzeug.security import generate_password_hash, check_password_hash

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

# Send profile page
@app.route('/profile/<userid>')
def profile(userid):
    description = "Itt megtekinthető a saját illetve más felhasználók profiljai. A saját profil esetén adatmódosításra is van lehetőség. Más profilnál pedig a nyilvános quiz paklikat lehet megtekinteni."
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
            useridself = session['id']
            username, gender = getUserData(useridself)[0], getUserData(useridself)[1]

            # If the profile is the user's profile
            if useridself == profile[1]:
                quizzes = getUserQuizzes(userid, True)
                quizzescount = len(quizzes)

                if quizzes:
                    categnames = getCategForeach(quizzes)

                    return render_template('profile/profile.html', title=f"QuizR - {profile[3]}", logged_in=True, name=username, gender=gender, useridself=useridself, description=description, selfuser=True, profile=profile, quizzes=quizzes, categnames=categnames, quizzescount=quizzescount)
                else:
                    return render_template('profile/profile.html', title=f"QuizR - {profile[3]}", logged_in=True, name=username, gender=gender, useridself=useridself, description=description, selfuser=True, profile=profile, quizzes=False, categnames=False, quizzescount=quizzescount)    
            else:
                quizzes = getUserQuizzes(userid, False)
                quizzescount = len(quizzes)

                if quizzes:
                    categnames = getCategForeach(quizzes)

                    return render_template('profile/profile.html', title=f"QuizR - {profile[3]}", logged_in=True, name=username, gender=gender, useridself=useridself, description=description, profile=profile, quizzes=quizzes, categnames=categnames, quizzescount=quizzescount)
                else:
                    return render_template('profile/profile.html', title=f"QuizR - {profile[3]}", logged_in=True, name=username, gender=gender, useridself=useridself, description=description, profile=profile, quizzes=False, categnames=False, quizzescount=quizzescount)
        else:
            quizzes = getUserQuizzes(userid, False)
            quizzescount = len(quizzes)

            if quizzes:
                categnames = getCategForeach(quizzes)

                return render_template('profile/profile.html', title=f"QuizR - {profile[3]}", logged_in=False, description=description, profile=profile, quizzes=quizzes, categnames=categnames, quizzescount=quizzescount)
            else:
                return render_template('profile/profile.html', title=f"QuizR - {profile[3]}", logged_in=False, description=description, profile=profile, quizzes=False, categnames=False, quizzescount=quizzescount)
    else:
        if 'loggedin' in session:
            useridself = session['id']
            username, gender = getUserData(useridself)[0], getUserData(useridself)[1]

            flash('Nem található a felhasználó. 0x014')
            return render_template('error.html', title='QuizR - Quiz nem található', logged_in=True, name=username, gender=gender, useridself=useridself, description=descerror)
        else:
            flash('Nem található a felhasználó. 0x015')
            return render_template('error.html', title='QuizR - Quiz nem található', logged_in=False, description=descerror)
        
# API for user data change
@app.route('/editprofile', methods=['POST'])
def editprofile():
    # Parse data from form
    useridself = session['id']
    username = request.form['username']
    email = request.form['email']

    # Get the users data
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users WHERE userid = %s", (useridself,))
    user = cursor.fetchone()
    cursor.close()
    cnx.close()

    # If the username is not the same as the old one change it
    if username != user[3]:
        # Update the username
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("UPDATE users SET username = %s WHERE userid = %s", (username, useridself))
        cnx.commit()
        cursor.close()
        cnx.close()

    # If the email is not the same as the old one change it
    if email != user[2]:
        # Check if the email is already in use
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        emailcheck = cursor.fetchone()
        cursor.close()
        cnx.close()

        # If the email is not in use
        if not emailcheck:
            # Update the email
            cnx = cnxpool.get_connection()
            cursor = cnx.cursor()
            cursor.execute("UPDATE users SET email = %s WHERE userid = %s", (email, useridself))
            cnx.commit()
            cursor.close()
            cnx.close()
        else:
            flash('null')
            flash('A kívánt email cím már használatban van! Nem történt változtatás. 0x016')
            flash('null')
            return redirect(url_for('profile', userid=useridself))
        
    # If nothing changed return nothing changed
    if username == user[3] and email == user[2]:
        flash('null')
        flash('Nem változtattál meg semmit! 0x017')
        flash('null')
        return redirect(url_for('profile', userid=useridself))
    
    # If something changed return page
    flash('Sikeresen megváltoztattad az adataid!')
    flash('null')
    flash('null')
    return redirect(url_for('profile', userid=useridself))

# API for user password change
@app.route('/updatepass', methods=['POST'])
def updatepass():
    # Parse data from form
    useridself = session['id']
    oldpass = request.form['passold']
    newpass = request.form['passnew1']
    newpass2 = request.form['passnew2']

    # Get the users data
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users WHERE userid = %s", (useridself,))
    user = cursor.fetchone()
    cursor.close()
    cnx.close()

    # If the old password is correct
    if check_password_hash(user[4], oldpass):
        # If the new passwords match
        if newpass == newpass2:
            # Update the password
            cnx = cnxpool.get_connection()
            cursor = cnx.cursor()
            cursor.execute("UPDATE users SET password = %s WHERE userid = %s", (generate_password_hash(newpass, method='sha256'), useridself))
            cnx.commit()
            cursor.close()
            cnx.close()

            flash('Sikeresen megváltoztattad a jelszavad!')
            flash('null')
            flash('null')
            return redirect(url_for('profile', userid=useridself))
        else:
            flash('null')
            flash('null')
            flash('A két új jelszó nem egyezik meg! 0x018')
            return redirect(url_for('profile', userid=useridself))
    else:
        flash('null')
        flash('null')
        flash('A régi jelszó nem egyezik meg a megadottal! Nem történt változtatás. 0x019')
        return redirect(url_for('profile', userid=useridself))