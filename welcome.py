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
    #challenge_no =  request.form['opt_challenge'];
    #env_poco = request.form['poco_radio'];
    #env_note = request.form['note_radio'];
    #usr_code = request.form['code'];
    #usr_error = request.form['error'];
    result = utilities.parseResult(request.form)
    # return json.dumps(request.form)
    return result

if __name__ == '__main__':
    app.run(debug=True)