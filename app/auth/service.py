import uuid
from datetime import datetime
from flask import current_app
from flask_jwt_extended import create_access_token

from app import db
from app.utils import message, err_resp, internal_err_resp
from app.models.user import User
from app.models.schemas import UserSchema

user_schema = UserSchema()

class AuthService:
    @staticmethod
    def login(data):
        # Credenciais
        email = data["email"]
        password = data["password"]

        try:
            # Buscando dados do usuário
            if not (user := User.query.filter_by(email=email).first()):
                return err_resp(
                    "ERROR! Usuário ou senha inválido!",
                    403,
                )

            elif user and user.verify_password(password):
                user_info = user_schema.dump(user)

                access_token = create_access_token(identity=user.id)

                resp = message(True, "Login realizado com sucesso!")
                resp["access_token"] = access_token
                resp["user"] = user_info

                return resp, 200

            return err_resp(
                "ERROR! Usuário ou senha inválido!", 403
            )

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def register(data):
        # Assign vars

        ## Required values
        public_id = str(uuid.uuid4())
        email = data["email"]
        username = data["username"]
        password = data["password"]

        ## Optional
        data_name = data.get("name")

        # Verificar se o e-mail está em uso
        if User.query.filter_by(email=email).first() is not None:
            return err_resp("Esse e-mail já está em uso!", 403)

        # Check if the username is taken
        if User.query.filter_by(username=username).first() is not None:
            return err_resp("Esse usuário já está em uso!.", 403)

        try:
            new_user = User(
                public_id=public_id,
                email=email,
                username=username,
                name=data_name,
                password=password,
            )

            db.session.add(new_user)
            db.session.flush()

            # Carregar infos do novo usuario
            user_info = user_schema.dump(new_user)

            # Commit mudanças para o DB
            db.session.commit()

            # Criar um token de acesso
            access_token = create_access_token(identity=new_user.id)

            resp = message(True, "Usuário Cadastrado!!!")
            resp["access_token"] = access_token
            resp["user"] = user_info

            return resp, 201

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
