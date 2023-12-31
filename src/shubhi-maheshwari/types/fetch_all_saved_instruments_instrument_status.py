# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FetchAllSavedInstrumentsInstrumentStatus(str, enum.Enum):
    """
    Status of the saved instrument.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is FetchAllSavedInstrumentsInstrumentStatus.ACTIVE:
            return active()
        if self is FetchAllSavedInstrumentsInstrumentStatus.INACTIVE:
            return inactive()
