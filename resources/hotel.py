from flask_restful import Resource

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

class Hotel(Resource):
  def get(self, id):
    for hotel in hoteis:
      if hotel['id'] == id:
        return hotel
    return {'message': 'hotel não encontrado'}, 404 #not found