from app.bot.handlers.get_cat import router as router_get_cat
from app.bot.handlers.get_dog import router as router_get_dog
from app.bot.handlers.horoscope import router as router_horoscope
from app.bot.handlers.pinterest_to_photo import router as router_pinterest

__all__ = ["router_get_cat", "router_get_dog", "router_horoscope", "router_pinterest"]
