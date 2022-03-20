from enum import unique
from optparse import TitledHelpFormatter
from turtle import tiltangle
from . import db

class UserProperty(db.Model):
    __tablename__ = 'propertylist'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    description = db.Column(db.Text(),nullable = False)
    numroom = db.Column(db.Integer,nullable = False)
    numbath = db.Column(db.Integer,nullable = False)
    price = db.Column(db.Float,nullable = False)
    property_type = db.Column(db.String(20),nullable = False)
    location = db.Column(db.Text(),nullable = False)
    filename = db.Column(db.String(255))


    def __init__(self,title,description,numroom,numbath,price,property_type,location,filename):
        self.title = title
        self.description = description
        self.numroom = numroom
        self.numbath = numbath
        self.price = price
        self.property_type = property_type
        self.location = location
        self.filename= filename


   