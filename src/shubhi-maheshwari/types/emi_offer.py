# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .tenures_array import TenuresArray


class EmiOffer(pydantic.BaseModel):
    type: str = pydantic.Field(
        description=(
            'Type of emi offer. Possible values are `credit_card_emi`, `debit_card_emi`, `cardless_emi` <span style="white-space: nowrap">`<= 100 characters`</span> \n'
        )
    )
    bank_name: str = pydantic.Field(
        description=('Bank Name <span style="white-space: nowrap">`<= 100 characters`</span> \n')
    )
    tenures: typing.Optional[typing.List[TenuresArray]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}