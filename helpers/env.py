from typing import Optional

import os

def env(name: str, default: Optional[str] = None) -> str:
    value = os.getenv(name, default)
    return value
