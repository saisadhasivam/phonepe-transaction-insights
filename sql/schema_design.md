# PhonePe Database Schema Design

## 1. aggregated_transaction

Columns:
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- year (INT)
- quarter (INT)
- country (VARCHAR)
- state (VARCHAR, NULL)
- transaction_type (VARCHAR)
- transaction_count (BIGINT)
- transaction_amount (DOUBLE)

---

## 2. aggregated_user

Columns:
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- year (INT)
- quarter (INT)
- country (VARCHAR)
- state (VARCHAR, NULL)
- registered_users (BIGINT)
- app_opens (BIGINT)

---

## 3. aggregated_insurance

Columns:
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- year (INT)
- quarter (INT)
- country (VARCHAR)
- state (VARCHAR, NULL)
- insurance_count (BIGINT)
- insurance_amount (DOUBLE)
