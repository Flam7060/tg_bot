from datetime import date
from enum import Enum

from pydantic import BaseModel


class ZodiacSign(str, Enum):
    aries = "Aries"
    taurus = "Taurus"
    gemini = "Gemini"
    cancer = "Cancer"
    leo = "Leo"
    virgo = "Virgo"
    libra = "Libra"
    scorpio = "Scorpio"
    sagittarius = "Sagittarius"
    capricorn = "Capricorn"
    aquarius = "Aquarius"
    pisces = "Pisces"


class HoroscopeResponse(BaseModel):
    date: date
    sign: ZodiacSign
    horoscope: str
