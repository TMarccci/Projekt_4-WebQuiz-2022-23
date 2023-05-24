from app import *

@app.route('/search', methods=['GET'])
def search():
    description = "A keresés funkció segítségével a felhasználók megkereshetik a quiz paklikat. A kereséshez meg kell adni a keresendő szöveget és a keresés kategóriáját. A keresés lehet a quiz pakli neve vagy a quiz pakli kategóriája. A keresés eredménye a keresési feltételeknek megfelelő quiz paklik listája."
    
    # Get categories from database
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM quizcategories")
    categories = cursor.fetchall()
    cursor.close()
    cnx.close()

    if 'loggedin' in session:
        useridself = session['id']
        username, gender = getUserData(useridself)[0], getUserData(useridself)[1]

        return render_template('search/search.html', title='QuizR - Keresés', logged_in=True, name=username, gender=gender, useridself=useridself, description=description, categories=categories)
    else:
        return render_template('search/search.html', title='QuizR - Keresés', logged_in=False, description=description, categories=categories)
    
@app.route('/searchapi', methods=['POST'])
def search_post():
    # If there is no search text or category filter
    if request.form.get('searchtext') == "" and request.form.get('categoryfilter') == "-1":
        # Get quizzes from database
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM quizlist WHERE ispublic = 1 AND appearonsearch = 1")
        quizzes = cursor.fetchall()
        cursor.close()
        cnx.close()

    # If there is search text and category filter
    else:
        if request.form.get('searchtext') != "" and request.form.get('categoryfilter') != "-1":
            # Get quizzes from database
            cnx = cnxpool.get_connection()
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM quizlist WHERE ispublic = 1 AND appearonsearch = 1 AND (quizname LIKE %s OR quizcateg = %s)", (f"%{request.form.get('searchtext')}%", int(request.form.get('categoryfilter'))))
            quizzes = cursor.fetchall()
            cursor.close()
            cnx.close()

        else:
            # If there is only search text
            if request.form.get('searchtext') != "":
                # Get quizzes from database
                cnx = cnxpool.get_connection()
                cursor = cnx.cursor()
                cursor.execute("SELECT * FROM quizlist WHERE ispublic = 1 AND appearonsearch = 1 AND quizname LIKE %s", (f"%{request.form.get('searchtext')}%",))
                quizzes = cursor.fetchall()
                cursor.close()
                cnx.close()

            # If there is only category filter
            else:
                # Get quizzes from database
                cnx = cnxpool.get_connection()
                cursor = cnx.cursor()
                cursor.execute("SELECT * FROM quizlist WHERE ispublic = 1 AND appearonsearch = 1 AND quizcateg = %s", (int(request.form.get('categoryfilter')),))
                quizzes = cursor.fetchall()
                cursor.close()
                cnx.close()

    # Get categories from database
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM quizcategories")
    categories = cursor.fetchall()
    cursor.close()
    cnx.close()

    # Convert the categori id to category name


    for quiz in range(len(quizzes)):
        for category in categories:
            if quizzes[quiz][3] == category[0]:
                quizzes[quiz] = list(quizzes[quiz])
                quizzes[quiz][3] = category[1]
                quizzes[quiz] = tuple(quizzes[quiz])

    # Return the quizzes as json
    return jsonify(quizzes)