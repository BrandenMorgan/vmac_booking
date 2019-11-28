from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateTimeField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User, Event


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EventForm(FlaskForm):
    event_name = StringField('Event name', validators=[DataRequired()])
    promoter_name = StringField('Promoter name', validators=[DataRequired()])
    event_date = DateTimeField('Date', format='%m/%d/%Y', validators=[DataRequired()])
    event_type = StringField('Event type', validators=[DataRequired()])
    event_manager = StringField('Event manager', validators=[DataRequired()])
    deposit_amount = IntegerField('Deposit amount', validators=[DataRequired()])
    guest_count = IntegerField('Guest count', validators=[DataRequired()])
    bar_min = IntegerField('Bar minimum', validators=[DataRequired()])
    other_notes = TextAreaField('Other notes', validators=[Length(min=0, max=140)])
    booked = BooleanField('Booked')
    tsl_approved = BooleanField('TSL approved?')
    balance_paid = BooleanField('Balance paid?')
    contract_sent = BooleanField('Contract sent?')
    cleaning = BooleanField('Cleaning')
    deposit_paid = BooleanField('Deposit paid?')
    bar = BooleanField('Bar?')
    submit = SubmitField('Submit')


class EventDetailsForm(FlaskForm):
    event_name = StringField('Event name', validators=[DataRequired()])
    promoter_name = StringField('Promoter name', validators=[DataRequired()])
    event_date = DateTimeField('Date', format='%m/%d/%Y', validators=[DataRequired()])
    event_type = StringField('Event type', validators=[DataRequired()])
    event_manager = StringField('Event manager', validators=[DataRequired()])
    deposit_amount = IntegerField('Deposit amount', validators=[DataRequired()])
    guest_count = IntegerField('Guest count', validators=[DataRequired()])
    bar_min = IntegerField('Bar minimum', validators=[DataRequired()])
    other_notes = TextAreaField('Other notes', validators=[Length(min=0, max=140)])
    booked = BooleanField('Booked')
    tsl_approved = BooleanField('TSL approved?')
    balance_paid = BooleanField('Balance paid?')
    contract_sent = BooleanField('Contract sent?')
    cleaning = BooleanField('Cleaning')
    deposit_paid = BooleanField('Deposit paid?')
    bar = BooleanField('Bar?')
    submit = SubmitField('Update')
    id = IntegerField('ID')

    class DeleteEventForm(FlaskForm):
        event_name = StringField('Event name', validators=[DataRequired()])
        promoter_name = StringField('Promoter name', validators=[DataRequired()])
        event_date = DateTimeField('Date', format='%m/%d/%Y', validators=[DataRequired()])
        event_type = StringField('Event type', validators=[DataRequired()])
        event_manager = StringField('Event manager', validators=[DataRequired()])
        deposit_amount = IntegerField('Deposit amount', validators=[DataRequired()])
        guest_count = IntegerField('Guest count', validators=[DataRequired()])
        bar_min = IntegerField('Bar minimum', validators=[DataRequired()])
        other_notes = TextAreaField('Other notes', validators=[Length(min=0, max=140)])
        booked = BooleanField('Booked')
        tsl_approved = BooleanField('TSL approved?')
        balance_paid = BooleanField('Balance paid?')
        contract_sent = BooleanField('Contract sent?')
        cleaning = BooleanField('Cleaning')
        deposit_paid = BooleanField('Deposit paid?')
        bar = BooleanField('Bar?')
        submit = SubmitField('Delete')
