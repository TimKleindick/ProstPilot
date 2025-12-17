from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, TypedDict

from django.db import models
from general_manager import GeneralManager
from general_manager.interface import DatabaseInterface, ReadOnlyInterface
from general_manager.measurement import Measurement, MeasurementField

if TYPE_CHECKING:
    from .beverage import Beverage
    from catalog.models.container import Size, size


class Price(GeneralManager):
    beverage: Beverage
    supermarket: Supermarket
    last_updated: datetime
    price_per_unit: Measurement
    packaging: Packaging

    class Interface(DatabaseInterface):
        beverage = models.ForeignKey(
            "shopping.Beverage",
            on_delete=models.CASCADE,
            related_name="prices",
        )
        supermarket = models.ForeignKey(
            "Supermarket",
            on_delete=models.CASCADE,
            related_name="prices",
        )
        last_updated = models.DateTimeField(auto_now=True)
        price_per_unit = MeasurementField("EUR")
        packaging = models.ForeignKey(
            "Packaging",
            on_delete=models.PROTECT,
            related_name="prices",
        )


class Supermarket(GeneralManager):
    name: str
    location: str

    class Interface(DatabaseInterface):
        name = models.CharField(max_length=150, unique=True)
        location = models.CharField(max_length=255)


class packaging(TypedDict):
    type: str
    total_volume: str
    basis_size: size


class Packaging(GeneralManager):
    type: str
    total_volume: Measurement
    basis_size: Size

    _data: list[packaging] = [
        {
            "type": "Einzelflasche 0.33l",
            "total_volume": "330 milliliter",
            "basis_size": {"container": "Flasche", "volume": "330 milliliter"},
        },
        {
            "type": "Einzelflasche 0.5l",
            "total_volume": "500 milliliter",
            "basis_size": {"container": "Flasche", "volume": "500 milliliter"},
        },
        {
            "type": "Einzeldose 0.33l",
            "total_volume": "330 milliliter",
            "basis_size": {"container": "Dose", "volume": "330 milliliter"},
        },
        {
            "type": "Einzeldose 0.5l",
            "total_volume": "500 milliliter",
            "basis_size": {"container": "Dose", "volume": "500 milliliter"},
        },
        {
            "type": "Dosen Palette 24x0.33l",
            "total_volume": "7920 milliliter",
            "basis_size": {"container": "Dose", "volume": "330 milliliter"},
        },
        {
            "type": "Dosen Palette 24x0.5l",
            "total_volume": "12000 milliliter",
            "basis_size": {"container": "Dose", "volume": "500 milliliter"},
        },
        {
            "type": "Karton 1l",
            "total_volume": "1000 milliliter",
            "basis_size": {"container": "Flasche", "volume": "1000 milliliter"},
        },
        {
            "type": "Sixpack 6x0.33l",
            "total_volume": "1980 milliliter",
            "basis_size": {"container": "Flasche", "volume": "330 milliliter"},
        },
        {
            "type": "Sixpack 6x0.5l",
            "total_volume": "3000 milliliter",
            "basis_size": {"container": "Flasche", "volume": "500 milliliter"},
        },
        {
            "type": "Kasten 12x1l",
            "total_volume": "12000 milliliter",
            "basis_size": {"container": "Flasche", "volume": "1000 milliliter"},
        },
        {
            "type": "Kasten 20x0.5l",
            "total_volume": "10000 milliliter",
            "basis_size": {"container": "Flasche", "volume": "500 milliliter"},
        },
        {
            "type": "Kasten 24x0.33l",
            "total_volume": "7920 milliliter",
            "basis_size": {"container": "Flasche", "volume": "330 milliliter"},
        },
    ]

    class Interface(ReadOnlyInterface):
        type = models.CharField(max_length=100, unique=True)
        total_volume = MeasurementField("milliliter")
        basis_size = models.ForeignKey(
            "catalog.Size",
            on_delete=models.CASCADE,
        )
