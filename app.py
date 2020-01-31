import os
from flask import Flask
app = Flask(__name__)

def num(s):
    try:
        return float(s)
    except ValueError:
        return 'err'

@app.route('/')
def hello():
    return '<h1><a href="/square/5">Click here to square 5</a></h1>'

@app.route('/square/<n>')
def square(n):
	n = num(n)
	if type(n) == str:
		return 'you cant square a string silly'
	else:
		return f'{float(n)} squared is {n**2}'

@app.route('/cube/<n>')
def cube(n):
	n = num(n)
	if type(n) == str:
		return 'you cant cube a string silly'
	else:
		return f'{float(n)} cubed is {n**3}'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)

