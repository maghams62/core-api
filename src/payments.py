"""Core payments workflow."""


def create_payment(amount: float, currency: str) -> dict:
    """Create a payment using the initial contract (no VAT)."""
    if amount <= 0:
        raise ValueError("amount must be positive")
    return {
        "amount": amount,
        "currency": currency.upper(),
        "status": "pending",
        "requires_vat_code": False,
    }
