from application import db

class Houses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #house_name = db.Column(db.String(50))
    house_location = db.Column(db.String(50))
    house_size = db.Column(db.Integer)
    house_price = db.Column(db.Integer)
    date_generated = db.Column(db.DateTime)
    def __str__(self):
        return f"{self.house_name}: {self.house_location} with {self.house_size} bedrooms, would cost around {self.house_price}"
        