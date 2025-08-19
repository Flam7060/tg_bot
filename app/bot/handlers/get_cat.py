from aiogram import F
from aiogram.types import Message, URLInputFile
from app.bot.create_bot import dp
from app.config import configs
from app.services.get_animals.get_cat import CatApiClient


Cats_Words = ["киса", "кису", "кота", "котика", "котик", "киску"]
Names_Bot = ["леха", "алексей"]


def contains_bot_and_cat(text: str) -> bool:
    text_lower = text.lower()
    bot_in_text = any(name.lower() in text_lower for name in Names_Bot)
    cat_in_text = any(cat_word.lower() in text_lower for cat_word in Cats_Words)
    return bot_in_text and cat_in_text


@dp.message(F.text.func(contains_bot_and_cat))
async def get_cat_handler(message: Message):
    cat = CatApiClient(configs.cat.base_url, configs.cat.api_key.get_secret_value())
    try:
        cat_info = cat.get_cat()
        print(cat_info, flush=True)
        if cat_info is None:
            await message.answer("Не удалось получить изображение кота 😿")
            return

        # Отправляем изображение по URL
        print(cat_info.url, flush=True)
        photo = URLInputFile(cat_info.url)
        await message.answer_photo(photo, caption="Вот твой котик! 🐱")

    except Exception as e:
        print(e, flush=True)
        await message.answer("Произошла ошибка при получении изображения кота 😿")
