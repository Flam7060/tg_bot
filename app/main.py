import asyncio
from aiogram import Bot
from app.bot.create_bot import dp
from app.config import Config
from app.bot.handlers import horoscope


configs = Config()

bot = Bot(token=configs.telegram.bot_token.get_secret_value())


async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        
        print("Бот запускается...")
        await dp.start_polling(bot)
    finally:
        print("Бот начинает закрыватьсяч...")
        await bot.session.close()
        print("Бот закрывается ...")


if __name__ == "__main__":
    print(configs.telegram.bot_token)
    asyncio.run(main())
