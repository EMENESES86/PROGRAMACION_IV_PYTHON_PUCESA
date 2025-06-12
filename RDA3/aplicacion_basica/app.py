from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a Flask"

@app.route('/base.html')
def base_template():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)