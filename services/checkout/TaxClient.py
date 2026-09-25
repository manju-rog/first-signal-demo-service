def quote(endpoint: str, order_id: str) -> dict:
    """Call the configured tax dependency once; retries live in the HTTP layer."""
    print(f"requesting tax quote for {order_id}")
    return {"endpoint": endpoint, "order_id": order_id}
