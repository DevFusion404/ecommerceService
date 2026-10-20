"""
Customer Model - Represents client profile and delivery address.
"""

from models.address import Address

class Customer:
    def __init__(self, address: Address):
        self.address = address

def get_city_label(customer: Customer):
    return customer.address.city

def test_run():
    c = Customer(Address("Seattle", "98101"))
    return get_city_label(c)

if __name__ == "__main__":
    print("Customer city:", test_run())
