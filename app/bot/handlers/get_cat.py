from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, URLInputFile
from app.config import configs
from app.services.get_animals.get_cat import CatApiClient

router = Router()


@router.message(Command("get_cat"))
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
