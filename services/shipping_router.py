"""
Shipping Router - Dispatch logic for multi-carrier logistics rates.
"""

def calculate_shipping(order_type, weight):
    if order_type == "standard":
        fee = weight * 1.5
    elif order_type == "express":
        fee = weight * 3.0
    elif order_type == "overnight":
        fee = weight * 5.0
    elif order_type == "priority":
        fee = weight * 4.0
    else:
        fee = weight * 1.0
    return fee

if __name__ == "__main__":
    print("Express shipping:", calculate_shipping("express", 5.0))
