# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .card_emi_card_bank_name import CardEmiCardBankName


class CardEmi(pydantic.BaseModel):
    channel: typing.Optional[str] = pydantic.Field(
        description=('The channel for card payments will always be "link"\n')
    )
    card_number: typing.Optional[str] = pydantic.Field(description=("Customer card number.\n"))
    card_holder_name: typing.Optional[str] = pydantic.Field(description=("Customer name mentioned on the card.\n"))
    card_expiry_mm: typing.Optional[str] = pydantic.Field(description=("Card expiry month.\n"))
    card_expiry_yy: typing.Optional[str] = pydantic.Field(description=("Card expiry year.\n"))
    card_cvv: typing.Optional[str] = pydantic.Field(description=("CVV mentioned on the card.\n"))
    card_alias: typing.Optional[str] = pydantic.Field(description=("Card alias as returned by Cashfree Vault API\n"))
    card_bank_name: typing.Optional[CardEmiCardBankName] = pydantic.Field(
        description=(
            'Card bank name, required for EMI payments. This is the bank user has selected for EMI. One of ["hdfc, "kotak", "icici", "rbl", "bob", "standard chartered", "axis", "au", "yes", "sbi", "fed", "hsbc", "citi", "amex"]\n'
        )
    )
    emi_tenure: typing.Optional[int] = pydantic.Field(description=("EMI tenure selected by the user\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
