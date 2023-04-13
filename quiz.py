from flask import Flask, session, redirect, request, url_for, render_template, Response, jsonify

hostIp = '127.0.0.1'
hostPort = 5003
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/learn/<material>')
def learn(material):
    return render_template('learn.html',)

if __name__ == '__main__':
    app.run(host=hostIp, port=hostPort, debug=False)
    print("\n")