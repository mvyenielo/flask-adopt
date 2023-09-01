"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    """Form for adding new pet"""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = SelectField("Age",
                      choices = [('baby', 'Baby'), ('young', 'Young'),
                                 ('adult', 'Adult'), ('senior', 'Senior')])
    notes = StringField("Notes")
    available = BooleanField("Available")

