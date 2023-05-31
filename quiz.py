from app import *
import datetime

def sendQuiz(quizz, username, gender, useridself):
        descerror = "Valami hiba történt. A hiba leírása mellett megjelenik a hiba kódja is. A hiba kódját a fejlesztőknek kell elküldeniük, hogy javítsák a hibát vagy utánajárjanak a problémának."
        description = "Tanuld meg a kártyákat könnyebben. Nézd meg a megoldásokat, ha mégsem sikerülne. Majd próbáld meg ismét. A QuizR segít a tanulásban."

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
        cursor.execute("SELECT * FROM users WHERE userid = %s", (quizz[6],))
        creator = cursor.fetchone()
        cursor.close()
        cnx.close()

        if username and gender and useridself is not None:
            # Handle errors
            if quizcategory is None:
                flash('Hiba történt! 0x007')
                return render_template('error.html', title='QuizR - Hiba történt', logged_in=True, name=username, gender=gender, useridself=useridself, description=descerror)
            if len(quizcontents) == 0:
                flash('Hiba történt! 0x009')
                return render_template('error.html', title='QuizR - Hiba történt', logged_in=True, name=username, gender=gender, useridself=useridself, description=descerror)
            
            return render_template('quizes/learnquiz.html', title='QuizR - ' + quizcategory + ' - ' + quizz[2], logged_in=True, name=username, gender=gender, useridself=useridself, quiz=quizz, quizcategory=quizcategory, quizcontents=quizcontents, quizcreatorid=creator[1], quizcreator=creator[3],description=description)
        else:
            # Handle errors
            if quizcategory is None:
                flash('Hiba történt! 0x008')
                return render_template('error.html', title='QuizR - Hiba történt', logged_in=False, description=descerror)
            if len(quizcontents) == 0:
                flash('Hiba történt! 0x010')
                return render_template('error.html', title='QuizR - Hiba történt', logged_in=False, description=descerror)

            return render_template('quizes/learnquiz.html', title='QuizR - ' + quizcategory + ' - ' + quizz[2], logged_in=False, quiz=quizz, quizcategory=quizcategory, quizcontents=quizcontents, quizcreator=creator[1], description=description)

@app.route('/createquiz')
def createquiz():
    description = "A felhasználók új quiz paklikat hozhatnak létre. A quiz pakli létrehozásához meg kell adni a quiz pakli nevét, kategóriáját és a quiz pakli kártyáit. A quiz pakli létrehozása után a felhasználó átkerül a kész quiz pakli oldalrára."

    # If the session contains the loggedin variable, we can assume the user is logged in.
    if 'loggedin' in session:
        useridself = session['id']

        username, gender = getUserData(useridself)[0], getUserData(useridself)[1]

        # Get categories list
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM quizcategories")
        categories = cursor.fetchall()
        cursor.close()
        cnx.close()

        return render_template('quizes/createquiz.html', title='QuizR - Új Quiz pakli készítése', logged_in=True, name=username, gender=gender, useridself=useridself, categories=categories, description=description)
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
    descerror = "Valami hiba történt. A hiba leírása mellett megjelenik a hiba kódja is. A hiba kódját a fejlesztőknek kell elküldeniük, hogy javítsák a hibát vagy utánajárjanak a problémának."

    # Search quiz in database
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM quizlist WHERE quizid = %s", (quizid,))
    quiz = cursor.fetchone()
    cursor.close()
    cnx.close()

    if 'loggedin' in session:
        useridself = session['id']
        username, gender = getUserData(useridself)[0], getUserData(useridself)[1]

    # If the quiz doesnt exist, return error
    if quiz is None:
        # If the user is logged in, return the error page with the logged in template
        if 'loggedin' in session:
            flash('A kért quiz nem található! 0x002')
            return render_template('error.html', title='QuizR - Quiz nem található', logged_in=True, name=username, gender=gender, useridself=useridself, description=descerror)
        else:
            flash('A kért quiz nem található! 0x003')
            return render_template('error.html', title='QuizR - Quiz nem található', logged_in=False, description=descerror)
    else:
        # Logged in
        if 'loggedin' in session:
            # If quiz is private
            if quiz[8] == 0:
                if quiz[6] != useridself:
                    flash('A kért quiz nem nyilvános! 0x004')
                    return render_template('error.html', title='QuizR - Quiz nem nyilvános', logged_in=True, name=username, gender=gender, useridself=useridself, description=descerror)
                else:
                    flash('A quized mások számára nem megtekinthető! 0x006')
                    return sendQuiz(quiz, username, gender, useridself)
            # If quiz is public
            else:
                return sendQuiz(quiz, username, gender, useridself)
        # Not logged in
        else:
            # If quiz is private
            if quiz[8] == 0:
                flash('A kért quiz nem nyilvános! 0x005')
                return render_template('error.html', title='QuizR - Quiz nem nyilvános', logged_in=False, description=descerror)
            # If quiz is public
            else:
                return sendQuiz(quiz, None, None, None)
            
@app.route('/editquiz/<quizid>')
def editquiz(quizid):
    descerror = "Valami hiba történt. A hiba leírása mellett megjelenik a hiba kódja is. A hiba kódját a fejlesztőknek kell elküldeniük, hogy javítsák a hibát vagy utánajárjanak a problémának."
    description = "Ez az oldal a quiz pakli szerkesztésére szolgál. A quiz pakli módosítását, a létrehozáshoz hasonlóan kell csinálni. A quiz pakli szerkesztése után a felhasználó átkerül a kész quiz pakli oldalára."
    
    if 'loggedin' in session:
        useridself = session['id']
        username, gender = getUserData(useridself)[0], getUserData(useridself)[1]
        
        # Check if the user is the owner of the quiz
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM quizlist WHERE quizid = %s AND ownerid = %s", (quizid, useridself))
        quiz = cursor.fetchone()
        cursor.close()
        cnx.close()
        
        if quiz is None:
            flash('Quiz nem található vagy nincs jogod a quiz szereksztéséhez! 0x026')
            return render_template('error.html', title='QuizR - Hiba', logged_in=True, name=username, gender=gender, useridself=useridself, description=descerror)
        else:
            # Get the quiz contents
            cnx = cnxpool.get_connection()
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM quizcontents WHERE quizid = %s", (quizid,))
            quizcontents = cursor.fetchall()
            cursor.close()
            cnx.close()
            
            # Get the category list
            cnx = cnxpool.get_connection()
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM quizcategories")
            categories = cursor.fetchall()
            cursor.close()
            cnx.close()
            
            return render_template('quizes/editquiz.html', title=f"QuizR - { quiz[2] } szerkesztés", logged_in=True, gender=gender, useridself=useridself, name=username, quiz=quiz, quizcontents=quizcontents, categories=categories, description=description)
            
    else:
        flash('Quiz szerkesztéséhez jelentkezz be vagy regisztrálj! 0x025')
        return render_template('error.html', title='QuizR - Hiba', logged_in=False, description=descerror)

@app.route('/editquiz/<quizid>', methods=['POST'])
def editquizpost(quizid):
    if 'loggedin' not in session:
        return Response(status=403)
    else:
        # If the form doesnt have the required fields, return error
        if 'quizname' not in request.form or 'category' not in request.form or 'ispublic' not in request.form:
            return Response(status=400)
        else:
            # Check if the user is the owner of the quiz
            cnx = cnxpool.get_connection()
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM quizlist WHERE quizid = %s AND ownerid = %s", (quizid, session['id']))
            quiz = cursor.fetchone()
            cursor.close()
            cnx.close()
            
            if quiz:
                # Get the form data
                quizname = request.form['quizname']
                category = request.form['category']
                ispublic = request.form['ispublic']
                if 'appearinsearch' in request.form:
                    appearinsearch = request.form['appearinsearch']
                else:
                    appearinsearch = 0
                seqcount = request.form['seqcount']
                now = datetime.datetime.now()
                
                # Update the quiz
                cnx = cnxpool.get_connection()
                cursor = cnx.cursor()
                cursor.execute("UPDATE quizlist SET quizname = %s, quizcateg = %s, ispublic = %s, appearonsearch = %s, lastedit = %s, seqcount = %s WHERE quizid = %s", (quizname, category, ispublic, appearinsearch, now, seqcount, quizid))
                cnx.commit()
                cursor.close()
                cnx.close()
                
                # Delete the old quiz contents
                cnx = cnxpool.get_connection()
                cursor = cnx.cursor()
                cursor.execute("DELETE FROM quizcontents WHERE quizid = %s", (quizid,))
                cnx.commit()
                cursor.close()
                cnx.close()
                
                # Insert the new quiz contents
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
                    
                return redirect(url_for('quiz', quizid=quizid))
            else:
                return Response(status=403)