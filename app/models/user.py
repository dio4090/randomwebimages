from datetime import datetime
from app import db, bcrypt

# Alias common DB names
Column = db.Column
Model = db.Model
relationship = db.relationship

class User(Model):
    """ User model para armazenar dados relacionados ao usuário """

    id: int = Column(db.Integer, primary_key=True, autoincrement=True)
    public_id: str = Column(db.String(36), primary_key=True)
    email: str = Column(db.String(64), unique=True, index=True)
    username: str = Column(db.String(15), unique=True, index=True)
    name: str = Column(db.String(100))
    password_hash: str = Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=db.func.now())

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"
