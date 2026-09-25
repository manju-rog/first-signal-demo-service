def quote(endpoint: str, order_id: str) -> dict:
    """Call the configured tax dependency once; retries live in the HTTP layer."""
    return {"endpoint": endpoint, "order_id": order_id}
