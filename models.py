# models.py 
 
from app import db
 
 
class Broker(db.Model):
    __tablename__ = "brokers"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
 
    def __repr__(self):
        return "<Broker: {}>".format(self.name)
 
 
class Contact(db.Model):
    """"""
    __tablename__ = "contacts"
 
    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    address = db.Column(db.String)
    location = db.Column(db.String)
    notes = db.Column(db.String)
 
    broker_id = db.Column(db.Integer, db.ForeignKey("brokers.id"))
    broker = db.relationship("Broker", backref=db.backref(
        "contacts", order_by=id), lazy=True)
