# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.remove_none_from_headers import remove_none_from_headers
from ...types.payments_entity import PaymentsEntity


class PaymentsClient:
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

    def get_paymentsfororder(self, order_id: str) -> PaymentsEntity:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"orders/{order_id}/payments"),
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
            return pydantic.parse_obj_as(PaymentsEntity, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_paymentby_id(self, order_id: str, cf_payment_id: int) -> PaymentsEntity:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"orders/{order_id}/payments/{cf_payment_id}"),
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
            return pydantic.parse_obj_as(PaymentsEntity, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPaymentsClient:
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

    async def get_paymentsfororder(self, order_id: str) -> PaymentsEntity:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment}/", f"orders/{order_id}/payments"),
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
            return pydantic.parse_obj_as(PaymentsEntity, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_paymentby_id(self, order_id: str, cf_payment_id: int) -> PaymentsEntity:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment}/", f"orders/{order_id}/payments/{cf_payment_id}"),
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
            return pydantic.parse_obj_as(PaymentsEntity, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
