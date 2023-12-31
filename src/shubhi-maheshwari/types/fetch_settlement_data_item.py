# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class FetchSettlementDataItem(pydantic.BaseModel):
    event_type: typing.Optional[str] = pydantic.Field(description=("Event type is SETTLEMENT.\n"))
    cf_settlement_id: typing.Optional[int] = pydantic.Field(description=("Unique ID to identify the settlement.\n"))
    status: typing.Optional[str] = pydantic.Field(description=("Status of the settlement.\n"))
    settlement_date: typing.Optional[str] = pydantic.Field(
        description=("Date and time when the settlement was processed.\n")
    )
    payment_amount: typing.Optional[float] = pydantic.Field(description=("Amount captured.\n"))
    settlement_utr: typing.Optional[str] = pydantic.Field(
        description=("Unique transaction reference number of the payment.\n")
    )
    adjustment: typing.Optional[float] = pydantic.Field(
        description=("Amount that is adjusted from the settlement amount.\n")
    )
    service_tax: typing.Optional[float] = pydantic.Field(description=("Service tax applicable on settlement.\n"))
    service_charge: typing.Optional[float] = pydantic.Field(description=("Service charge applicable on settlement.\n"))
    amount_settled: typing.Optional[float] = pydantic.Field(
        description=(
            "Net amount that is settled after deducting the settlement charges and tax. (Settlement charges and tax is applicable for instant and on demand settlements.)\n"
        )
    )
    payment_from: typing.Optional[str] = pydantic.Field(description=("The start time of time range of settlement.\n"))
    payment_till: typing.Optional[str] = pydantic.Field(description=("The end time of time range of settlement\n"))
    reason: typing.Optional[str] = pydantic.Field(description=("Reason for failure.\n"))
    settlement_initiated_on: typing.Optional[str] = pydantic.Field(description=("Settlement initiation time.\n"))
    settlement_type: typing.Optional[str] = pydantic.Field(description=("Settlement type.\n"))
    settlement_charge: typing.Optional[float] = pydantic.Field(
        description=("Settlement tax applicable on settlement.\n")
    )
    settlement_tax: typing.Optional[float] = pydantic.Field(
        description=("Settlement charge applicable on settlement.\n")
    )
    remarks: typing.Optional[str] = pydantic.Field(description=("Remarks on the settlement.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
