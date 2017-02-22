# -*- coding: UTF-8 -*-
from flask import *
from app.main import main
from app.redisdb import *


@main.route('/abc', methods=['POST'])
def getset():

    return jsonify({
                    'code': 0,

    })


@main.route('/', methods=['GET'])
def index():
    return jsonify({'a':'a'})