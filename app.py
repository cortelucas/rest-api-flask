from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
  {
    'id': 'alpha',
    'nome': 'Alpha Hotel',
    'estrelas': 4.3,
    'diaria': 420.34,
    'cidade': 'Rio de Janeiro'
  },
  {
    'id': 'bravo',
    'nome': 'Bravo Hotel',
    'estrelas': 4.4,
    'diaria': 380.90,
    'cidade': 'Santa Catarina'
  },
  {
    'id': 'charlie',
    'nome': 'Charlie Hotel',
    'estrelas': 4.3,
    'diaria': 420.34,
    'cidade': 'São Salvador'
  },
]

class Hoteis(Resource):
  def get(self):
    return {'hoteis': hoteis}

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
  app.run(debug=True)