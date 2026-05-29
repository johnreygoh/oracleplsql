import csv
import random
import itertools
from datetime import datetime, timedelta

# Configuration
NUM_ROWS = 5000

# 80 First Names
first_names = [
    "Juan", "Jose", "Pedro", "Miguel", "Carlos", "Ramon", "Vicente", "Arturo", "Mario", "Rafael",
    "Ernesto", "Reynaldo", "Romeo", "Fernando", "Rodolfo", "Renato", "Danilo", "Ruben", "Teodoro", "Tomas",
    "Grace", "Risa", "Manny", "Pia", "Loren", "Leni", "Rodrigo", "Bongbong", "Sara", "Isko",
    "Vico", "Joy", "Abby", "Marcelino", "Rex", "Alan", "Chiz", "Koko", "Migz", "Sonny",
    "Joel", "Win", "Sherwin", "Bam", "Imee", "Cynthia", "Nancy", "JV", "Jinggoy", "Robin",
    "Raffy", "Mark", "Allan", "Tito", "Vic", "Joey", "Pepe", "Lito", "Mar", "Noli",
    "Jojo", "Jejomar", "Panfilo", "Ping", "Dick", "Richard", "Ralph", "Kiko", "Francis", "Antonio",
    "Leila", "Ruffy", "Ed", "Martin", "Gloria", "Fidel", "Cory", "Erap", "Ferdinand", "Benigno"
]

# 80 Last Names
last_names = [
    "Dela Cruz", "Garcia", "Reyes", "Ramos", "Mendoza", "Santos", "Flores", "Gonzales", "Bautista", "Villanueva",
    "Fernandez", "Cruz", "De Leon", "Ocampo", "Perez", "Castro", "Aquino", "Marquez", "Padilla", "Domingo",
    "Navarro", "Torres", "Castillo", "Sison", "Vargas", "Tolentino", "Roxas", "Poe", "Hontiveros", "Pacquiao",
    "Cayetano", "Legarda", "Robredo", "Duterte", "Marcos", "Moreno", "Sotto", "Pimentel", "Zubiri", "Angara",
    "Gatchalian", "Villar", "Binay", "Ejercito", "Estrada", "Tulfo", "Revilla", "Lapid", "Recto", "Gordon",
    "Pangilinan", "Trillanes", "Lacson", "Honasan", "Enrile", "Drilon", "Arroyo", "Macapagal", "Magsaysay", "Quirino",
    "Osmena", "Quezon", "Aguinaldo", "Bonifacio", "Rizal", "Mabini", "Luna", "Del Pilar", "Silang", "Cojuangco",
    "Lopez", "Ayala", "Sy", "Tan", "Gokongwei", "Abalos", "Remulla", "Biazon", "Belmonte", "Gomez"
]

regions = ["NCR", "Luzon", "Visayas", "Mindanao"]
statuses = ["Delivered", "Shipped", "Processing", "Cancelled"]
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset", "Desk", "Chair", "Webcam", "Docking Station", "Tablet"]
channels = ["Online", "In-Store", "Phone"]

# Generate EXACTLY 6,400 Unique Name Combinations (80 x 80)
all_name_combinations = list(itertools.product(first_names, last_names))
random.shuffle(all_name_combinations)

# Take only the first 5000 combinations
unique_names = all_name_combinations[:NUM_ROWS]

# Safely generate a random date within an exact range
def random_date(start_date_str, end_date_str):
    start = datetime.strptime(start_date_str, '%Y-%m-%d')
    end = datetime.strptime(end_date_str, '%Y-%m-%d')
    return start + timedelta(days=random.randint(0, (end - start).days))

# 1. Generate Customers (Guaranteed Unique Names)
print("Generating customers.csv...")
with open('customers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['customer_id', 'first_name', 'last_name', 'email', 'region'])
    for i in range(1, NUM_ROWS + 1):
        fname, lname = unique_names[i-1] # Pull from our unique combinations
        
        # Adding the customer ID to the email ensures it will never violate a UNIQUE constraint
        clean_fname = fname.lower().replace(' ', '')
        clean_lname = lname.lower().replace(' ', '')
        email = f"{clean_fname}.{clean_lname}.{i}@example.com"
        
        writer.writerow([i, fname, lname, email, random.choice(regions)])

# 2. Generate Orders
print("Generating orders.csv...")
with open('orders.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['order_id', 'customer_id', 'order_date', 'status'])
    for i in range(1, NUM_ROWS + 1):
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
        q1_date = random_date('2023-01-01', '2023-03-31').strftime('%Y-%m-%d')
        writer.writerow([f"Q1-{i:05d}", q1_date, random.randint(1, NUM_ROWS), round(random.uniform(5.0, 500.0), 2), random.choice(channels)])

# 5. Generate Sales Q2
print("Generating sales_q2.csv...")
with open('sales_q2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['transaction_id', 'sale_date', 'customer_id', 'amount', 'channel'])
    for i in range(1, NUM_ROWS + 1):
        q2_date = random_date('2023-04-01', '2023-06-30').strftime('%Y-%m-%d')
        writer.writerow([f"Q2-{i:05d}", q2_date, random.randint(1, NUM_ROWS), round(random.uniform(5.0, 500.0), 2), random.choice(channels)])

print("All 5 CSV files generated successfully with NO duplicate names!")