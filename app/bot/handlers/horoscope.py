from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from app.bot.create_bot import dp
from app.bot.keyboards.horoscope import zodiac_keyboard
from app.config import configs
from app.services.astrology.schemas import ZodiacSign
from app.services.astrology.horoscope import HoroscopeApiClient
from app.services.utils.translator import translate_text


@dp.message(Command("horoscop"))
async def get_horoscope(message: Message):
    user_mention = message.from_user.first_name
    print(user_mention)
    text = (
        f"🌊 Сегодня волны энергии особенно сильны, {user_mention}! 🌊\n\n"
        "Выбери свой знак зодиака, чтобы узнать, какие тайные силы сопровождают тебя."
    )
    keyboard = zodiac_keyboard()
    await message.answer(text, reply_markup=keyboard)


@dp.callback_query(lambda c: c.data and c.data.startswith("zodiac_"))
async def zodiac_button_handler(callback_query: CallbackQuery):
    sign_str = callback_query.data.split("_")[1]
    sign = ZodiacSign(sign_str.capitalize())
    horoscop = HoroscopeApiClient(
        configs.ninja.base_url, configs.ninja.api_key.get_secret_value()
    )
    horoscope_response = horoscop.get_horoscope(sign)
    if horoscope_response is not None:
        translated_text = translate_text(horoscope_response.horoscope, target_lang="ru")
        answer_text = f"Гороскоп на сегодня для {sign.value}:\n\n{translated_text}"
    else:
        answer_text = "К сожалению, гороскоп не получен. Попробуйте позже."

    await callback_query.message.answer(answer_text)
    await callback_query.answer()
