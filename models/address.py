"""
Address Model - Value object encapsulating delivery city and postal code.
"""

class Address:
    def __init__(self, city: str, postcode: str):
        self.city = city
        self.postcode = postcode

    def __repr__(self):
        return f"Address(city='{self.city}', postcode='{self.postcode}')"
