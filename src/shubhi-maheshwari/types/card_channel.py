# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CardChannel(str, enum.Enum):
    """
    The channel for card payments can be "link" or "post". Post is used for seamless OTP payments where merchant captures OTP on their own page.
    """

    LINK = "link"
    POST = "post"

    def visit(self, link: typing.Callable[[], T_Result], post: typing.Callable[[], T_Result]) -> T_Result:
        if self is CardChannel.LINK:
            return link()
        if self is CardChannel.POST:
            return post()
