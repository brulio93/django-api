from flask import Blueprint
from api import geeksApi
from . import views

auth_blueprint = Blueprint('auth', __name__)


def create_app(config_name):
    @geeksApi.route('/appointments/<ind:id>', methods=['GET','PUT','DELETE'])
    def appointments_manipulation(id, **kwargs):
        return id

    from ..auth import auth_blueprint
    geeksApi.register_blueprint(auth_blueprint)

    return geeksApi
