from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=False)
    reviews = db.relationship('Review', backref='book', lazy=True)
    order_items = db.relationship('OrderItem', backref='book', lazy=True)
    cart_items = db.relationship('CartItem', backref='book', lazy=True)
    wishlist_items = db.relationship('Wishlist', backref='book', lazy=True)
