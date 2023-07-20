# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .offer_details import OfferDetails
from .offer_meta import OfferMeta
from .offer_tnc import OfferTnc
from .offer_validations import OfferValidations


class OfferEntity(pydantic.BaseModel):
    offer_id: typing.Optional[int]
    offer_status: typing.Optional[str]
    offer_meta: typing.Optional[OfferMeta]
    offer_tnc: typing.Optional[OfferTnc]
    offer_details: typing.Optional[OfferDetails]
    offer_validations: typing.Optional[OfferValidations]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
