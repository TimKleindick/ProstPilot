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
    id: int


class Container(GeneralManager):
    name: str
    icon: str
    size_list: Bucket[Size]

    _data: list[container] = [
        {"id": 1, "name": "Flasche", "icon": "mdi:bottle"},
        {"id": 2, "name": "Dose", "icon": "mdi:can"},
        {"id": 3, "name": "Becher", "icon": "mdi:cup"},
        {"id": 4, "name": "Shotglas", "icon": "mdi:shot"},
        {"id": 5, "name": "Weinglas", "icon": "mdi:glass-wine"},
        {"id": 6, "name": "Sektglas", "icon": "mdi:glass-champagne"},
        {"id": 7, "name": "Bierglas", "icon": "mdi:glass-mug"},
        {"id": 8, "name": "Bierkrug", "icon": "mdi:beer"},
    ]

    class Interface(ReadOnlyInterface):
        name: ClassVar[models.CharField] = models.CharField(
            max_length=100,
            unique=True,
        )
        icon: ClassVar[models.CharField] = models.CharField(max_length=100)


class size(TypedDict):
    container: dict[str, int]
    volume: str


class Size(GeneralManager):
    container: Container
    volume: Measurement
    drink_list: Bucket[Drink]

    _data: list[size] = [
        {"container": {"id": 1}, "volume": "330 milliliter"},
        {"container": {"id": 1}, "volume": "500 milliliter"},
        {"container": {"id": 1}, "volume": "1000 milliliter"},
        {"container": {"id": 2}, "volume": "330 milliliter"},
        {"container": {"id": 2}, "volume": "500 milliliter"},
        {"container": {"id": 3}, "volume": "200 milliliter"},
        {"container": {"id": 3}, "volume": "400 milliliter"},
        {"container": {"id": 4}, "volume": "40 milliliter"},
        {"container": {"id": 5}, "volume": "150 milliliter"},
        {"container": {"id": 6}, "volume": "120 milliliter"},
        {"container": {"id": 7}, "volume": "300 milliliter"},
        {"container": {"id": 7}, "volume": "500 milliliter"},
        {"container": {"id": 8}, "volume": "500 milliliter"},
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
