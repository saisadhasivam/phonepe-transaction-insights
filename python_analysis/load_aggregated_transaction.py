import os
import json
import mysql.connector

# ---------- MySQL connection ----------
connection = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    port=4000,
    user="2dr6yzXnL6Bbrn7.root",
    password="8lPgy0tN2RoPunUG",
    database="phonepe",
    ssl_ca="/etc/ssl/cert.pem"
)

cursor = connection.cursor()

# ---------- Base data path ----------
BASE_PATH = "data_extraction/pulse/data/aggregated/transaction/country/india"

# ---------- Traverse folders ----------
for year in os.listdir(BASE_PATH):
    year_path = os.path.join(BASE_PATH, year)

    if not os.path.isdir(year_path):
        continue

    for file in os.listdir(year_path):
        if not file.endswith(".json"):
            continue

        quarter = int(file.replace(".json", ""))
        file_path = os.path.join(year_path, file)

        with open(file_path, "r") as f:
            data = json.load(f)

        transaction_data = data["data"]["transactionData"]

        for item in transaction_data:
            transaction_type = item["name"]
            count = item["paymentInstruments"][0]["count"]
            amount = item["paymentInstruments"][0]["amount"]

            insert_query = """
            INSERT INTO aggregated_transaction
            (year, quarter, country, state, transaction_type, transaction_count, transaction_amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                int(year),
                quarter,
                "India",
                None,
                transaction_type,
                count,
                amount
            )

            cursor.execute(insert_query, values)

# ---------- Commit & close ----------
connection.commit()
cursor.close()
connection.close()

print("Aggregated transaction data loaded successfully.")
