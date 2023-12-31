# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions

from ..core.datetime_utils import serialize_datetime
from .fetch_all_saved_instruments_instrument_status import FetchAllSavedInstrumentsInstrumentStatus
from .saved_instrument_meta import SavedInstrumentMeta


class FetchAllSavedInstruments(pydantic.BaseModel):
    customer_id: typing.Optional[str] = pydantic.Field(description=("customer_id for which the instrument was saved\n"))
    afa_reference: typing.Optional[int] = pydantic.Field(
        description=("cf_payment_id of the successful transaction done while saving instrument\n")
    )
    instrument_id: typing.Optional[str] = pydantic.Field(description=("saved instrument id\n"))
    instrument_type: typing.Optional[typing_extensions.Literal["card"]]
    instrument_uid: typing.Optional[str] = pydantic.Field(description=("Unique id for the saved instrument\n"))
    instrument_display: typing.Optional[str] = pydantic.Field(
        description=("masked card number displayed to the customer\n")
    )
    instrument_status: typing.Optional[FetchAllSavedInstrumentsInstrumentStatus] = pydantic.Field(
        description=("Status of the saved instrument.\n")
    )
    created_at: typing.Optional[str] = pydantic.Field(description=("Timestamp at which instrument was saved.\n"))
    instrument_meta: typing.Optional[SavedInstrumentMeta]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
