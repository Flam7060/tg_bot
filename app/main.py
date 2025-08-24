import asyncio
from app.config import configs
from app.bot.create_bot import create_bot


if __name__ == "__main__":
    print()
    asyncio.run(create_bot(configs.telegram.bot_token.get_secret_value()))
