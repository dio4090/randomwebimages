from flask_restx import Namespace, fields
class ImageDto:

    api = Namespace("image", description="Image related operations.")

    image_obj = api.model(
        "Image object",
        {
            "public_id": fields.String,
            "name": fields.String,
            "link": fields.String,
            "category": fields.DateTime,
            "created_at": fields.Integer,
        },
    )

    image_create = api.model(
        "Image data",
        {
            "name": fields.String(required=True),
            "link": fields.String(required=True),
            "category": fields.String(required=True),
        },
    )

    data_resp = api.model(
        "Image Data Response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "image": fields.Nested(image_obj),
        },
    )
