from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    stock = db.Column(db.Integer, nullable=False)