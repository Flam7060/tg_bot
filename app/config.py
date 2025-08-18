from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


# docs
# https://habr.com/ru/articles/866536/
# https://docs.pydantic.dev/latest/concepts/pydantic_settings/
# https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretStr


env_path = Path(__file__).parent.parent / ".env"


class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(env_path), env_file_encoding="utf-8", extra="ignore"
    )


class TelegramConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="tg_")

    bot_token: SecretStr


class ApiNinjasConfig(ConfigBase):
    """
    Колекция различных api для различных задач
    """

    model_config = SettingsConfigDict(env_prefix="ninja_")
    base_url: str = "https://api.api-ninjas.com/v1"
    api_key: SecretStr


class ThecatapiConfig(ConfigBase):
    """
    Апи с котиками!!
    """

    model_config = SettingsConfigDict(env_prefix="thecat_")
    base_url: str = "https://api.thecatapi.com/v1/"
    api_key: SecretStr


3


class Config(BaseSettings):
    telegram: TelegramConfig = Field(default_factory=TelegramConfig)
    ninja: ApiNinjasConfig = Field(default_factory=ApiNinjasConfig)
    cat: ThecatapiConfig = Field(default_factory=ThecatapiConfig)

    @classmethod
    def load(cls) -> "Config":
        return cls()


configs = Config()
