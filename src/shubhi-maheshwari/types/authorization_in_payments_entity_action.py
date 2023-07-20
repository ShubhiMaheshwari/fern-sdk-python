# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AuthorizationInPaymentsEntityAction(str, enum.Enum):
    """
    One of CAPTURE or VOID
    """

    CAPTURE = "CAPTURE"
    VOID = "VOID"

    def visit(self, capture: typing.Callable[[], T_Result], void: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthorizationInPaymentsEntityAction.CAPTURE:
            return capture()
        if self is AuthorizationInPaymentsEntityAction.VOID:
            return void()
