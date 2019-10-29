# db_creator.py
 
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///mycontacts.db', echo=True)
Base = declarative_base()
 
 
class Broker(Base):
    __tablename__ = "brokers"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
 
    def __repr__(self):
        return "{}".format(self.name)
 
 
class Contact(Base):
    """"""
    __tablename__ = "contacts"
 
    id = Column(Integer, primary_key=True)
    contact_name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    location = Column(String)
    notes = Column(String)
 
    broker_id = Column(Integer, ForeignKey("brokers.id"))
    broker = relationship("Broker", backref=backref(
        "contacts", order_by=id))
 
# create tables
Base.metadata.create_all(engine)
