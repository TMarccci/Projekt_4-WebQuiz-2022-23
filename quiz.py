from flask import Flask, session, redirect, request, url_for, render_template, Response, jsonify
import mysql.connector.pooling

# Flask Settings
hostIp = '127.0.0.1'
hostPort = 5004
# Database Settings
dbHost = 'vpn.tmarccci.hu'
dbUser = 'qpbackend'
dbPass = 'quiz123@'
dbName = 'quizpro'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', title='QuizPro - Home')

@app.route('/learn/<materialid>')
def learn(materialid):
    return render_template('learn.html', title='QuizPro - Material Name')

@app.route('createmarterial/<materialid>')
def creatematerial(materialid):
    return render_template('creatematerial.html', title='QuizPro - Create Material')

if __name__ == '__main__':
    app.run(host=hostIp, port=hostPort, debug=False)
    print("\n")