from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from send_mail import send_email
from sqlalchemy.sql import func

app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:post123@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    email_col = db.Column(db.String(120), unique = True)
    height_col = db.Column(db.Integer)

    def __init__(self, email_col, height_col):
        self.email_col = email_col
        self.height_col = height_col



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        if db.session.query(Data).filter(Data.email_col == email).count() == 0:
            info = Data(email, height)
            db.session.add(info)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_col)).scalar()
            average_height = round(average_height, 2)
            count = db.session.query(Data.height_col).count()
            send_email(email, height, average_height, count)
            return render_template('success.html')
    return render_template('index.html', text = "Hey we've already got your height!")

if __name__ == '__main__':
    app.run(debug = True)
