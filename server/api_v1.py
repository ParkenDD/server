from flask import Blueprint

v1 = Blueprint('v1', 'v1')


@v1.route('/')
def meta():
    return {
        'api_version': '1.0',
        'cities': {},
        'reference': '',
        'server_version': ''
    }


@v1.route('/<city_name>')
def city(city_name):
    return {
        'last_downloaded': '',
        'last_updated': '',
        'lots': []
    }


@v1.route('/<city_name>/<lot_id>/timespan')
def timespan(city_name, lot_id):
    return {
        'version': 1.0,
        'data': {}
    }
