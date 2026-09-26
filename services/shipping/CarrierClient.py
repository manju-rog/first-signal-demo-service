from __future__ import annotations

import httpx


class CarrierClient:
    """Small synthetic client used only by the First Signal demonstration."""

    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint
        self.timeout_seconds = 2.0
        self.retry_attempts = 2

    def quote(self, postal_code: str) -> dict[str, object]:
        last_error: httpx.TimeoutException | None = None
        for _ in range(self.retry_attempts + 1):
            try:
                response = httpx.get(
                    f"{self.endpoint}/quotes/{postal_code}",
                    timeout=self.timeout_seconds,
                )
                response.raise_for_status()
                return response.json()
            except httpx.TimeoutException as exc:
                last_error = exc
        raise RuntimeError("carrier quote timed out") from last_error
