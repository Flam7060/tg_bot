import re
from aiogram import F, Router
from aiogram.types import Message

router = Router()

# Обновленное регулярное выражение
pin_link_pattern = re.compile(r"https?://(?:www\.)?pin\.it/\S+", re.IGNORECASE)


@router.message(F.text)
async def handle_pinterest_short_link(message: Message):
    found_links = pin_link_pattern.findall(message.text)
    for link in found_links:
        await message.answer(f"Обнаружена ссылка Pinterest: {link}")
