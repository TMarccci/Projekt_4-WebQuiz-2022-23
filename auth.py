from flask import session, redirect, request, url_for, render_template, Response, jsonify, flash
from app import app, cnxpool
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

@app.route('/register')
def register():
    if 'loggedin' in session:
        return redirect(url_for('index'))
    return render_template('auth/register.html', title='QuizR - Regisztráció', reg=True)

@app.route('/register', methods=['POST'])
def register_post():
    # Parse form data
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    gender = request.form.get('gender')
    remember = True if request.form.get('remember') else False
    if gender == "male":
        gender = False
    else:
        gender = True
    dob = request.form.get('dob')
    generatedUUID = str(uuid.uuid4())

    # Check if user exists
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))

    if cursor.fetchone() is not None:
        cursor.close()
        cnx.close()

        flash('Ezzel az email címmel már regisztráltak!')
        return render_template('auth/register.html', title='QuizR - Regisztráció')

    # Close cursor and connection
    cursor.close()
    cnx.close()

    # Register user
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()

    # Database structure: Table: users
    # id	userid	email	username	password	dob	regdate	lastlogin	sex	

    # Create user
    sql = ("INSERT INTO users (userid, email, username, password, dob, regdate, lastlogin, sex) VALUES (%s, %s, %s, %s, %s, NOW(), NULL, %s)")
    var = (generatedUUID, email, username, generate_password_hash(password, method='sha256'), dob, gender)
    cursor.execute(sql, var)
    cnx.commit()
    cnx.close()

    if remember:
        session['loggedin'] = True
        session['id'] = generatedUUID

        # Update last login
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("UPDATE users SET lastlogin = NOW() WHERE userid = %s", (generatedUUID,))
        cnx.commit()
        cnx.close()

        return redirect(url_for('index'))

    return redirect(url_for('login'))

@app.route('/login')
def login():
    if 'loggedin' in session:
        return redirect(url_for('index'))
    return render_template('auth/login.html', title='QuizR - Bejelentkezés', reg=False)

@app.route('/login', methods=['POST'])
def login_post():
    # Parse form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if user exists
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user is None:
        cursor.close()
        cnx.close()

        flash('Hibás email cím vagy jelszó!')
        return render_template('auth/login.html', title='QuizR - Bejelentkezés')

    # Close cursor and connection
    cursor.close()
    cnx.close()

    # Check password
    if check_password_hash(user[4], password):
        # Update last login
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute("UPDATE users SET lastlogin = NOW() WHERE id = %s", (user[0],))
        cnx.commit()
        cnx.close()

        # Remember user to session
        session['loggedin'] = True
        session['id'] = user[1]

        return redirect(url_for('index'))

    flash('Hibás email cím vagy jelszó!')
    return render_template('auth/login.html', title='QuizR - Bejelentkezés')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    return redirect(url_for('index'))
