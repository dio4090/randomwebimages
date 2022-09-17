from datetime import datetime
from app import db, bcrypt

# Alias common DB names
Column = db.Column
Model = db.Model
relationship = db.relationship

class Image(Model):
    """ Image model para armazenar dados relacionados a imagem """

    id: int = Column(db.Integer, primary_key=True, autoincrement=True)
    public_id: str = Column(db.String(36), primary_key=True)
    name: str = Column(db.String(70), unique=False, index=True)
    link: str = Column(db.String(255), unique=True, index=True)
    category: str = Column(db.String(25))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=db.func.now())

    def __init__(self, **kwargs):
        super(Image, self).__init__(**kwargs)

    def __repr__(self):
        return f"<Image {self.name}>"
