from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    plaid_account_id = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    official_name = db.Column(db.String(120))
    type = db.Column(db.String(50))
    subtype = db.Column(db.String(50))
    mask = db.Column(db.String(10))
    balances = db.Column(db.Float)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    plaid_transaction_id = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date)
    name = db.Column(db.String(255))
    amount = db.Column(db.Float)
    category = db.Column(db.String(120))
    iso_currency_code = db.Column(db.String(10))
    pending = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
