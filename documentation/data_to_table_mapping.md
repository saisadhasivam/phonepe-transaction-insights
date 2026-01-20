# Data to SQL Table Mapping

## Aggregated Tables

### aggregated_transaction
Source:
data/aggregated/transaction/

Data includes:
- Year
- Quarter
- Country / State
- Transaction category
- Transaction count
- Transaction amount

### aggregated_user
Source:
data/aggregated/user/

Data includes:
- Year
- Quarter
- Registered users
- App opens

### aggregated_insurance
Source:
data/aggregated/insurance/

Data includes:
- Year
- Quarter
- Insurance transaction count
- Insurance transaction amount

---

## Map Tables

### map_transaction
Source:
data/map/transaction/

Granularity:
- State
- District

### map_user
Source:
data/map/user/

Granularity:
- State
- District

### map_insurance
Source:
data/map/insurance/

Granularity:
- State
- District

---

## Top Tables

### top_transaction
Source:
data/top/transaction/

Identifies:
- Top states
- Top districts
- Top pincodes

### top_user
Source:
data/top/user/

Identifies:
- Top user regions

### top_insurance
Source:
data/top/insurance/

Identifies:
- Top insurance regions
