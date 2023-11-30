

from helpers.env import env


def http():
    return {
        'http': {
            'host': env('HTTP_HOST', '0.0.0.0'),
            'port': env('HTTP_PORT', 8000),
            'websocket-path': env('WEBSOCKET_PATH', '/emitter'),
        }
    }