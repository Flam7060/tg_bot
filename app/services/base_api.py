import requests
from typing import Optional, Dict, Any, Union


class BaseApiClient:
    def __init__(
        self, base_url: str, headers: Optional[Dict[str, str]] = None, timeout: int = 10
    ):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}
        self.timeout = timeout

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Union[Dict[str, Any], str]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Optional[requests.Response]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        req_headers = self.headers.copy()
        if headers:
            req_headers.update(headers)

        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                headers=req_headers,
                params=params,
                data=data,
                json=json,
                timeout=self.timeout,
            )
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            # Логирование или обработка ошибок
            print(f"API request error [{method} {url}]: {e}")
            return None

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Optional[requests.Response]:
        return self._request("GET", endpoint, params=params, headers=headers)

    def post(
        self,
        endpoint: str,
        data: Optional[Union[Dict[str, Any], str]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Optional[requests.Response]:
        return self._request("POST", endpoint, data=data, json=json, headers=headers)

    def put(
        self,
        endpoint: str,
        data: Optional[Union[Dict[str, Any], str]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Optional[requests.Response]:
        return self._request("PUT", endpoint, data=data, json=json, headers=headers)

    def delete(
        self, endpoint: str, headers: Optional[Dict[str, str]] = None
    ) -> Optional[requests.Response]:
        return self._request("DELETE", endpoint, headers=headers)
