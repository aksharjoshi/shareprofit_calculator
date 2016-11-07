#! flask/bin/python
from flask import Flask, render_template,request,jsonify
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
     return render_template ('index.html')

@app.route('/user/<name>',methods=['GET'])
def user(name=None):
	return render_template('index.html',name=name)

@app.route('/data',methods=['POST'])
def data():
    #jsondata = {"email": request.form['email']}
    #jsondata = { "id": "1001", "type": "Regular" }    
    data = json.dumps({ "id": "1001", "type": "Regular" })
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
