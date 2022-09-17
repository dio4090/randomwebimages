# Model Schemas
from app import ma

class UserSchema(ma.Schema):
    class Meta:
        # Campos que serão exibidos
        fields = ("public_id","email", "name", "username", "created_at")

class ImageSchema(ma.Schema):
    class Meta:
        # Campos que serão exibidos
        fields = ("public_id","name", "link", "category", "created_at")