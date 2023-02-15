# modules/common/database.py
"""This module defines the class Database to connect & manipulate DB data."""
import sqlite3
from config.config import config_dict


class Database:
    """Defines several methods to connect & CRUD DB data."""

    def __init__(self) -> None:
        """Set connection to DB file."""
        self.connection = sqlite3.connect(config_dict["DB"]["path"])
        self.cursor = self.connection.cursor()

    def test_connection(self) -> None:
        """Test connection to DB.

        Returns:
            print sqlite version
        """
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self) -> list:
        """Get the rows of a query result all customers from DB.

        Returns:
            List of tuples with data
        """
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name: str) -> list:
        """Get data by name from DB.

        Args:
            name: Customer's name

        Returns:
            List of tuples with data
        """
        query = f"SELECT address, city, postalCode, country FROM customers \
            WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id: int, qnt: int) -> None:
        """Update quantity product by ID.

        Args:
            product_id: product ID
            qnt: product quantity
        """
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id: int) -> list:
        """Get quantity product by ID

        Args:
            product_id: product ID

        Returns:
            List of tuples with data
        """
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(
        self, product_id: int, name: str, description: str, qnt: int
    ) -> None:
        """Inserts or replace product

        Args:
            product_id: product ID
            name: name of the product
            description: Some text for the description
            qnt: quantity of the product
        """
        query = f"INSERT OR REPLACE INTO products \
            (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id: int) -> None:
        """Deleting product by ID.

        Args:
            product_id: product ID
        """
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self) -> list:
        """Get detailed info about orders with JOIN.

        Returns:
            List of tuples with data
        """
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
