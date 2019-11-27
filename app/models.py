from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from flask_login import UserMixin
from flask_table import Table, Col, LinkCol

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    events = db.relationship('Event', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Event(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        event_name = db.Column(db.String(120), index=True)
        promoter_name = db.Column(db.String(64), index=True)
        event_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
        event_type = db.Column(db.String(64), index=True)
        event_manager = db.Column(db.String(64), index=True)
        deposit_amount = db.Column(db.Integer)
        guest_count = db.Column(db.Integer)
        bar_min = db.Column(db.Integer)
        other_notes = db.Column(db.String(64), index=True)
        booked = db.Column(db.Boolean, default=False)
        tsl_approved = db.Column(db.Boolean, default=False)
        balance_paid = db.Column(db.Boolean, default=False)
        contract_sent = db.Column(db.Boolean, default=False)
        cleaning = db.Column(db.Boolean, default=False)
        deposit_paid = db.Column(db.Boolean, default=False)
        bar = db.Column(db.Boolean, default=False)
        update = LinkCol('Update', 'update_event', url_kwargs=dict(id='id'))
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

        def __repr__(self):
            return '<Event {}>'.format(self.event_name)
