import os
import json
import mysql.connector

# -------------------- DATABASE CONNECTION --------------------
connection = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    port=4000,
    user="2dr6yzXnL6Bbrn7.root",
    password="8lPgy0tN2RoPunUG",
    database="phonepe",
    ssl_ca="/etc/ssl/cert.pem"
)

cursor = connection.cursor()

# -------------------- BASE DATA PATH --------------------
BASE_PATH = "data_extraction/pulse/data/aggregated/insurance/country/india"

# -------------------- INSERT QUERY --------------------
insert_query = """
INSERT INTO aggregated_insurance (
    year,
    quarter,
    country,
    state,
    insurance_count,
    insurance_amount
)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# -------------------- DATA LOADING --------------------
for year in os.listdir(BASE_PATH):
    year_path = os.path.join(BASE_PATH, year)

    if not os.path.isdir(year_path):
        continue

    for file in os.listdir(year_path):
        if not file.endswith(".json"):
            continue

        quarter = int(file.replace(".json", "").replace("Q", ""))

        file_path = os.path.join(year_path, file)

        with open(file_path, "r") as f:
            data = json.load(f)

        for record in data["data"]["transactionData"]:
            values = (
                int(year),
                quarter,
                "India",
                record["name"],
                record["paymentInstruments"][0]["count"],
                record["paymentInstruments"][0]["amount"]
            )

            cursor.execute(insert_query, values)

# -------------------- COMMIT & CLOSE --------------------
connection.commit()
cursor.close()
connection.close()

print("Aggregated insurance data loaded successfully.")