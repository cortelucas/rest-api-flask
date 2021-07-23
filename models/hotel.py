from create_db import db

class HotelModel(db.Model):
  __tablename__ = 'hoteis'

  id = db.Column(db.String, primary_key=True)
  name = db.Column(db.String(80))
  stars = db.Column(db.Float(precision=1))
  daily = db.Column(db.Float(precision=2))
  city = db.Column(db.String(40))

  def __init__(self, id, name, stars, daily, city):
    self.id = id
    self.name = name
    self.stars = stars
    self.daily = daily
    self.city = city

  def json(self):
    return {
      "id": self.id,
      "name": self.name,
      "stars": self.stars,
      "daily": self.daily,
      "city": self.city
    }

  @classmethod
  def find_hotel(cls, id):
    hotel = cls.query.filter_by(id=id).first() #select * from hoteis where id = id
    if hotel:
      return hotel
    return None

  def save_hotel(self):
    db.session.add(self)
    db.session.commit()