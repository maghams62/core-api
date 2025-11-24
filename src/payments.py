"""Core payments workflow."""


def create_payment(amount: float, currency: str, vat_code: str | None = None) -> dict:
    """Allow downstream callers to include a VAT code (optional)."""
    if amount <= 0:
        raise ValueError("amount must be positive")
    payload = {
        "amount": amount,
        "currency": currency.upper(),
        "status": "pending",
        "requires_vat_code": False,
    }
    if vat_code:
        payload["vat_code"] = vat_code
    return payload
