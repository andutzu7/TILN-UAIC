from flask import Flask
from flask import jsonify
from flask_cors import CORS,cross_origin
from flask import request

import os
print(os.cwd())

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'


@cross_origin(support_credentials=True)
@app.route("/",methods=['POST'])
def helloWorld():
  print(request.args)
  return jsonify({'text':'vim'} )

