import os, random, ast

from flask import Flask, render_template, request, make_response

import unittest

from flask.wrappers import Response

class UnitTests(unittest.TestCase):

    def test_generatessixnumbers(self):
        self.assertEqual(len(list), 6)

    def test_uniqueNumbers(self):
        flag = 0
        flag = len(set(list)) == len(list)

        if(flag):
            return(True)


app = Flask(__name__)

@app.route('/')
def generateNumber():
    if isinstance(request.cookies.get('randomNumbers'), str):
        cookie = ast.literal_eval(request.cookies.get('randomNumbers'))
        if isinstance(cookie, list):
            print(cookie)

    newNumbers = random.sample(range(1, 60), 6)
    newNumbers.sort()

    response = make_response(render_template('index.html', numbers=" ".join(str(x) for x in newNumbers), cookies=cookie))
    response.set_cookie('randomNumbers', str(newNumbers))
    return response
 