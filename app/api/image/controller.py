from flask import request
from flask_restx import Resource

from app.utils import validation_error
from flask_jwt_extended import jwt_required

from .service import ImageService
from .dto import ImageDto

from .utils import load_data

create_schema = load_data

api = ImageDto.api
data_resp = ImageDto.data_resp

@api.route("/random")
class ImageGet(Resource):
    @api.doc(
        "Get one randomic image",
        responses={
            200: ("Image data successfully sent", data_resp),
            404: "Image not found!",
        },
    )
    def get(self):
        """ Get one randomic image """
        return ImageService.get_random_image_data()

@api.route("/<string:image_id>")
class ImageGet(Resource):
    @api.doc(
        "Get a specific image",
        responses={
            200: ("Image data successfully sent", data_resp),
            404: "Image not found!",
        },
    )
    @jwt_required()
    def get(self, image_id):
        """ Get a specific image's by their image_id """
        return ImageService.get_image_data(image_id)

@api.route("/create")
class AuthRegister(Resource):
    """
    O usuário se registra e em seguida recebe o token de acesso
    """

    image_register = ImageDto.image_create

    @api.doc(
        "Image registration",
        responses={
            201: ("Imagem registrada com sucesso!"),
            400: "Falha na validação dos dados!",
        },
    )
    @api.expect(image_register, validate=True)
    @jwt_required()
    def post(self):
        """ Image registration """
        # Recebe os dados em JSON
        register_data = request.get_json()

        return ImageService.register(register_data)
