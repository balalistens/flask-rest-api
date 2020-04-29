import logging
import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("FLASK_ENV") == "development"
APPLICATION_ROOT = os.getenv("APPLICATION_ROOT", "/api")
HOST = os.getenv("APPLICATION_HOST", "127.0.0.1")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
