from app import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    health = db.Column(db.Integer, default=100)
    happiness = db.Column(db.Integer, default=100)
    energy = db.Column(db.Integer, default=100)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    owner = db.relationship('User', backref='pets')
