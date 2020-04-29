from flask import Flask
from flask.blueprints import Blueprint

import config
import routes

server = Flask(__name__)

server.debug = config.DEBUG

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT)
