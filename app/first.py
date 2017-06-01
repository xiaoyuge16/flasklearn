from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return '<h1>Hello World!,Welcome!</h1>'
    # return render_template("base.html")


@app.route('/form', methods=['GET', 'POST'])
def form():
    # if request.method == 'POST':
    #     return render_template('form.html', method=request.method)
    return render_template('form.html', method=request.method)


if __name__ == '__main__':
    app.run(debug=True)
