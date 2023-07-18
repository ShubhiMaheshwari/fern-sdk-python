# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class CustomerDetails(pydantic.BaseModel):
    """
    The customer details that are necessary. Note that you can pass dummy details if your use case does not require the customer details.
    """

    customer_id: str = pydantic.Field(
        description=(
            'A unique identifier for the customer. Use alphanumeric values only. <span style="white-space: nowrap">`<= 50 characters`</span> \n'
        )
    )
    customer_email: typing.Optional[str] = pydantic.Field(
        description=('Customer email address. <span style="white-space: nowrap">`<= 100 characters`</span> \n')
    )
    customer_phone: str = pydantic.Field(
        description=('Customer phone number. <span style="white-space: nowrap">`<= 10 characters`</span> \n')
    )
    customer_bank_account_number: typing.Optional[str] = pydantic.Field(
        description=(
            'Customer bank account. Required if you want to do a bank account check (TPV) <span style="white-space: nowrap">`<= 20 characters`</span> \n'
        )
    )
    customer_bank_ifsc: typing.Optional[str] = pydantic.Field(
        description=("Customer bank IFSC. Required if you want to do a bank account check (TPV)\n")
    )
    customer_bank_code: typing.Optional[str] = pydantic.Field(
        description=(
            "Customer bank code. Required for net banking payments, if you want to do a bank account check (TPV)\n"
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
