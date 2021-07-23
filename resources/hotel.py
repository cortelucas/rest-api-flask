from types import new_class
from flask_restful import Resource, reqparse
from models.hotel import HotelModel


class Hoteis(Resource):
  def get(self):
    return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]} #SELECT * FROM hoteis

class Hotel(Resource):
  arguments = reqparse.RequestParser()

  arguments.add_argument('name', type=str, required=True, help="this field 'name' connot be left blank.")
  arguments.add_argument('stars', type=float, required=True, help="this field 'stars' connot be left blank.")
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
    try:
      hotel.save_hotel()
    except:
      return {'message': 'An internal error ocurred tring to save hotel.'}, 500 #internal error
    return hotel.json()
  
  def put(self, id):
    data = Hotel.arguments.parse_args()

    hotel_encontrado = HotelModel.find_hotel(id)
    if hotel_encontrado:
      hotel_encontrado.update_hotel(**data)
      hotel_encontrado.save_hotel()
      return hotel_encontrado.json(), 200 #ok
    hotel = HotelModel(id, **data)
    try:
      hotel.save_hotel()
    except:
      return {'message': 'An internal error ocurred tring to save hotel.'}, 500 #internal error

    return hotel.json(), 201 #created
  
  def delete(self, id):
    hotel = HotelModel.find_hotel(id)
    if hotel:
      try:
        hotel.delete_hotel()
      except:
        return {'message': 'An error ocurred trying to delete hotel.'}
      return {'message': 'hotel deleted.'}
    return {'message': 'Hotel not found'}, 404