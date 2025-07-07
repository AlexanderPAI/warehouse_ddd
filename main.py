import asyncio
import logging

import uvicorn

from infrastructure.database import create_tables
from interfaces.api.api import app

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


async def main():
    await create_tables()
    config = uvicorn.Config(app=app, host="0.0.0.0", port=8080)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
