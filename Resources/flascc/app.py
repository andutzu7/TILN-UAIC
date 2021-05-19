
from flask import Flask
from flask import jsonify
#from flask_cors import CORS,cross_origin
from flask import request
from NN import predict

app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'


# @cross_origin(support_credentials=True)
@app.route("/",methods=['POST'])
def helloWorld():
  msg_type = request.get_json().get('type')
  if msg_type == 'string':
    result = predict.predict_by_text(request.get_json().get('text').get('text'))
  else:
    result = predict.predict_by_link(request.get_json().get('text').get('text'))


  answer = predict.print_predictions(result)
  return jsonify({'text':answer} )