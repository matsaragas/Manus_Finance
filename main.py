import asyncio

from app.agent.manus import Manus
from app.logger import logger


async def main():
    agent = await Manus.create()
    try:
        prompt = input("Enter your prompt: ")
        await agent.run(prompt)
    except KeyboardInterrupt:
        logger.warning("Operation Interrupted")
    finally:
        await agent.cleanup()
