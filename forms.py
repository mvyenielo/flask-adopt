"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, Length


class AddPetForm(FlaskForm):
    """Form for adding new pet"""

    name = StringField("Pet Name", validators=[InputRequired(), Length(max=30)])
    species = SelectField("Species",
                          choices=[('cat', 'Cat'), ('dog', 'Dog'),
                                   ('porcupine', 'Porcupine')],
                          validators=[InputRequired(),
                                      AnyOf(['cat', 'dog', 'porcupine']),
                                      Length(max=30)])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField("Age",
                      choices=[('baby', 'Baby'), ('young', 'Young'),
                               ('adult', 'Adult'), ('senior', 'Senior')],
                      validators=[InputRequired(),
                                  AnyOf(['baby', 'young', 'adult', 'senior']),
                                  Length(max=30)])
    notes = TextAreaField("Notes", validators=[Optional(), Length(max=500)])


class EditPetForm(FlaskForm):
    """Form for editing pet info"""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional(), Length(max=500)])
    available = BooleanField("Available", validators=[Optional()])

# TODO: take out length validator for SelectField
