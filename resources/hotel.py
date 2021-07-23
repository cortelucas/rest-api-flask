from types import new_class
from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
  {
    'id': 'alpha',
    'name': 'Alpha Hotel',
    'stars': 4.3,
    'daily': 420.34,
    'city': 'Rio de Janeiro'
  },
  {
    'id': 'bravo',
    'name': 'Bravo Hotel',
    'stars': 4.4,
    'daily': 380.90,
    'city': 'Santa Catarina'
  },
  {
    'id': 'charlie',
    'name': 'Charlie Hotel',
    'stars': 4.3,
    'daily': 420.34,
    'city': 'São Salvador'
  },
]


class Hoteis(Resource):
  def get(self):
    return {'hoteis': hoteis}

class Hotel(Resource):
  arguments = reqparse.RequestParser()

  arguments.add_argument('name')
  arguments.add_argument('stars')
  arguments.add_argument('daily')
  arguments.add_argument('city')  

  def get(self, id):
    hotel = HotelModel.find_hotel(id)

    if hotel:
      return hotel.json()
    return {'message': 'hotel não encontrado'}, 404 #not found
    
  def post(self, id):   
    if HotelModel.find_hotel(id):
      return {'message': f'Hotel id {id} already exists'}, 400 # bad request


    data = Hotel.arguments.parse_args()
    hotel = HotelModel(id, **data)
    
    hotel.save_hotel()

    return hotel.json()
  
  def put(self, id):
    data = Hotel.arguments.parse_args()
    object_hotel = HotelModel(id, **data)
    new_hotel = object_hotel.json()

    hotel = Hotel.find_hotel(id)
    if hotel:
      hotel.update(new_hotel)
      return new_hotel, 200 #ok
    hoteis.append(new_hotel)
    return new_hotel, 201 #created
  
  def delete(self, id):
    global hoteis # referencia a lista global
    hoteis = [hotel for hotel in hoteis if hotel['id'] != id]
    return {'message': 'hotel deletado.'}