# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...types.otp_request_action import OtpRequestAction
from ...types.otp_response_entity import OtpResponseEntity


class AuthenticationClient:
    def __init__(
        self,
        *,
        environment: str,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None,
        api_version: typing.Optional[str] = None,
    ):
        self._environment = environment
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_version = api_version

    def otp_request(self, payment_id: str, *, otp: str, action: OtpRequestAction) -> OtpResponseEntity:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", f"orders/pay/authenticate/{payment_id}"),
            json=jsonable_encoder({"otp": otp, "action": action}),
            headers=remove_none_from_headers(
                {
                    "x-client-id": self.client_id,
                    "x-client-secret": self.client_secret,
                    "x-api-version": self.api_version,
                }
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OtpResponseEntity, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAuthenticationClient:
    def __init__(
        self,
        *,
        environment: str,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None,
        api_version: typing.Optional[str] = None,
    ):
        self._environment = environment
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_version = api_version

    async def otp_request(self, payment_id: str, *, otp: str, action: OtpRequestAction) -> OtpResponseEntity:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment}/", f"orders/pay/authenticate/{payment_id}"),
                json=jsonable_encoder({"otp": otp, "action": action}),
                headers=remove_none_from_headers(
                    {
                        "x-client-id": self.client_id,
                        "x-client-secret": self.client_secret,
                        "x-api-version": self.api_version,
                    }
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OtpResponseEntity, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
