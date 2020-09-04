from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	user_logged_in = True
	return render_template('basic.html', user_logged_in=user_logged_in)

@app.route('/information')
def info():
	return '<h1>Hello Sir!</h1>\n'


#Dynamic routing
@app.route('/people/<name>')
def persons(name):
	upper = name.upper()
	return f"This profile belongs to {upper}.\n"


if __name__ == "__main__":
    app.run()
    #app.run(debug=True)
