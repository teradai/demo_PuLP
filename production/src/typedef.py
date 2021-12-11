import typing

class Item(typing.TypedDict):
    name: str
    job: list[int]
    profit: int


class ResultItem(typing.TypedDict):
    name: str
    value: int

class Result(typing.TypedDict):
    status: str
    objective_value: float
    items: list[ResultItem]
