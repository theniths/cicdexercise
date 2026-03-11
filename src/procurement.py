import re


# Validate SKU format: AAA-1234-BB
def is_valid_sku(sku):
    pattern = r"^[A-Z]{3}-\d{4}-[A-Z]{2}$"
    return bool(re.match(pattern, sku))


# Check for duplicate SKUs
def has_duplicate_skus(skus):
    return len(skus) != len(set(skus))


# Check vendor email domain
def is_approved_vendor_email(email):
    approved_domains = ["vendor.com", "supplier.com"]
    domain = email.split("@")[-1]
    return domain in approved_domains


# Check minimum order quantity
def meets_minimum_order(quantity, minimum_required):
    return quantity >= minimum_required


# Validate full purchase order
def validate_purchase_order(order, budget, minimum_required):
    skus = []
    total = 0

    # Check vendor email
    if not is_approved_vendor_email(order["vendor_email"]):
        return False

    for item in order["items"]:
        sku = item["sku"]
        price = item["price"]
        quantity = item["quantity"]

        # SKU format check
        if not is_valid_sku(sku):
            return False

        # MOQ check
        if not meets_minimum_order(quantity, minimum_required):
            return False

        skus.append(sku)
        total += price * quantity

    # Duplicate SKU check
    if has_duplicate_skus(skus):
        return False

    # Budget check
    if total <= 0 or total > budget:
        return False

    return True
