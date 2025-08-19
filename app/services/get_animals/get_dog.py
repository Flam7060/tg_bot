from pydantic import ValidationError
from app.services.get_animals.schemas.dog_schema import DogInfo
from app.services.base_api import BaseApiClient


class DogApiClient(BaseApiClient):
    def __init__(self, base_url: str, api_key: str):
        headers = {"X-Api-Key": api_key}
        super().__init__(base_url=base_url, headers=headers)

    def get_dog(self) -> DogInfo | None:
        response = self.get("images/search")
        if response is None:
            return None

        try:
            return DogInfo.model_validate(response.json()[0])
        except (ValidationError, ValueError, IndexError, KeyError):
            return None
