from flask import Flask,render_template
app=Flask(__name__)
#from flask_bootstrap import Bootstrap
#bootstrap=Bootstrap(app)
from flask import request


#def index():
#    return '<h1>hello flask</h1>'
@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s</h1>'%name
@app.route('/')
def index():
    return render_template('base.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    return render_template('upload.html')
if __name__=='__main__':
    app.run(host='0.0.0.0')
