from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models
from general_manager import GeneralManager
from general_manager.bucket import Bucket
from general_manager.interface import DatabaseInterface
from general_manager.measurement import Measurement, MeasurementField

if TYPE_CHECKING:
    from catalog.models.container import Size
    from shopping.models.beverage import BeverageType


class Ingredient(GeneralManager):
    beverage_type: BeverageType
    default_quantity: Measurement

    class Interface(DatabaseInterface):
        beverage_type = models.ForeignKey(
            "shopping.BeverageType",
            on_delete=models.CASCADE,
        )
        default_quantity = MeasurementField("milliliter")


class Recipe(GeneralManager):
    name: str
    possible_size_list: Bucket[Size]
    ingredient_list: Bucket[Ingredient]

    class Interface(DatabaseInterface):
        name = models.CharField(max_length=255)
