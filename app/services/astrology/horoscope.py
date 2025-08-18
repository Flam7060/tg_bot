from typing import Optional
from app.main import configs
from app.services.base_api import BaseApiClient
from app.services.astrology.schemas import HoroscopeResponse, ZodiacSign
from app.services.utils.translator import translate_output, translate_text


class HoroscopeApiClient(BaseApiClient):
    def __init__(self, base_url: str, api_key: str):
        headers = {"X-Api-Key": api_key}
        super().__init__(base_url=base_url, headers=headers)

    def get_horoscope(self, sign: ZodiacSign) -> Optional[HoroscopeResponse]:
        response = self.get("horoscope", params={"zodiac": sign.value.lower()})
        if response is None:
            return None

        try:
            data = response.json()
            return HoroscopeResponse(**data)
        except Exception as e:
            print(f"Ошибка парсинга ответа: {e}")
            return None


if "name" == "__main__":
    horoscop = HoroscopeApiClient(
        configs.ninja.base_url, configs.ninja.api_key.get_secret_value()
    )
    horoscope_response = horoscop.get_horoscope(ZodiacSign.leo)
    if horoscope_response is not None:
        translated_text = translate_text(horoscope_response.horoscope, target_lang="ru")
        print(translated_text)
    else:
        print("Гороскоп не получен")
