# -*- encoding: UTF-8 -*-
from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SelectField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    sex = RadioField('Sex', choices=[(0, 'Mail'), (1, 'Female')])
    age = IntegerField("Age")
    embarked = RadioField('Embarked',
                           choices=[('C', 'Cherbourg'),
                                    ('Q', 'Queenstown'),
                                    ('S', 'Southampton')])
    sibsp = IntegerField('SibSp')
    parch = IntegerField('Parch')
    cabin = StringField('Cabin')
    ticket = StringField('Ticket')
    submit = SubmitField("Send")
