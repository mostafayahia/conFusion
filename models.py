import os
from sqlalchemy import (
    Column, String, Integer, create_engine, Float,
    Boolean, DateTime, ForeignKey
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()


def rollback():
    """Rollback if transaction not successful"""
    db.session.rollback()


def close_connection():
    """Close the connection to make it available for reusing"""
    db.session.close()


def setup_db(app, database_path=database_path):
    """
    setup_db(app)
        binds a flask application and a SQLAlchemy service
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


class Dish(db.Model):
    """
    Dish
    """
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image = Column(String, nullable=False)
    category = Column(String, nullable=False)
    label = Column(String)
    price = Column(Float, nullable=False)
    featured = Column(Boolean)
    description = Column(String)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'category': self.category,
            'label': self.label,
            'price': self.price,
            'featured': self.featured,
            'description': self.description
        }


class Promotion(db.Model):
    """
    Promotion
    """
    __tablename__ = 'promotions'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image = Column(String, nullable=False)
    label = Column(String)
    price = Column(Float, nullable=False)
    featured = Column(Boolean)
    description = Column(String, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'label': self.label,
            'price': self.price,
            'featured': self.featured,
            'description': self.description
        }


class Comment(db.Model):
    """
    Comment
    """
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    dishid = Column(Integer)
    ForeignKey(column=dishid, ondelete='SET NULL')
    rating = Column(Float, nullable=False)
    comment = Column(String, nullable=False)
    author = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'dishid': self.dishid,
            'rating': self.rating,
            'comment': self.comment,
            'author': self.author,
            'date': self.date
        }
