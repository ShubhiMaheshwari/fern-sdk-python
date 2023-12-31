# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class FetchSettlementReconRequestFilters(pydantic.BaseModel):
    """
    Specify either the Settlement ID, Settlement UTR, or start date and end date to fetch the settlement details.
    """

    cf_settlement_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        description=("List of settlement IDs for which you want the settlement reconciliation details.\n")
    )
    settlement_utrs: typing.Optional[typing.List[str]] = pydantic.Field(
        description=("List of settlement UTRs for which you want the settlement reconciliation details.\n")
    )
    start_date: typing.Optional[str] = pydantic.Field(
        description=("Specify the start date from when you want the settlement reconciliation details.\n")
    )
    end_date: typing.Optional[str] = pydantic.Field(
        description=("Specify the end date till when you want the settlement reconciliation details.\n")
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
