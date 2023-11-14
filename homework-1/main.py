"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from tables import *

employees_data = get_employees_data("employees_data.csv")
orders_data = get_orders_data("orders_data.csv")
customers_data = get_customers_data("customers_data.csv")

try:
    with psycopg2.connect(
            dbname="north",
            user="postgres",
            password="5r36d6ft",
            host="localhost",
            client_encoding='utf-8'
    ) as conn:
        with conn.cursor() as cur:
            for line in employees_data[1:]:
                cur.execute(
                    "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                    (line[0], line[1], line[2], line[3], line[4], line[5])
                )

except Exception as ex:
    print("Exception:", ex)

finally:
    conn.close()
