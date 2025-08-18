from pydantic import BaseModel, AnyUrl

# Example {'breeds': [], 'id': '2oe', 'url': 'https://cdn2.thecatapi.com/images/2oe.jpg', 'width': 500, 'height': 332}


class Cat_info(BaseModel):
    id: str  # Тут каой то прикол с id, что то похожее на uuid, но не оно 'id': '2oe'
    breeds: list  # Порода
    url: str
    width: int
    height: int
