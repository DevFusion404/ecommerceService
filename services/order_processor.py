"""
Order Processor - High-volume batch ingestion and validation service.
"""

def process_order_batch(orders):
    total_amount = 0
    item_count = 0
    valid_orders = []
    tax_total = 0
    discount_total = 0
    for order in orders:
        if order.get("status") == "active":
            item_count += 1
            price = order.get("price", 0)
            quantity = order.get("quantity", 1)
            subtotal = price * quantity
            tax = subtotal * 0.08
            discount = subtotal * 0.05
            total_amount += subtotal + tax - discount
            valid_orders.append(order["id"])
    return {"count": item_count, "total": total_amount, "orders": valid_orders}

if __name__ == "__main__":
    items = [{"id": 1, "price": 40, "quantity": 2, "status": "active"}]
    print("Batch summary:", process_order_batch(items))
