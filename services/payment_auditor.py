"""
Payment Auditor - Validates transaction settlements and audit trails.
"""

def process_transaction(amount):
    if amount <= 0:
        return False
    print("Processing amount:", amount)
    return True
    print("Unreachable audit line")

if __name__ == "__main__":
    print("Transaction ok:", process_transaction(250))
