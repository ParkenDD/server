from flask import Flask

from server.api_v1 import v1
from server.api_v2 import v2

app = Flask(__name__)

app.register_blueprint(v1)
app.register_blueprint(v2, url_prefix='/v2')
app.run('0.0.0.0', '8080', debug=True)
