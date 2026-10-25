"""Run from the backend directory with `python main.py`."""

import os

from app.main import app


if __name__ == "__main__":
    import uvicorn

    production = "PORT" in os.environ
    uvicorn.run(
        "main:app",
        host="0.0.0.0" if production else "127.0.0.1",
        port=int(os.environ.get("PORT", "8000")),
        reload=not production,
    )
