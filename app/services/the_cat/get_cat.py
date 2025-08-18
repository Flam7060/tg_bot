from pydantic import ValidationError
from app.services.the_cat.schemas import Cat_info
from app.services.base_api import BaseApiClient


class CatApiClient(BaseApiClient):
    def __init__(self, base_url: str, api_key: str):
        headers = {"X-Api-Key": api_key}
        super().__init__(base_url=base_url, headers=headers)

    def get_cat(self) -> Cat_info | None:
        response = self.get("images/search")
        if response is None:
            return None

        try:
            return Cat_info.model_validate(response.json()[0])
        except (ValidationError, ValueError, IndexError, KeyError):
            return None
