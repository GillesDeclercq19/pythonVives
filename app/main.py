import os
import csv
import pandas as pd
from database import Database
from models import User, Product
from utils import load_settings

def get_user_input_user():
    username = input("Voer gebruikersnaam in: ")
    email = input("Voer e-mailadres in: ")
    return username, email

def get_user_input_product():
    name = input("Voer productnaam in: ")
    price = float(input("Voer productprijs in: "))
    return name, price

def display_users(db):
    select_users_query = "SELECT user_id, username, email FROM users"
    users_data = db.fetch_query(select_users_query)

    print("\nAlle gebruikers:")
    for user in users_data:
        print(f"ID: {user['user_id']}, Naam: {user['username']}, E-mail: {user['email']}")

def generate_report(data, format, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if format == 'csv':
        if not data:
            print("Geen gegevens om te rapporteren.")
            return
        if isinstance(data[0], tuple):
            fieldnames = ["column1", "column2", ...]  
            data = [dict(zip(fieldnames, row)) for row in data]

        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in data:
                writer.writerow(row)

        print(f"Rapport gegenereerd in CSV-formaat ({file_path})")
    elif format == 'excel':
        df = pd.DataFrame(data)
        df.to_excel(file_path + '.xlsx', index=False, engine='xlsxwriter')
        print(f"Rapport gegenereerd in Excel-formaat ({file_path}.xlsx)")
    else:
        print("Ongeldig rapportformaat. Alleen CSV en Excel worden ondersteund.")

def update_user(db):
    user_id = int(input("Voer het ID van de gebruiker in die je wilt bijwerken: "))
    new_username = input("Voer de nieuwe gebruikersnaam in: ")
    new_email = input("Voer het nieuwe e-mailadres in: ")

    update_user_query = "UPDATE users SET username=?, email=? WHERE user_id=?"
    db.execute_query(update_user_query, (new_username, new_email, user_id))
    print("Gebruiker bijgewerkt.")

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
        print("\n1. Voeg gebruiker toe")
        print("2. Voeg product toe")
        print("3. Genereer rapport gebruikers")
        print("4. Genereer rapport producten")
        print("5. Werk gebruiker bij")
        print("6. Afsluiten")

        choice = input("Selecteer een optie: ")

        if choice == '1':
            username, email = get_user_input_user()
            insert_user_query = "INSERT INTO users (username, email) VALUES (?, ?)"
            db.execute_query(insert_user_query, (username, email))
            print("Gebruiker toegevoegd.")

        elif choice == '2':
            name, price = get_user_input_product()
            insert_product_query = "INSERT INTO products (name, price) VALUES (?, ?)"
            db.execute_query(insert_product_query, (name, price))
            print("Product toegevoegd.")

        elif choice == '3':
            select_users_query = "SELECT * FROM users"
            users_data = db.fetch_query(select_users_query)
            report_format = input("Selecteer het rapportformaat (csv/excel): ").lower()
            file_path = 'rapporten/users_report.csv'  
            generate_report(users_data, report_format, file_path)

        elif choice == '4':
            select_products_query = "SELECT * FROM products"
            products_data = db.fetch_query(select_products_query)
            report_format = input("Selecteer het rapportformaat (csv/excel): ").lower()
            file_path = 'rapporten/products_report.csv' 
            generate_report(products_data, report_format, file_path)

        elif choice == '5':
            display_users(db)
            update_user(db)

        elif choice == '6':
            break

        else:
            print("Ongeldige keuze. Probeer opnieuw.")



if __name__ == "__main__":
    main()
