"""Run from the project root with `python -m backend.main`."""

import os

from backend.app.main import app


if __name__ == "__main__":
    import uvicorn

    production = "PORT" in os.environ
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0" if production else "127.0.0.1",
        port=int(os.environ.get("PORT", "8000")),
        reload=not production,
    )
