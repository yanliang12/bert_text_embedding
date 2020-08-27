##############server_path.py##############
import time
import logging
import argsparser
from flask_restplus import *
from flask import *

import numpy 
from jessica_text_embedding import text_embedding

ns = Namespace('jessica', description='')
args = argsparser.prepare_args()

parser = ns.parser()
parser.add_argument('text', type=str, location='json')

req_fields = {'text': fields.String(example = u"Abu Dhabi Finance")}
jessica_api_req = ns.model('jessica_req_fields', req_fields)

rsp_fields = {
	'embedding_vector': fields.List(fields.Float),
	'embedding_vector_dim':fields.Integer,
	'error':fields.String,
	'running_time':fields.Float
	}

jessica_api_rsp = ns.model('jessica_rsp_fields', rsp_fields)

@ns.route('/bert_text_embedding')
class jessica_api(Resource):
	def __init__(self, *args, **kwargs):
		super(jessica_api, self).__init__(*args, **kwargs)
	@ns.marshal_with(jessica_api_rsp)
	@ns.expect(jessica_api_req)
	def post(self):		
		start = time.time()
		try:			
			args = parser.parse_args()		
			output = {}
			output['embedding_vector_dim'] = 2048
			output['embedding_vector'] = text_embedding(args['text'])
			output['error'] = 'success'
			output['running_time'] = float(time.time()- start)
			return output, 200
		except Exception as e:
			output = {}
			output['error'] = str(e)
			output['running_time'] = float(time.time()- start)
			return output
##############server_path.py##############
