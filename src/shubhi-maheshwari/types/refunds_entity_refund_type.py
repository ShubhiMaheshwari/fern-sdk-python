# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RefundsEntityRefundType(str, enum.Enum):
    """
    This can be one of ["PAYMENT_AUTO_REFUND", "MERCHANT_INITIATED", "UNRECONCILED_AUTO_REFUND"]
    """

    PAYMENT_AUTO_REFUND = "PAYMENT_AUTO_REFUND"
    MERCHANT_INITIATED = "MERCHANT_INITIATED"
    UNRECONCILED_AUTO_REFUND = "UNRECONCILED_AUTO_REFUND"

    def visit(
        self,
        payment_auto_refund: typing.Callable[[], T_Result],
        merchant_initiated: typing.Callable[[], T_Result],
        unreconciled_auto_refund: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RefundsEntityRefundType.PAYMENT_AUTO_REFUND:
            return payment_auto_refund()
        if self is RefundsEntityRefundType.MERCHANT_INITIATED:
            return merchant_initiated()
        if self is RefundsEntityRefundType.UNRECONCILED_AUTO_REFUND:
            return unreconciled_auto_refund()
