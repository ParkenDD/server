from flask import Flask

from server import api_v2

app = Flask(__name__)

app.register_blueprint(api_v2.v2, url_prefix='/v2')
app.run('0.0.0.0', '8080', debug=True)
