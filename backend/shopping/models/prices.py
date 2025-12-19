from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, ClassVar, TypedDict

from django.db import models
from general_manager import GeneralManager
from general_manager.interface import DatabaseInterface, ReadOnlyInterface
from general_manager.measurement import Measurement, MeasurementField

if TYPE_CHECKING:
    from catalog.models.container import Size

    from .beverage import Beverage


class Price(GeneralManager):
    beverage: Beverage
    supermarket: Supermarket
    last_updated: datetime
    price_per_unit: Measurement
    packaging: Packaging

    class Interface(DatabaseInterface):
        beverage: ClassVar[models.ForeignKey] = models.ForeignKey(
            "shopping.Beverage",
            on_delete=models.CASCADE,
            related_name="prices",
        )
        supermarket: ClassVar[models.ForeignKey] = models.ForeignKey(
            "Supermarket",
            on_delete=models.CASCADE,
            related_name="prices",
        )
        last_updated: ClassVar[models.DateTimeField] = models.DateTimeField(
            auto_now=True,
        )
        price_per_unit: ClassVar[MeasurementField] = MeasurementField("EUR")
        packaging: ClassVar[models.ForeignKey] = models.ForeignKey(
            "Packaging",
            on_delete=models.PROTECT,
            related_name="prices",
        )


class Supermarket(GeneralManager):
    name: str
    location: str

    class Interface(DatabaseInterface):
        name: ClassVar[models.CharField] = models.CharField(
            max_length=150,
            unique=True,
        )
        location: ClassVar[models.CharField] = models.CharField(max_length=255)


class packaging(TypedDict):
    type: str
    total_volume: str
    basis_size: basisSize


class basisSize(TypedDict):
    container_id: int
    volume: str


class Packaging(GeneralManager):
    type: str
    total_volume: Measurement
    basis_size: Size

    _data: list[packaging] = [
        {
            "type": "Einzelflasche 0.33l",
            "total_volume": "330 milliliter",
            "basis_size": {"container_id": 1, "volume": "330 milliliter"},
        },
        {
            "type": "Einzelflasche 0.5l",
            "total_volume": "500 milliliter",
            "basis_size": {"container_id": 1, "volume": "500 milliliter"},
        },
        {
            "type": "Einzeldose 0.33l",
            "total_volume": "330 milliliter",
            "basis_size": {"container_id": 2, "volume": "330 milliliter"},
        },
        {
            "type": "Einzeldose 0.5l",
            "total_volume": "500 milliliter",
            "basis_size": {"container_id": 2, "volume": "500 milliliter"},
        },
        {
            "type": "Dosen Palette 24x0.33l",
            "total_volume": "7920 milliliter",
            "basis_size": {"container_id": 2, "volume": "330 milliliter"},
        },
        {
            "type": "Dosen Palette 24x0.5l",
            "total_volume": "12000 milliliter",
            "basis_size": {"container_id": 2, "volume": "500 milliliter"},
        },
        {
            "type": "Karton 1l",
            "total_volume": "1000 milliliter",
            "basis_size": {"container_id": 1, "volume": "1000 milliliter"},
        },
        {
            "type": "Sixpack 6x0.33l",
            "total_volume": "1980 milliliter",
            "basis_size": {"container_id": 1, "volume": "330 milliliter"},
        },
        {
            "type": "Sixpack 6x0.5l",
            "total_volume": "3000 milliliter",
            "basis_size": {"container_id": 1, "volume": "500 milliliter"},
        },
        {
            "type": "Kasten 12x1l",
            "total_volume": "12000 milliliter",
            "basis_size": {"container_id": 1, "volume": "1000 milliliter"},
        },
        {
            "type": "Kasten 20x0.5l",
            "total_volume": "10000 milliliter",
            "basis_size": {"container_id": 1, "volume": "500 milliliter"},
        },
        {
            "type": "Kasten 24x0.33l",
            "total_volume": "7920 milliliter",
            "basis_size": {"container_id": 1, "volume": "330 milliliter"},
        },
    ]

    class Interface(ReadOnlyInterface):
        type: ClassVar[models.CharField] = models.CharField(
            max_length=100,
            unique=True,
        )
        total_volume: ClassVar[MeasurementField] = MeasurementField("milliliter")
        basis_size: ClassVar[models.ForeignKey] = models.ForeignKey(
            "catalog.Size",
            on_delete=models.CASCADE,
        )
