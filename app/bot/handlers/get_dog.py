from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, URLInputFile
from app.config import configs
from app.services.get_animals.get_dog import DogApiClient

router = Router()


@router.message(Command("get_dog"))
async def get_dog_handler(message: Message):
    dog = DogApiClient(configs.dog.base_url, configs.dog.api_key.get_secret_value())
    try:
        dog_info = dog.get_dog()
        print(dog_info, flush=True)
        if dog_info is None:
            await message.answer("Не удалось получить изображение собаки")
            return

        # Отправляем изображение по URL
        print(dog_info.url, flush=True)
        photo = URLInputFile(dog_info.url)
        await message.answer_photo(photo, caption="Вот твоя песа!")

    except Exception as e:
        print(e, flush=True)
        await message.answer("Произошла ошибка при получении изображения песы")
