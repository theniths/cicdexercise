from src.procurement import (
    is_valid_sku,
    has_duplicate_skus,
    is_approved_vendor_email,
    meets_minimum_order,
    validate_purchase_order,
)

# ---------- SKU TESTS ----------

def test_valid_sku():
    assert is_valid_sku("ELE-1234-AB")

def test_invalid_sku_format():
    assert not is_valid_sku("ELE1234AB")

def test_invalid_sku_lowercase():
    assert not is_valid_sku("ele-1234-AB")


# ---------- DUPLICATE SKU TESTS ----------

def test_no_duplicate_skus():
    skus = ["ELE-1234-AB", "OFF-5678-CD"]
    assert not has_duplicate_skus(skus)

def test_duplicate_skus():
    skus = ["ELE-1234-AB", "ELE-1234-AB"]
    assert has_duplicate_skus(skus)


# ---------- VENDOR EMAIL TESTS ----------

def test_approved_vendor_email():
    assert is_approved_vendor_email("supplier@vendor.com")

def test_unapproved_vendor_email():
    assert not is_approved_vendor_email("supplier@gmail.com")


# ---------- MINIMUM ORDER TESTS ----------

def test_meets_minimum_order():
    assert meets_minimum_order(10, 5)


# ---------- FULL PURCHASE ORDER TESTS ----------

def test_valid_purchase_order():
    order = {
        "vendor_email": "supplier@vendor.com",
        "items": [
            {"sku": "ELE-1234-AB", "price": 100, "quantity": 10},
            {"sku": "OFF-5678-CD", "price": 50, "quantity": 5}
        ]
    }

    assert validate_purchase_order(order, budget=2000, minimum_required=2)


def test_invalid_vendor_email():
    order = {
        "vendor_email": "supplier@gmail.com",
        "items": [
            {"sku": "ELE-1234-AB", "price": 100, "quantity": 10}
        ]
    }

    assert not validate_purchase_order(order, budget=2000, minimum_required=2)


def test_duplicate_sku_in_order():
    order = {
        "vendor_email": "supplier@vendor.com",
        "items": [
            {"sku": "ELE-1234-AB", "price": 100, "quantity": 10},
            {"sku": "ELE-1234-AB", "price": 50, "quantity": 5}
        ]
    }

    assert not validate_purchase_order(order, budget=2000, minimum_required=2)


def test_order_exceeds_budget():
    order = {
        "vendor_email": "supplier@vendor.com",
        "items": [
            {"sku": "ELE-1234-AB", "price": 2000, "quantity": 2}
        ]
    }

    assert not validate_purchase_order(order, budget=2000, minimum_required=1)