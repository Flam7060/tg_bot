import asyncio
from aiogram import Bot
from app.bot.create_bot import dp
from app.bot.handlers import horoscope, get_cat, get_dog
from app.config import configs


bot = Bot(token=configs.telegram.bot_token.get_secret_value())


async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)

        print("Bot worked")
        await dp.start_polling(bot)
    finally:

        await bot.session.close()



if __name__ == "__main__":
    print()
    asyncio.run(main())
