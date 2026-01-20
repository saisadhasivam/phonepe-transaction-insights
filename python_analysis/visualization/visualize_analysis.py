# ---------------------------------------------
# PhonePe Data Analysis – Python Visualizations
# ---------------------------------------------

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from python_analysis.db_connection import get_connection

# ---------------------------------------------
# BASIC SETUP
# ---------------------------------------------

OUTPUT_DIR = "python_analysis/visualization/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# ---------------------------------------------
# DATABASE CONNECTION
# ---------------------------------------------

conn = get_connection()

# ---------------------------------------------
# 1. YEARLY TRANSACTION GROWTH
# ---------------------------------------------

query_yearly_transactions = """
SELECT
    year,
    SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY year
ORDER BY year;
"""

df_yearly = pd.read_sql(query_yearly_transactions, conn)

plt.figure()
plt.plot(df_yearly["year"], df_yearly["total_amount"], marker="o")
plt.title("Yearly Transaction Growth")
plt.xlabel("Year")
plt.ylabel("Total Transaction Amount")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "yearly_transaction_growth.png"))
plt.close()

# ---------------------------------------------
# 2. TOP 10 STATES BY TOTAL REVENUE
# ---------------------------------------------

query_top_states = """
SELECT
    state,
    SUM(transaction_amount) AS total_revenue
FROM map_transaction
GROUP BY state
ORDER BY total_revenue DESC
LIMIT 10;
"""

df_states = pd.read_sql(query_top_states, conn)

plt.figure()
sns.barplot(
    data=df_states,
    x="total_revenue",
    y="state"
)
plt.title("Top 10 States by Transaction Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("State")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "top_10_states_revenue.png"))
plt.close()

# ---------------------------------------------
# 3. TRANSACTION TYPE DISTRIBUTION
# ---------------------------------------------

query_txn_type = """
SELECT
    transaction_type,
    SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total_amount DESC;
"""

df_txn_type = pd.read_sql(query_txn_type, conn)

plt.figure()
sns.barplot(
    data=df_txn_type,
    x="total_amount",
    y="transaction_type"
)
plt.title("Transaction Amount by Type")
plt.xlabel("Total Amount")
plt.ylabel("Transaction Type")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "transaction_type_distribution.png"))
plt.close()

# ---------------------------------------------
# 4. USER ADOPTION OVER TIME
# ---------------------------------------------

query_users = """
SELECT
    year,
    SUM(registered_users) AS users
FROM aggregated_user
GROUP BY year
ORDER BY year;
"""

df_users = pd.read_sql(query_users, conn)

plt.figure()
plt.plot(df_users["year"], df_users["users"], marker="o", color="green")
plt.title("User Adoption Over Time")
plt.xlabel("Year")
plt.ylabel("Registered Users")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "user_adoption_growth.png"))
plt.close()

# ---------------------------------------------
# 5. INSURANCE GROWTH OVER TIME
# ---------------------------------------------

query_insurance = """
SELECT
    year,
    SUM(insurance_amount) AS total_amount
FROM aggregated_insurance
GROUP BY year
ORDER BY year;
"""

df_insurance = pd.read_sql(query_insurance, conn)

plt.figure()
plt.plot(df_insurance["year"], df_insurance["total_amount"], marker="o", color="purple")
plt.title("Insurance Transaction Growth")
plt.xlabel("Year")
plt.ylabel("Insurance Amount")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "insurance_growth.png"))
plt.close()

# ---------------------------------------------
# CLOSE CONNECTION
# ---------------------------------------------

conn.close()

print("✅ All visualizations generated successfully.")