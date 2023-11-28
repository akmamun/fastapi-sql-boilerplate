from config.db import db_config
from dotenv import load_dotenv

load_dotenv()

def config():
    return dict(
        **db_config()
    )