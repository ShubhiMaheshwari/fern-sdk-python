# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OfferTncOfferTncType(str, enum.Enum):
    """
    TnC Type for the Offer. It can be either `text` or `link`
    """

    LINK = "link"
    POST = "post"

    def visit(self, link: typing.Callable[[], T_Result], post: typing.Callable[[], T_Result]) -> T_Result:
        if self is OfferTncOfferTncType.LINK:
            return link()
        if self is OfferTncOfferTncType.POST:
            return post()