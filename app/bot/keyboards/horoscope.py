from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.services.astrology.schemas import ZodiacSign

RUSSIAN_ZODIAC_NAMES = {
    ZodiacSign.aries: "Овен",
    ZodiacSign.taurus: "Телец",
    ZodiacSign.gemini: "Близнецы",
    ZodiacSign.cancer: "Рак",
    ZodiacSign.leo: "Лев",
    ZodiacSign.virgo: "Дева",
    ZodiacSign.libra: "Весы",
    ZodiacSign.scorpio: "Скорпион",
    ZodiacSign.sagittarius: "Стрелец",
    ZodiacSign.capricorn: "Козерог",
    ZodiacSign.aquarius: "Водолей",
    ZodiacSign.pisces: "Рыбы",
}


def zodiac_keyboard():
    buttons = []
    signs = list(ZodiacSign)
    # создаём ряды по 3 кнопки
    for i in range(0, len(signs), 3):
        row = [
            InlineKeyboardButton(
                text=RUSSIAN_ZODIAC_NAMES[sign],
                callback_data=f"zodiac_{sign.value.lower()}",
            )
            for sign in signs[i : i + 3]
        ]
        buttons.append(row)
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
