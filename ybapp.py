from flask import Flask, render_template, send_from_directory

app = Flask("hello")

@app.route('/')
def home():
    return "Hello, World!"


@app.route('/welcome')
def welcome():
    return render_template('yellow_bird.html')


@app.route('/<dir>/<file_name>')
def static_content(dir, file_name):
    return send_from_directory(dir, file_name)


if __name__ == '__main__':
    app.run()