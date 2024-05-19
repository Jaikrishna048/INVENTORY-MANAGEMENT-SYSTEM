import mysql.connector


def connect_to_database(): try:
connection = mysql.connector.connect( host="localhost",
user="root", password="root", database="inventory_db"
)
print("Connected to the database") return connection
except mysql.connector.Error as e: print("Error connecting to the database:", e) return None

def create_product_table(connection): try:
cursor = connection.cursor() cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL,
category VARCHAR(50) NOT NULL,
quantity INT NOT NULL,
price DECIMAL(10,2) NOT NULL
)
 
""")
print("Product table created successfully") cursor.close()
except mysql.connector.Error as e: print("Error creating product table:", e)

def add_product(connection):
name = input("Enter product name: ") category = input("Enter product category: ")
quantity = int(input("Enter product quantity: ")) price = float(input("Enter product price: "))

try:
cursor = connection.cursor() cursor.execute("""
INSERT INTO products (name, category, quantity, price) VALUES (%s, %s, %s, %s)
""", (name, category, quantity, price)) connection.commit()
print("Product added successfully") cursor.close()
except mysql.connector.Error as e: print("Error adding product:", e)

def view_products(connection): try:
cursor = connection.cursor() cursor.execute("SELECT * FROM products") products = cursor.fetchall()
 
if products:
print("Product ID | Product Name | Category | Quantity | Price") print("	-")
for product in products:
print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]} |
{product[4]}") else:
print("No products found in the inventory") cursor.close()
except mysql.connector.Error as e: print("Error viewing products:", e)

def update_product(connection, product_id, quantity, price): try:
cursor = connection.cursor() cursor.execute("""
UPDATE products
SET quantity = %s, price = %s WHERE id = %s
""", (quantity, price, product_id)) connection.commit()
print("Product information updated successfully") cursor.close()
except mysql.connector.Error as e:
print("Error updating product information:", e)


def remove_product(connection, product_id): try:
cursor = connection.cursor()
 
cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
connection.commit()
print("Product removed from inventory") cursor.close()
except mysql.connector.Error as e:
print("Error removing product from inventory:", e)



def main():
connection = connect_to_database() if connection:
create_product_table(connection)


while True: print("\nMenu:") print("1. Add Product")
print("2. Update Product") print("3. View Products") print("4. Remove Product") print("5. Exit")

choice = input("Enter your choice (1-5): ")


if choice == "1": add_product(connection)
elif choice == "2":
product_id = int(input("Enter the product ID to update: ")) quantity = int(input("Enter the new quantity: "))
 
price = float(input("Enter the new price: ")) update_product(connection, product_id, quantity, price)
elif choice == "3": view_products(connection)
elif choice == "4":
product_id = int(input("Enter the product ID to remove: ")) remove_product(connection, product_id)
elif choice == "5": print("Exiting...") break
else:
print("Invalid choice. Please enter a number between 1 and 5.")


connection.close()
print("Connection to the database closed")


if _name_ == "_main_": main()
