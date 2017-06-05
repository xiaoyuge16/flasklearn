# -*- coding: utf-8 -*-
from flask import  render_template,request
from werkzeug.utils import secure_filename
from os import path

def init_views(app):
    @app.route('/')
    def index():
        return render_template('base.html')


    @app.route('/user/<name>')
    def user(name):
        return '<h1>Welcome,%s</h1>' % name


    @app.route('/form', methods=['GET', 'POST'])
    def form():
        if request.method == 'POST':
            f = request.form
            username = request.form.get('username')
            # return render_template('form.html', method=request.method)
            return u'<p>用户名是%s</p>' % username
        return render_template('form.html', method=request.method)


    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':
            f = request.files['file']
            filename = f.filename
            abspath = path.abspath(path.dirname(__file__))
            uploadpath = path.join(abspath, 'static/uploads')
            f.save(uploadpath + secure_filename(f.filename))
            return '<div class="container">上传路径是：%s</div>' % uploadpath
        return render_template('upload.html')

