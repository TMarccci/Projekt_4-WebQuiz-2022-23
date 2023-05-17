from app import *

@app.route('/')
def index():
    description = "A QuizR egy webes alkalmazás, amely lehetővé teszi a felhasználók számára, hogy saját kvíz paklikat készítsenek, és azokat megosszák másokkal. A QuizR egyben lehetőséget biztosít a felhasználók számára, hogy mások által készített kvíz paklikat tanuljanak, és teszteljék tudásukat."

    # If the session contains the loggedin variable, we can assume the user is logged in.
    if 'loggedin' in session:
        userid = session['id']
        username, gender = getUserData(userid)[0], getUserData(userid)[1]

        return render_template('home.html', title='QuizR - Főoldal', logged_in=True, home=True, name=username, gender=gender, description=description)
    else:
        return render_template('home.html', title='QuizR - Főoldal', logged_in=False, home=True, description=description)
    
@app.route('/policy')
def policy():
    description = "Az adatkezelési tájékoztatóban leírtakat a felhasználóknak el kell fogadniuk a regisztrációhoz. Az adatkezelési tájékoztatóban leírtakat a felhasználók bármikor elolvashatják."

    # If the session contains the loggedin variable, we can assume the user is logged in.
    if 'loggedin' in session:
        userid = session['id']
        username, gender = getUserData(userid)[0], getUserData(userid)[1]

        return render_template('policy.html', title='QuizR - Adatkezelési tájékoztató', logged_in=True, name=username, gender=gender, description=description)
    else:
        return render_template('policy.html', title='QuizR - Adatkezelési tájékoztató', logged_in=False, description=description)
    
@app.route('/howtomakequiz')
def howtomakequiz():
    description = "A Hogyan csinálj quizt oldalon a felhasználók megismerhetik a QuizR használatát. Különböző lehetőségek, funkciók használatát mutatja be. Alapszintű használati útmutató."

    # If the session contains the loggedin variable, we can assume the user is logged in.
    if 'loggedin' in session:
        userid = session['id']
        username, gender = getUserData(userid)[0], getUserData(userid)[1]

        return render_template('howtomakequiz.html', title='QuizR - Quiz pakli készítés útmutató', logged_in=True, name=username, gender=gender, description=description)
    else:
        return render_template('howtomakequiz.html', title='QuizR - Quiz pakli készítés útmutató', logged_in=False, description=description)