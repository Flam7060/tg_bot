from pydantic import BaseModel, AnyUrl


# Example response:
# [
#   {
#     "id": "BJa4kxc4X",
#     "url": "https://cdn.thedogapi.com/images/BJa4kxc4X.jpg",
#     "breeds": []
#   }
# ]


class DogInfo(BaseModel):
    id: str  # Тут каой то прикол с id, что то похожее на uuid, но не оно 'id': '2oe'
    breeds: list  # Порода
    url: str
