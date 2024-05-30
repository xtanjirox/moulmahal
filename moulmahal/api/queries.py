from ninja import Schema
from typing import List
from core import models


class ClientQuery(Schema):
    client_name: List[str]
    client_phone: List[str]
    client_address: List[str]
