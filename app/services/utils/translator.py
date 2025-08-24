from functools import wraps

from deep_translator import GoogleTranslator


def translate_text(text: str, target_lang="en", source_lang="auto") -> str:
    """
    Функция перевода текста с помощью deep_translator.
    :param text: исходный текст
    :param target_lang: язык перевода
    :param source_lang: исходный язык
    :return: переведённый текст или оригинал при ошибке
    """
    if not isinstance(text, str):
        return text  # переводим только строки
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text


def translate_output(target_lang="en", source_lang="auto"):
    """
    Декоратор для перевода строкового результата функции на целевой язык.
    :param target_lang: язык перевода (например, 'en', 'ru', 'fr' и т.д.)
    :param source_lang: исходный язык (по умолчанию 'auto')
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return translate_text(result, target_lang=target_lang, source_lang=source_lang)

        return wrapper

    return decorator
