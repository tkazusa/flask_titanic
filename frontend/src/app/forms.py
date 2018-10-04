# -*- encoding: UTF-8 -*-
from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SelectField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    sex = RadioField('Sex',
                     choices=[(0, 'Mail'), (1, 'Female')],
                     validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    embarked = RadioField('Embarked',
                          choices=[('C', 'Cherbourg'),
                                   ('Q', 'Queenstown'),
                                   ('S', 'Southampton')],
                          validators=[DataRequired()])
    pclass = RadioField('pclass',
                        choices=[('1', '1st'),
                                 ('2', '2nd'),
                                 ('3', '3rd')],
                        validators=[DataRequired()])
    sibsp = IntegerField('SibSp', validators=[DataRequired()])
    parch = IntegerField('Parch', validators=[DataRequired()])
    cabin = StringField('Cabin', validators=[DataRequired()])
    ticket = StringField('Ticket', validators=[DataRequired()])
    submit = SubmitField("Send")
