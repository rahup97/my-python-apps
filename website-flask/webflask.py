from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/flogin/')
def flogin():
    return render_template("flogin.html")

@app.route('/slogin/')
def slogin():
    return render_template("slogin.html")

if __name__ == "__main__":
    app.run(debug=True)
