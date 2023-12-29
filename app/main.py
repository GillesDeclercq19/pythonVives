def main():
    db_path = load_settings()
    db = Database(db_path)

    create_users_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
    """
    create_products_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
    """
    db.execute_query(create_users_table_query)
    db.execute_query(create_products_table_query)

    while True:
        print("\n1. Add a user")
        print("2. Add a product")
        print("3. Generate user report")
        print("4. Genereer product report")
        print("5. Change user")
        print("6. Exit")

        choice = input("Select a option: ")

        if choice == '1':
            username, email = get_user_input_user()
            insert_user_query = "INSERT INTO users (username, email) VALUES (?, ?)"
            db.execute_query(insert_user_query, (username, email))
            print("User added.")

        elif choice == '2':
            name, price = get_user_input_product()
            insert_product_query = "INSERT INTO products (name, price) VALUES (?, ?)"
            db.execute_query(insert_product_query, (name, price))
            print("Product added.")

        elif choice == '3':
            select_users_query = "SELECT * FROM users"
            users_data = db.fetch_query(select_users_query)
            report_format = input("Select format (csv/excel): ").lower()
            file_path = 'rapporten/users_report.csv'  

        elif choice == '4':
            select_products_query = "SELECT * FROM products"
            products_data = db.fetch_query(select_products_query)
            report_format = input("Select format (csv/excel): ").lower()
            file_path = 'rapporten/products_report.csv' 
            

        

        else:
            print("Invalid choice, try again")



if __name__ == "__main__":
    main()
