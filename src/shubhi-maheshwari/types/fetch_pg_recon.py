# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .fetch_pg_recon_data_item import FetchPgReconDataItem


class FetchPgRecon(pydantic.BaseModel):
    cursor: typing.Optional[str] = pydantic.Field(
        description=("Specifies from where the next set of settlement details should be fetched.\n")
    )
    limit: typing.Optional[int] = pydantic.Field(
        description=("Number of settlements you want to fetch in the next iteration.\n")
    )
    data: typing.Optional[typing.List[FetchPgReconDataItem]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}