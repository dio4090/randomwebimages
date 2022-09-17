from flask import request
from flask_restx import Resource

from app.utils import validation_error
from flask_jwt_extended import jwt_required

# Auth modules
from .service import AuthService
from .dto import AuthDto
from .utils import LoginSchema, RegisterSchema

api = AuthDto.api 
auth_success = AuthDto.auth_success

login_schema = LoginSchema()
register_schema = RegisterSchema()


@api.route("/login")
class AuthLogin(Resource):
    """ User login endpoint
    O usuário se loga e em seguida recebe as informações do usuário e o token de acesso
    """

    auth_login = AuthDto.auth_login

    @api.doc(
        "Auth login",
        responses={
            200: ("Logado.", auth_success),
            400: "Validações falharam.",
            403: "Credenciais incorretas!",
            404: "Credenciais incorretas!",
        },
    )
    @api.expect(auth_login, validate=True)
    @jwt_required()
    def post(self):
        """ Login usando email e senha """
        # Recebe os dados em json
        login_data = request.get_json()

        # Valida os dados
        if (errors := login_schema.validate(login_data)) :
            return validation_error(False, errors), 400

        return AuthService.login(login_data)


@api.route("/register")
class AuthRegister(Resource):
    """
    O usuário se registra e em seguida recebe o token de acesso
    """

    auth_register = AuthDto.auth_register

    @api.doc(
        "Auth registration",
        responses={
            201: ("Usuário registrado com sucesso!", auth_success),
            400: "Falha na validação dos dados!",
        },
    )
    @api.expect(auth_register, validate=True)
    @jwt_required()
    def post(self):
        """ User registration """
        # Recebe os dados em JSON
        register_data = request.get_json()

        # Valida os dados
        if (errors := register_schema.validate(register_data)) :
            return validation_error(False, errors), 400

        return AuthService.register(register_data)
