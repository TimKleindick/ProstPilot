from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models
from general_manager import GeneralManager
from general_manager.bucket import Bucket
from general_manager.interface import DatabaseInterface

if TYPE_CHECKING:
    from catalog.models.container import Size


class BeverageType(GeneralManager):
    name: str
    default_brand: Brand
    beverage_list: Bucket[Beverage]

    class Interface(DatabaseInterface):
        name = models.CharField(max_length=100, unique=True)
        default_brand = models.ForeignKey(
            "Brand",
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            related_name="default_for_types",
        )


class Brand(GeneralManager):
    name: str
    icon: str
    default_for_types_list: Bucket[BeverageType]
    beverage_list: Bucket[Beverage]

    class Interface(DatabaseInterface):
        name = models.CharField(max_length=150, unique=True)
        icon = models.CharField(max_length=150)


class Beverage(GeneralManager):
    drink_type: BeverageType
    size: Size
    brand: Brand

    class Interface(DatabaseInterface):
        drink_type = models.ForeignKey(
            "BeverageType",
            on_delete=models.CASCADE,
            related_name="beverages",
        )
        size = models.ForeignKey(
            "catalog.Size",
            on_delete=models.CASCADE,
            related_name="beverages",
        )
        brand = models.ForeignKey(
            "Brand",
            on_delete=models.CASCADE,
            related_name="beverages",
        )
