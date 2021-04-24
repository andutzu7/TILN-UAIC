from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return {'rows':'vim'} 


@app.route('/api',methods=['GET'])
def api():
  return{
    'userid':1,
    'title':'console application',
    'completed':True
  }
