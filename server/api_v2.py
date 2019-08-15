from flask import Blueprint

v2 = Blueprint('v2', 'v2')


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


@v2.route('/timespan/<lot_id>')
def timespan(lot_id):
    return {
        'data': []
    }
