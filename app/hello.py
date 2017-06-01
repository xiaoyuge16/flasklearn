from flask import Flask,render_template
app=Flask(__name__)
from flask_bootstrap import Bootstrap
bootstrap=Bootstrap(app)
from flask import request
from werkzeug.utils import secure_filename
from os import path

#def index():
#    return '<h1>hello flask</h1>'
@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s</h1>'%name
@app.route('/')
def index():
    return render_template('base.html')
@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
         f= request.form
         # return '<h1>%s</h1>'%f
#    return render_template('form.html')
         username=request.form.get('username')
         # return render_template('form.html', method=request.method)
         return '<p>%s</p>'%username
    return render_template('form.html', method=request.method)
#    return render_template('form.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        # return '<h1>%s</h1>'%f.filename
        abspath=path.abspath(path.dirname(__file__))
        # return '%s'%abspath
        uploadpath=path.join(abspath,'static/uploads')
        # return '%s'%uploadpath
        f.save(uploadpath+f.filename )
        # f.save(uploadpath,secure_filename(f.filename ))

    return render_template('upload.html')
if __name__=='__main__':
    app.run(debug='True')
    # app.run(host='0.0.0.0',port='5000')
