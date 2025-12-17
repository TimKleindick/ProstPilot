from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, TypedDict

from django.db import models
from general_manager import GeneralManager
from general_manager.bucket import Bucket
from general_manager.interface import ReadOnlyInterface
from general_manager.measurement import Measurement, MeasurementField

if TYPE_CHECKING:
    from .drinks import Drink


class container(TypedDict):
    name: str
    icon: str


class Container(GeneralManager):
    name: str
    icon: str
    size_list: Bucket[Size]

    _data: list[container] = [
        {"name": "Flasche", "icon": "mdi:bottle"},
        {"name": "Dose", "icon": "mdi:can"},
        {"name": "Becher", "icon": "mdi:cup"},
        {"name": "Shotglas", "icon": "mdi:shot"},
        {"name": "Weinglas", "icon": "mdi:glass-wine"},
        {"name": "Sektglas", "icon": "mdi:glass-champagne"},
        {"name": "Bierglas", "icon": "mdi:glass-mug"},
        {"name": "Bierkrug", "icon": "mdi:beer"},
    ]

    class Interface(ReadOnlyInterface):
        name: ClassVar[models.CharField] = models.CharField(
            max_length=100,
            unique=True,
        )
        icon: ClassVar[models.CharField] = models.CharField(max_length=100)


class size(TypedDict):
    container: str
    volume: str


class Size(GeneralManager):
    container: Container
    volume: Measurement
    drink_list: Bucket[Drink]

    _data: list[size] = [
        {"container": "Flasche", "volume": "330 milliliter"},
        {"container": "Flasche", "volume": "500 milliliter"},
        {"container": "Dose", "volume": "330 milliliter"},
        {"container": "Dose", "volume": "500 milliliter"},
        {"container": "Becher", "volume": "200 milliliter"},
        {"container": "Becher", "volume": "400 milliliter"},
        {"container": "Shotglas", "volume": "40 milliliter"},
        {"container": "Weinglas", "volume": "150 milliliter"},
        {"container": "Sektglas", "volume": "120 milliliter"},
        {"container": "Bierglas", "volume": "300 milliliter"},
        {"container": "Bierglas", "volume": "500 milliliter"},
        {"container": "Bierkrug", "volume": "500 milliliter"},
    ]

    class Interface(ReadOnlyInterface):
        container: ClassVar[models.ForeignKey] = models.ForeignKey(
            "Container",
            on_delete=models.CASCADE,
        )
        volume: ClassVar[MeasurementField] = MeasurementField("milliliter")

        class Meta:
            constraints = [
                models.UniqueConstraint(
                    fields=["container", "volume"],
                    name="unique_container_volume",
                )
            ]
