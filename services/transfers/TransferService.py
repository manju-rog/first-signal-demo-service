"""Synthetic transfer service used only by the First Signal demonstration.

It contains no real customer, account, payment, or bank integration data.
"""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class TransferCommand:
    request_id: str
    idempotency_key: str
    logical_transfer_token: str
    amount_minor: int
    currency: str


class IdempotencyStore(Protocol):
    def get(self, key: str) -> str | None: ...
    def put(self, key: str, posting_id: str) -> None: ...


class Ledger(Protocol):
    def post(self, command: TransferCommand) -> str: ...


class TransferService:
    def __init__(self, idempotency_store: IdempotencyStore, ledger: Ledger):
        self.idempotency_store = idempotency_store
        self.ledger = ledger

    def submit(self, command: TransferCommand) -> str:
        dedupe_key = f"transfer:{command.idempotency_key}"
        existing = self.idempotency_store.get(dedupe_key)
        if existing is not None:
            return existing

        posting_id = self.ledger.post(command)
        self.idempotency_store.put(dedupe_key, posting_id)
        return posting_id
