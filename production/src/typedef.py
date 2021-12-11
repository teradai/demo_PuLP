import typing

class Item(typing.TypedDict):
    name: str
    job: list[int]
    profit: int
    