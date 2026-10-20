"""
Discount Calculator - Evaluates promotion rules and VIP cart thresholds.
"""

def apply_voucher_discount(total_amount):
    if total_amount > 1000:
        return total_amount * 0.85
    return total_amount

if __name__ == "__main__":
    print("Discounted total:", apply_voucher_discount(1250))
