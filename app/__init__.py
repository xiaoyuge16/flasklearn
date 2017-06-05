# -*- coding: utf-8 -*-
from flask import Flask
from flask_nav import Nav
from flask_nav.elements import *
from flask_bootstrap import Bootstrap
from views import init_views

bootstrap = Bootstrap()
nav = Nav()

def creat_app():
    app = Flask(__name__)
    nav.register_element('top', Navbar(u'狗狗爱豆豆',
                                       View(u'主页', 'index'),
                                       View(u'上传文件', 'upload'),
                                       View(u'登录', 'form'),
                                       # View(u'欢迎', 'user'),
                                       ))
    bootstrap.init_app(app)
    nav.init_app(app)
    init_views(app)
    return app


