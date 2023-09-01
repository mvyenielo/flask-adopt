"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    """Database model for pet"""

    __tablename__="pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(30),
        nullable=False
    )

    species = db.Column(
        db.String(30),
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default=''
    )

    species = db.Column(
        db.String(30),
        nullable=False
    )

    notes = db.Column(
        db.String(500),
        nullable=True
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)
