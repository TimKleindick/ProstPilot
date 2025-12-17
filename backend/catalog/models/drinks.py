from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, TypedDict

from django.db import models
from general_manager import GeneralManager
from general_manager.bucket import Bucket
from general_manager.interface import DatabaseInterface, ReadOnlyInterface

if TYPE_CHECKING:
    from .container import Size


class drinkCategory(TypedDict):
    name: str
    description: str


class DrinkCategory(GeneralManager):
    name: str
    description: str

    _data: list[drinkCategory] = [
        {
            "name": "Soft-Drink",
            "description": "Nicht alkoholische Erfrischungsgetränke",
        },
        {
            "name": "Bier",
            "description": "Gebraute alkoholische Getränke aus Getreide",
        },
        {
            "name": "Wein",
            "description": "Gärung von Trauben oder anderen Früchten",
        },
        {
            "name": "Cocktail",
            "description": "Gemischte alkoholische Getränke, oft mit Säften oder Sirupen",
        },
        {
            "name": "Schaumwein",
            "description": "Perlend und sprudelnd, oft aus Trauben hergestellt",
        },
        {
            "name": "Shots",
            "description": "Kleine Mengen hochprozentiger Spirituosen",
        },
        {
            "name": "Long-Drink",
            "description": "Alkoholische Mischgetränke, die in großen Gläsern serviert werden",
        },
    ]

    class Interface(ReadOnlyInterface):
        name: ClassVar[models.CharField] = models.CharField(
            max_length=100,
            unique=True,
        )
        description: ClassVar[models.TextField] = models.TextField()


class Drink(GeneralManager):
    size: Size
    drink_group: DrinkGroup

    class Interface(DatabaseInterface):
        size: ClassVar[models.ForeignKey] = models.ForeignKey(
            "Size",
            on_delete=models.CASCADE,
        )
        drink_group: ClassVar[models.ForeignKey] = models.ForeignKey(
            "DrinkGroup",
            on_delete=models.CASCADE,
        )


class DrinkGroup(GeneralManager):
    name: str
    icon: str
    drink_category: DrinkCategory
    drink_list: Bucket[Drink]

    class Interface(DatabaseInterface):
        name: ClassVar[models.CharField] = models.CharField(max_length=100)
        icon: ClassVar[models.CharField] = models.CharField(max_length=100)
        drink_category: ClassVar[models.ForeignKey] = models.ForeignKey(
            "DrinkCategory",
            on_delete=models.CASCADE,
        )
