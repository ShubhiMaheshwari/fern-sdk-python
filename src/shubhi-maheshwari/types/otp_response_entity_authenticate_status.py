# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OtpResponseEntityAuthenticateStatus(str, enum.Enum):
    """
    Status of the is action. Will be either failed or successful. If the action is successful, you should still call the authorization status to verify the final payment status.
    """

    FAILED = "FAILED"
    SUCCESS = "SUCCESS"

    def visit(self, failed: typing.Callable[[], T_Result], success: typing.Callable[[], T_Result]) -> T_Result:
        if self is OtpResponseEntityAuthenticateStatus.FAILED:
            return failed()
        if self is OtpResponseEntityAuthenticateStatus.SUCCESS:
            return success()
