"""
Tax Service - Computes state and national sales taxes.
"""

def calculate_sales_tax(subtotal):
    if subtotal <= 0:
        return 0.0
    return subtotal * 0.15

if __name__ == "__main__":
    print("Sales tax on $100:", calculate_sales_tax(100.0))
