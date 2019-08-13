from flask import Blueprint

from .db.db import *

v2 = Blueprint('v2', __name__)


@v2.route('/pools')
def pools():
    return {
        'api_version': 2.0,
        'pools': []
    }


@v2.route('/pool/<pool_name>')
def pool(pool_name):
    return {
        'pool': pool_name,
        'lots': []
    }
