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
BASE_PATH = "data_extraction/pulse/data/aggregated/user/country/india"

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

        users_data = data["data"]["aggregated"]

        registered_users = users_data["registeredUsers"]
        app_opens = users_data["appOpens"]

        insert_query = """
        INSERT INTO aggregated_user
        (year, quarter, country, state, registered_users, app_opens)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            int(year),
            quarter,
            "India",
            None,
            registered_users,
            app_opens
        )

        cursor.execute(insert_query, values)

# ---------- Commit & close ----------
connection.commit()
cursor.close()
connection.close()

print("Aggregated user data loaded successfully.")