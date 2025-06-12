from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home5():
    return render_template("home.html")

@app.route('/users')
def user():
    return render_template("usuarios.html")

if __name__ == '__main__':
    app.run(debug=True)
