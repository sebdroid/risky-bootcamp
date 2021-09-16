import os, random, ast, unittest

from flask import Flask, render_template, request, make_response

class UnitTests(unittest.TestCase):

    def test_generatessixnumbers(self):
        self.assertEqual(len(list), 6)

    # def test_uniqueNumbers(self):
    #     flag = 0
    #     flag = len(set(list)) == len(list)

    #     if(flag):
    #         return(True)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generateNumber():
    cookie = []

    if isinstance(request.cookies.get('randomNumbers'), str) and request.method == 'GET':
        cookie = ast.literal_eval(request.cookies.get('randomNumbers'))
        if not isinstance(cookie, list):
            cookie = []
    

    newNumbers = random.sample(range(1, 60), 6)
    newNumbers.sort()
    lottoNumbers=" ".join(str(x) for x in newNumbers)

    response = make_response(render_template('index.html', numbers=lottoNumbers, cookies=cookie))
    cookie.append(lottoNumbers)
    response.set_cookie('randomNumbers', str(cookie))
    return response
 