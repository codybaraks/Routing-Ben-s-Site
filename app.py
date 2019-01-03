from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/add')
def add():
    return render_template('generic.html')


@app.route('/form')
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run()
