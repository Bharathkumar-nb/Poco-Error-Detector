from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import json
import ast
import utilities

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/getAnswers', methods=['POST'])
def getAnswers():
    result = utilities.parseResult(request.form)
    # return json.dumps(request.form)
    return result

if __name__ == '__main__':
    app.run(debug=True)