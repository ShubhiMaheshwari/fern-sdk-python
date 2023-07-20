# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .offer_tnc_offer_tnc_type import OfferTncOfferTncType


class OfferTnc(pydantic.BaseModel):
    offer_tnc_type: OfferTncOfferTncType = pydantic.Field(
        description=("TnC Type for the Offer. It can be either `text` or `link`\n")
    )
    offer_tnc_value: str = pydantic.Field(
        description=('TnC for the Offer. <span style="white-space: nowrap">`<= 100 characters`</span> \n')
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