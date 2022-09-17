# Validations with Marshmallow
# from marshmallow import Schema, fields
# from marshmallow.validate import Regexp, Length

# class LoginSchema(Schema):
#     """ /auth/login [POST]

#     Parameters:
#     - Email
#     - Password (Str)
#     """

#     email = fields.Email(required=True, validate=[Length(max=64)])
#     password = fields.Str(required=True, validate=[Length(min=8, max=128)])

def load_data(image_db_obj):
    """ Load image's data

    Parameters:
    - Image db object
    """
    from app.models.schemas import ImageSchema

    image_schema = ImageSchema()
    data = image_schema.dump(image_db_obj)

    return data
