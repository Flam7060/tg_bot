from aiogram import Bot, Dispatcher
from app.bot.handlers import router_get_cat, router_get_dog, router_horoscope


async def create_bot(bot_token: str):
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_routers(router_horoscope, router_get_dog, router_get_cat)
    print("Bot worked", flush=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
