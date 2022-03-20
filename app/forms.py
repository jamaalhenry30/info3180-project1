#from msilib.schema import Property
#from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,IntegerField,FloatField,HiddenField,SubmitField
from wtforms.validators import DataRequired,InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
   
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    numroom = IntegerField('No. of Rooms', validators=[InputRequired()])
    numbath = IntegerField('No of Bathrooms', validators=[InputRequired()])
    price = FloatField('Price', validators=[InputRequired()])
    property_type = SelectField('Property Type', choices = [('House','House'),('Appartment','Appartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])
     
