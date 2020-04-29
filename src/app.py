from flask import Flask
from flask.blueprints import Blueprint

import config
import routes
from util.error_handlers import register_custom_error_handlers

app = Flask(__name__)

app.debug = config.DEBUG
app.config["PROPAGATE_EXCEPTIONS"] = True

register_custom_error_handlers(app)

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)
