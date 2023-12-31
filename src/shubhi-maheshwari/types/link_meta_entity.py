# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class LinkMetaEntity(pydantic.BaseModel):
    notify_url: typing.Optional[str] = pydantic.Field(
        description=("Notification URL for server-server communication. It should be an https URL.\n")
    )
    upi_intent: typing.Optional[bool] = pydantic.Field(
        description=('If "true", link will directly open UPI Intent flow on mobile, and normal link flow elsewhere\n')
    )
    return_url: typing.Optional[str] = pydantic.Field(
        description=(
            "The URL to which user will be redirected to after the payment is done on the link. Maximum length: 250.\n"
        )
    )
    payment_methods: typing.Optional[str] = pydantic.Field(
        description=(
            'Allowed payment modes for this link. Pass comma-separated values among following options - "cc", "dc", "ccc", "ppc", "nb", "upi", "paypal", "app". Leave it blank to show all available payment methods\n'
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
