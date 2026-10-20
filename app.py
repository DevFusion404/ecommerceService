"""
app.py - Main entry point for the E-Commerce Order Processing Service.
Coordinates cart validation, tax calculation, discount rules, and shipping dispatch.
"""

from core.pricing_engine import get_standard_packaging_volume
from core.discount_calculator import apply_voucher_discount
from core.tax_service import calculate_sales_tax
from services.order_processor import process_order_batch
from services.shipping_router import calculate_shipping
from services.account_manager import create_account

def run_service_pipeline():
    print("=" * 60)
    print("       E-Commerce Order Processing Service v2.4")
    print("=" * 60)

    # 1. User onboarding
    user = create_account()
    print(f"User onboarded: {user['name']} ({user['email']})")

    # 2. Packaging geometry check
    pkg_vol = get_standard_packaging_volume()
    print(f"Standard packaging volume: {pkg_vol:.2f} cm^3")

    # 3. Order batch processing
    sample_orders = [
        {"id": 101, "price": 45.0, "quantity": 2, "status": "active"},
        {"id": 102, "price": 120.0, "quantity": 1, "status": "active"},
        {"id": 103, "price": 15.0, "quantity": 5, "status": "inactive"},
    ]
    batch_summary = process_order_batch(sample_orders)
    print(f"Batch processed: {batch_summary['count']} active items, Subtotal: ${batch_summary['total']:.2f}")

    # 4. Tax & Voucher calculations
    tax = calculate_sales_tax(batch_summary["total"])
    discounted_total = apply_voucher_discount(batch_summary["total"] + tax)
    print(f"Tax: ${tax:.2f} | Final Total: ${discounted_total:.2f}")

    # 5. Logistics shipping route
    shipping_cost = calculate_shipping("express", 4.5)
    print(f"Express Shipping: ${shipping_cost:.2f}")
    print("=" * 60)

if __name__ == "__main__":
    run_service_pipeline()
