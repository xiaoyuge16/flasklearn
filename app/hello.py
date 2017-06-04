# coding:utf-8
from flask import Flask, render_template, request
from flask_nav import Nav
from flask_nav.elements import *
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from os import path

app = Flask(__name__)
bootstrap = Bootstrap(app)
nav = Nav()
#
# nav.register_element('top',Navbar(u'Flask入门',
#                                     View(u'主页','home'),
#                                     View(u'关于','about'),
#                                     Subgroup(u'项目',
#                                              View(u'项目一','about'),
#                                              Separator(),
#                                              View(u'项目二', 'service'),
#                                     ),
# ))

nav.register_element('top', Navbar(u'狗狗爱豆豆',
                                   View(u'上传文件', 'upload'),
                                   View(u'登录', 'form'),
                                   View(u'登录', 'form'),
                                   Subgroup(u'登录',
                                            View(u'登录', 'form'),
                                            Separator(),
                                            View(u'登录', 'form'),
                                            ),
                                   ))
#
nav.init_app(app)


# def index():
#    return '<h1>hello flask</h1>'
@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s</h1>' % name


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        f = request.form
        # return '<h1>%s</h1>'%f
        #    return render_template('form.html')
        username = request.form.get('username')
        # return render_template('form.html', method=request.method)
        return '<p>%s</p>' % username
    return render_template('form.html', method=request.method)


#    return render_template('form.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        # return '<h1>%s</h1>'%f.filename
        abspath = path.abspath(path.dirname(__file__))
        # return '%s'%abspath
        uploadpath = path.join(abspath, 'static/uploads')
        # return '%s'%uploadpath
        f.save(uploadpath + f.filename)
        # f.save(uploadpath,secure_filename(f.filename ))

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug='True')
    # app.run(host='0.0.0.0',port='5000')
