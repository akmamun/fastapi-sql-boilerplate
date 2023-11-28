from helpers.env import env
# from dotenv import load_dotenv

# load_dotenv()


def db_config() -> dict:
    return {
        "db": {
            "default": {
                "url": env("DATABASE_URL"),
                "pool_size": int(env("POOL_SIZE", 200)),
                "max_overflow": int(env("MAX_OVERFLOW", 100)),
                "echo": bool(env("DB_ECHO", False)),
                "future": True,
                "pool_pre_ping": True,
                "pool_use_lifo": True,
            },
            "other_db": {
                "url": env("OTHER_DATABASE_URL"),
                "pool_size": int(env("OTHER_POOL_SIZE", 200)),
                "max_overflow": int(env("OTHER_MAX_OVERFLOW", 100)),
                "echo": bool(env("OTHER_DB_ECHO", False)),
                "future": True,
                "pool_pre_ping": True,
                "pool_use_lifo": True,
            }, }
    }
