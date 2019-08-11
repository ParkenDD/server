from flask import Flask, jsonify

v2 = Flask(__name__)


@v2.route('/v2/pools')
def pools():
    return jsonify({
        'api_version': 2.0,
        'pools': []
    })


v2.run('0.0.0.0', '8080', debug=True)
