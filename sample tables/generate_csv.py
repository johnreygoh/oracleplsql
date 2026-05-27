import csv
import random
from datetime import datetime, timedelta

# Configuration
NUM_ROWS = 5000
first_names = ["Juan", "Maria", "Jose", "Luz", "Ramon", "Grace", "Risa", "Manny", "Pia", "Loren"]
last_names = ["Dela Cruz", "Reyes", "Santos", "Aquino", "Poe", "Hontiveros", "Pacquiao", "Cayetano"]
regions = ["NCR", "Luzon", "Visayas", "Mindanao"]
statuses = ["Delivered", "Shipped", "Processing", "Cancelled"]
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset", "Desk", "Chair"]
channels = ["Online", "In-Store", "Phone"]

# FIXED: Safely generate a random date within an exact range
def random_date(start_date_str, end_date_str):
    start = datetime.strptime(start_date_str, '%Y-%m-%d')
    end = datetime.strptime(end_date_str, '%Y-%m-%d')
    return start + timedelta(days=random.randint(0, (end - start).days))

# 1. Generate Customers
print("Generating customers.csv...")
with open('customers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['customer_id', 'first_name', 'last_name', 'email', 'region'])
    for i in range(1, NUM_ROWS + 1):
        fname = random.choice(first_names)
        lname = random.choice(last_names)
        email = f"{fname.lower()}.{lname.lower().replace(' ','')}@example.com"
        writer.writerow([i, fname, lname, email, random.choice(regions)])

# 2. Generate Orders
print("Generating orders.csv...")
with open('orders.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['order_id', 'customer_id', 'order_date', 'status'])
    for i in range(1, NUM_ROWS + 1):
        # Any date in 2023
        r_date = random_date('2023-01-01', '2023-12-31').strftime('%Y-%m-%d')
        writer.writerow([i, random.randint(1, NUM_ROWS), r_date, random.choice(statuses)])

# 3. Generate Order Items
print("Generating order_items.csv...")
with open('order_items.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['item_id', 'order_id', 'product_name', 'price'])
    for i in range(1, NUM_ROWS + 1):
        writer.writerow([i, random.randint(1, NUM_ROWS), random.choice(products), round(random.uniform(10.0, 1500.0), 2)])

# 4. Generate Sales Q1
print("Generating sales_q1.csv...")
with open('sales_q1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['transaction_id', 'sale_date', 'customer_id', 'amount', 'channel'])
    for i in range(1, NUM_ROWS + 1):
        # Strict Q1 Date Range
        q1_date = random_date('2023-01-01', '2023-03-31').strftime('%Y-%m-%d')
        writer.writerow([f"Q1-{i:05d}", q1_date, random.randint(1, NUM_ROWS), round(random.uniform(5.0, 500.0), 2), random.choice(channels)])

# 5. Generate Sales Q2
print("Generating sales_q2.csv...")
with open('sales_q2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['transaction_id', 'sale_date', 'customer_id', 'amount', 'channel'])
    for i in range(1, NUM_ROWS + 1):
        # Strict Q2 Date Range
        q2_date = random_date('2023-04-01', '2023-06-30').strftime('%Y-%m-%d')
        writer.writerow([f"Q2-{i:05d}", q2_date, random.randint(1, NUM_ROWS), round(random.uniform(5.0, 500.0), 2), random.choice(channels)])

print("All 5 CSV files generated successfully!")