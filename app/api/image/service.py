from flask import current_app
from app.utils import err_resp, message, internal_err_resp
from app.models.image import Image

import uuid
import random

from app import db
from app.models.schemas import ImageSchema

image_schema = ImageSchema()

class ImageService:
    @staticmethod
    def get_image_data(image_id):
        """ Pegar dados da imagem pelo image_id """
        if not(image := Image.query.filter_by(id=image_id).first()):
            return err_resp("Image not found!", 404)
        
        from .utils import load_data

        try:
            image_data = load_data(image)
            resp = message(True, "Image data sent")
            resp["image"] = image_data

            return resp, 200

        except Exception as err:
            current_app.logger.error(err)
            return internal_err_resp()

    @staticmethod
    def get_random_image_data():
        """ Pegar dados de uma imagem aleatória """

        # Verifica o número máximo de imagens
        #max_count = Image.query.filter(Image.id >= 1).count()
        max_count = 56

        # Pega um random entre 1 e o número máximo de objetos de Imagem
        rid = random.randint(1, max_count)
            
        if not(image := Image.query.filter_by(id=rid).first()):
            return err_resp("Image not found!", 404)
        
        from .utils import load_data

        try:
            image_data = load_data(image)
            resp = message(True, "Image data sent")
            resp["image"] = image_data

            return resp, 200

        except Exception as err:
            current_app.logger.error(err)
            return internal_err_resp()

    @staticmethod
    def register(data):
        # Assign vars

        ## Required values
        public_id = str(uuid.uuid4())
        name = data["name"]
        link = data["link"]
        category = data["category"]

        # Verificar se o link já existe
        if Image.query.filter_by(link=link).first() is not None:
            return err_resp("Link já cadastrado!", 403)

        try:
            new_image = Image(
                public_id=public_id,
                name=name,
                link=link,
                category=category,
            )

            db.session.add(new_image)
            db.session.flush()

            # Carregar infos do novo usuario
            image_info = image_schema.dump(new_image)

            # Commit mudanças para o DB
            db.session.commit()

            resp = message(True, "Imagem cadsatrada!")
            resp["image"] = image_info

            return resp, 201

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
