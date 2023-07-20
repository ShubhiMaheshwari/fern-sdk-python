# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .offer_validations_payment_method import OfferValidationsPaymentMethod


class OfferValidations(pydantic.BaseModel):
    min_amount: typing.Optional[str] = pydantic.Field(
        description=(
            'Minimum Amount for Offer to be Applicable <span style="white-space: nowrap">`<= 50 characters`</span> \n'
        )
    )
    payment_method: OfferValidationsPaymentMethod
    max_allowed: str = pydantic.Field(
        description=(
            'Maximum amount of Offer that can be availed. <span style="white-space: nowrap">`<= 100 characters`</span> \n'
        )
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
