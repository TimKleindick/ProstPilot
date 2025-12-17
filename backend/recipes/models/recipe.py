from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

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
        beverage_type: ClassVar[models.ForeignKey] = models.ForeignKey(
            "shopping.BeverageType",
            on_delete=models.CASCADE,
        )
        default_quantity: ClassVar[MeasurementField] = MeasurementField(
            "milliliter",
        )


class Recipe(GeneralManager):
    name: str
    possible_size_list: Bucket[Size]
    ingredient_list: Bucket[Ingredient]

    class Interface(DatabaseInterface):
        name: ClassVar[models.CharField] = models.CharField(max_length=255)
