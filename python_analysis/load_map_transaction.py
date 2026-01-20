import os
import json
import mysql.connector

# ------------------ DB CONNECTION ------------------
connection = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    port=4000,
    user="2dr6yzXnL6Bbrn7.root",
    password="8lPgy0tN2RoPunUG",
    database="phonepe",
    ssl_ca="/etc/ssl/cert.pem"
)

cursor = connection.cursor()

# ------------------ BASE PATH ------------------
BASE_PATH = "data_extraction/pulse/data/map/transaction/hover/country/india/state"

# ------------------ ITERATE STATES ------------------
for state in os.listdir(BASE_PATH):
    state_path = os.path.join(BASE_PATH, state)

    if not os.path.isdir(state_path):
        continue

    # ------------------ ITERATE YEARS ------------------
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)

        if not os.path.isdir(year_path):
            continue

        # ------------------ ITERATE QUARTERS ------------------
        for file in os.listdir(year_path):
            if not file.endswith(".json"):
                continue

            quarter = int(file.replace(".json", ""))
            file_path = os.path.join(year_path, file)

            with open(file_path, "r") as f:
                data = json.load(f)

            hover_data = data["data"]["hoverDataList"]

            for entry in hover_data:
                transaction_type = entry["name"]
                count = entry["metric"][0]["count"]
                amount = entry["metric"][0]["amount"]

                insert_query = """
                INSERT INTO map_transaction
                (year, quarter, state, transaction_type, transaction_count, transaction_amount)
                VALUES (%s, %s, %s, %s, %s, %s)
                """

                values = (
                    int(year),
                    quarter,
                    state.replace("-", " ").title(),
                    transaction_type,
                    count,
                    amount
                )

                cursor.execute(insert_query, values)

# ------------------ COMMIT & CLOSE ------------------
connection.commit()
cursor.close()
connection.close()

print("Map transaction data loaded successfully.")

