from flask import Flask

app = Flask('__name__')

@app.route('/')
def home():
    return render_template('*.html')


@app.route('/about')
def about():
    return render_template('*.html')


if __name__ == '__main__':
    app.run(debug = True)
