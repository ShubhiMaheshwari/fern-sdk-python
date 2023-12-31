# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class FetchPgReconDataItem(pydantic.BaseModel):
    event_id: typing.Optional[str] = pydantic.Field(description=("Unique ID associated with the event.\n"))
    event_type: typing.Optional[str] = pydantic.Field(
        description=(
            "The event type can be SETTLEMENT, PAYMENT, REFUND, REFUND_REVERSAL, DISPUTE, DISPUTE_REVERSAL, CHARGEBACK, CHARGEBACK_REVERSAL, OTHER_ADJUSTMENT.\n"
        )
    )
    event_settlement_amount: typing.Optional[float] = pydantic.Field(
        description=("Amount that is part of the settlement corresponding to the event.\n")
    )
    event_amount: typing.Optional[float] = pydantic.Field(
        description=("Amount of the event. Example, refund amount, dispute amount, payment amount, etc.\n")
    )
    sale_type: typing.Optional[str] = pydantic.Field(description=("Indicates if it is CREDIT/DEBIT sale.\n"))
    event_status: typing.Optional[str] = pydantic.Field(
        description=("Status of the event. Example - SUCCESS, FAILED, PENDING, CANCELLED.\n")
    )
    entity: typing.Optional[str] = pydantic.Field(description=("Recon\n"))
    event_time: typing.Optional[str] = pydantic.Field(
        description=("Time associated with the event. Example, transaction time, dispute initiation time\n")
    )
    event_currency: typing.Optional[str] = pydantic.Field(description=("Curreny type - INR.\n"))
    order_id: typing.Optional[str] = pydantic.Field(
        description=("Unique order ID. Alphanumeric and only '-' and '_' allowed.\n")
    )
    order_amount: typing.Optional[float] = pydantic.Field(
        description=("The amount which was passed at the order creation time.\n")
    )
    customer_phone: typing.Optional[str] = pydantic.Field(description=("Customer phone number.\n"))
    customer_email: typing.Optional[str] = pydantic.Field(description=("Customer email.\n"))
    customer_name: typing.Optional[str] = pydantic.Field(description=("Customer name.\n"))
    payment_amount: typing.Optional[float] = pydantic.Field(description=("Payment amount captured.\n"))
    payment_utr: typing.Optional[str] = pydantic.Field(
        description=("Unique transaction reference number of the payment.\n")
    )
    payment_time: typing.Optional[str] = pydantic.Field(description=("Date and time when the payment was initiated.\n"))
    payment_service_charge: typing.Optional[float] = pydantic.Field(
        description=("Service charge applicable for the payment.\n")
    )
    payment_service_tax: typing.Optional[float] = pydantic.Field(
        description=("Service tax applicable on the payment.\n")
    )
    cf_payment_id: typing.Optional[int] = pydantic.Field(
        description=("Cashfree Payments unique ID to identify a payment.\n")
    )
    cf_settlement_id: typing.Optional[int] = pydantic.Field(description=("Unique ID to identify the settlement.\n"))
    settlement_date: typing.Optional[str] = pydantic.Field(
        description=("Date and time when the settlement was processed.\n")
    )
    settlement_utr: typing.Optional[str] = pydantic.Field(
        description=("Unique transaction reference number of the settlement.\n")
    )
    split_service_charge: typing.Optional[float] = pydantic.Field(
        description=("Service charge that is applicable for splitting the payment.\n")
    )
    split_service_tax: typing.Optional[float] = pydantic.Field(
        description=("Service tax applicable for splitting the amount to vendors.\n")
    )
    vendor_commission: typing.Optional[float] = pydantic.Field(
        description=("Vendor commission applicable for this transaction.\n")
    )
    closed_in_favor_of: typing.Optional[str] = pydantic.Field(
        description=(
            "Specifies whether the dispute was closed in favor of the merchant or customer. /n Possible values - Merchant, Customer\n"
        )
    )
    dispute_resolved_on: typing.Optional[str] = pydantic.Field(
        description=("Date and time when the dispute was resolved.\n")
    )
    dispute_category: typing.Optional[str] = pydantic.Field(
        description=("Category of the dispute - Dispute code and the reason for dispute is shown.\n")
    )
    dispute_note: typing.Optional[str] = pydantic.Field(description=("Note regarding the dispute.\n"))
    refund_processed_at: typing.Optional[str] = pydantic.Field(
        description=("Date and time when the refund was processed.\n")
    )
    refund_arn: typing.Optional[str] = pydantic.Field(description=("The bank reference number for the refund.\n"))
    refund_note: typing.Optional[str] = pydantic.Field(description=("A refund note for your reference.\n"))
    refund_id: typing.Optional[str] = pydantic.Field(description=("An unique ID to associate the refund with.\n"))
    adjustment_remarks: typing.Optional[str] = pydantic.Field(description=("Other adjustment remarks.\n"))
    adjustment: typing.Optional[float] = pydantic.Field(
        description=(
            "Amount that is adjusted from the settlement amount because of any credit/debit event such as refund, refund_reverse etc.\n"
        )
    )
    service_tax: typing.Optional[float] = pydantic.Field(
        description=("Service tax applicable on the settlement amount.\n")
    )
    service_charge: typing.Optional[float] = pydantic.Field(
        description=("Service charge applicable on the settlement amount.\n")
    )
    amount_settled: typing.Optional[float] = pydantic.Field(
        description=("Net amount that is settled after considering the adjustments, settlement charge and tax.\n")
    )
    payment_from: typing.Optional[str] = pydantic.Field(
        description=("The start time of the time range of the payments considered for the settlement.\n")
    )
    payment_till: typing.Optional[str] = pydantic.Field(
        description=("The end time of time range of the payments considered for the settlement.\n")
    )
    reason: typing.Optional[str] = pydantic.Field(description=("Reason for settlement failure.\n"))
    settlement_initiated_on: typing.Optional[str] = pydantic.Field(
        description=("Date and time when the settlement was initiated.\n")
    )
    settlement_type: typing.Optional[str] = pydantic.Field(
        description=("Type of settlement. Possible values - Standard, Instant, On demand.\n")
    )
    settlement_charge: typing.Optional[float] = pydantic.Field(
        description=("Settlement charges applicable on the settlement.\n")
    )
    settlement_tax: typing.Optional[float] = pydantic.Field(
        description=("Settlement tax applicable on the settlement.\n")
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
