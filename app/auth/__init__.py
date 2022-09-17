from flask_restx import Api
from flask import Blueprint

# Import auth namespace
from .contoller import api as auth_ns
from ..api.user.controller import api as user_ns
from ..api.image.controller import api as image_ns

#Basic Authentication
authorizations = {
    "basicAuth" : {
        "type" : "basic"
    }
}

#Criação das rotas utilizando o blueprint
auth_bp = Blueprint("auth", __name__)

auth = Api(
    auth_bp,
    title="Random Image Generator MVC API",
    version='1.0',
    description="rigapp MVC API",
    authorizations=authorizations
)

# API namespaces
auth.add_namespace(auth_ns)
auth.add_namespace(user_ns)
auth.add_namespace(image_ns)