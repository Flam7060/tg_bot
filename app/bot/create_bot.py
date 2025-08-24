from aiogram import Dispatcher, Bot
from app.bot.handlers import router_horoscop, router_get_cat, router_get_dog


async def create_bot(bot_token: str):
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_routers(router_horoscop, router_get_dog, router_get_cat)
    print("Bot worked", flush=1)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
