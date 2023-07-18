# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ErrorResponseType(str, enum.Enum):
    """
    One of ["invalid_request_error", "authentication_error", "rate_limit_error", "validation_error", "api_error"]
    """

    INVALID_REQUEST_ERROR = "invalid_request_error"
    AUTHENTICATION_ERROR = "authentication_error"
    RATE_LIMIT_ERROR = "rate_limit_error"
    VALIDATION_ERROR = "validation_error"
    API_ERROR = "api_error"

    def visit(
        self,
        invalid_request_error: typing.Callable[[], T_Result],
        authentication_error: typing.Callable[[], T_Result],
        rate_limit_error: typing.Callable[[], T_Result],
        validation_error: typing.Callable[[], T_Result],
        api_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ErrorResponseType.INVALID_REQUEST_ERROR:
            return invalid_request_error()
        if self is ErrorResponseType.AUTHENTICATION_ERROR:
            return authentication_error()
        if self is ErrorResponseType.RATE_LIMIT_ERROR:
            return rate_limit_error()
        if self is ErrorResponseType.VALIDATION_ERROR:
            return validation_error()
        if self is ErrorResponseType.API_ERROR:
            return api_error()
