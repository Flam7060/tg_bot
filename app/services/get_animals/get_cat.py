from app.services.base_api import BaseApiClient
from app.services.get_animals.schemas.cat_schema import CatInfo
from pydantic import ValidationError


class CatApiClient(BaseApiClient):
    def __init__(self, base_url: str, api_key: str):
        headers = {"X-Api-Key": api_key}
        super().__init__(base_url=base_url, headers=headers)

    def get_cat(self) -> CatInfo | None:
        response = self.get("images/search")
        if response is None:
            return None

        try:
            return CatInfo.model_validate(response.json()[0])
        except (ValidationError, ValueError, IndexError, KeyError):
            return None
