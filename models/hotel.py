class HotelModel:
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