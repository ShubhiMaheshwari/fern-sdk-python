# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .link_customer_details_entity import LinkCustomerDetailsEntity
from .link_meta_entity import LinkMetaEntity
from .link_notes_entity import LinkNotesEntity
from .link_notify_entity import LinkNotifyEntity


class LinkCancelledResponse(pydantic.BaseModel):
    cf_link_id: typing.Optional[int]
    link_id: typing.Optional[str]
    link_status: typing.Optional[str]
    link_currency: typing.Optional[str]
    link_amount: typing.Optional[float]
    link_amount_paid: typing.Optional[float]
    link_partial_payments: typing.Optional[bool]
    link_minimum_partial_amount: typing.Optional[float]
    link_purpose: typing.Optional[str]
    link_created_at: typing.Optional[str]
    customer_details: typing.Optional[LinkCustomerDetailsEntity]
    link_meta: typing.Optional[LinkMetaEntity]
    link_url: typing.Optional[str]
    link_expiry_time: typing.Optional[str]
    link_notes: typing.Optional[LinkNotesEntity]
    link_auto_reminders: typing.Optional[bool]
    link_notify: typing.Optional[LinkNotifyEntity]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
