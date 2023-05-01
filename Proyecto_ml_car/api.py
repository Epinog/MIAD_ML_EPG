#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from flask_cors import CORS
#se carga la función del Modelo.py
from Modelo import predict_price

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

api = Api(
    app, 
    version='1.0', 
    title='API - Model Prediction Price Car',
    description='Machile Learning Model to predict car prices')

ns = api.namespace('predict', 
     description='Car price regressor')
   
parser = api.parser()

parser.add_argument(
    'Year', 
    type=str, 
    required=True, 
    help='Model car year', 
    location='args')

parser.add_argument(
    'Mileage', 
    type=str, 
    required=True, 
    help='Car mileage', 
    location='args')

parser.add_argument(
    'State', 
    type=str, 
    required=True, 
    help='USA State', 
    location='args')

parser.add_argument(
    'Make', 
    type=str, 
    required=True, 
    help='Car manufacturer', 
    location='args')

parser.add_argument(
    'Model', 
    type=str, 
    required=True, 
    help='Car model', 
    location='args')

resource_fields = api.model('Resource', {
    'Estimated price for this car is': fields.String,
})

@ns.route('/')
class CarApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        return {
         "result": predict_price([args['Year'],args['Mileage'],args['State'],args['Make'],args['Model']])
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)


# In[2]:


pip install flask_restx


# In[ ]:




