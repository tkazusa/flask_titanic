# -*- encoding: UTF-8 -*-
from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SelectField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired()])
    Sex = RadioField('Sex',
                     choices=[(0, 'Mail'), (1, 'Female')],
                     validators=[DataRequired()])
    Age = IntegerField("Age", validators=[DataRequired()])
    Embarked = RadioField('Embarked',
                          choices=[('C', 'Cherbourg'),
                                   ('Q', 'Queenstown'),
                                   ('S', 'Southampton')],
                          validators=[DataRequired()])
    Pclass = RadioField('pclass',
                        choices=[('1', '1st'),
                                 ('2', '2nd'),
                                 ('3', '3rd')],
                        validators=[DataRequired()])
    SibSp = IntegerField('SibSp', validators=[DataRequired()])
    Parch = IntegerField('Parch', validators=[DataRequired()])
    Cabin = StringField('Cabin', validators=[DataRequired()])
    Ticket = StringField('Ticket', validators=[DataRequired()])
    submit = SubmitField("Send")
