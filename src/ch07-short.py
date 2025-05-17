# ตัวอย่างการสร้าง List ที่มีข้อมูลเริ่มต้น (รายการสินค้าในแค็ตตาล็อก)
# Nested List
customer_orders = [
    [1001, "Alice", 350.00],  # Order 1
    [1002, "Bob", 1200.50],   # Order 2
    [1003, "Alice", 80.00],    # Order 3
    [1004, "Charlie", 2500.75] # Order 4
]

# Display name for order 4
print("Order 2 name:", customer_orders[3][1])
