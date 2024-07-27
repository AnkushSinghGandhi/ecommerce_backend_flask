from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Shipping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    date_shipped = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)