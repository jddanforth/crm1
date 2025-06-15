from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f"<Contact {self.email}>"
