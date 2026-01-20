from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM aggregated_transaction")
result = cursor.fetchone()

print("Connection successful. Row count:", result[0])

cursor.close()
conn.close()
