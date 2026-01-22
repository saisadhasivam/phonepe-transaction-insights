# PhonePe Transaction Insights

**End-to-End Data Analysis and Insight Generation using SQL, Python, and Streamlit**

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---

## 1. Project Overview

This project delivers a comprehensive, end-to-end analytical study of **PhonePe Pulse transactional data**, with the objective of extracting actionable business insights across **transactions, user adoption, regional performance, and insurance growth** in India.

The work follows a structured analytics lifecycle from raw data extraction and database design to analysis, visualization, and business interpretation — culminating in a **Streamlit-based executive dashboard**.

This repository is designed to reflect **industry-grade analytical standards**, emphasizing clarity, reproducibility, scalability, and decision-oriented insights.

---

## 2. Business Objectives

The primary business questions addressed in this project are:

* How has PhonePe’s transaction value evolved year-over-year across India?
* Which states contribute disproportionately to transaction revenue?
* What transaction categories dominate platform usage?
* How has user adoption grown geographically and temporally?
* Is insurance adoption emerging as a meaningful growth lever?
* What strategic opportunities exist based on observed patterns?

---

## 3. Data Source

* **Dataset**: PhonePe Pulse (publicly available aggregated data)
* **Granularity**:

  * Yearly and quarterly transaction data
  * State-level and district-level aggregation
  * Transaction categories, users, and insurance metrics

---

## 4. Project Architecture & Folder Structure

```
phonepe/
│
├── data_extraction/
│   └── pulse/
│       └── Scripts and references for sourcing raw PhonePe Pulse data
│
├── documentation/
│   ├── data_to_table_mapping.md
│   └── rubric_checklist.md
│
├── presentation/
│   └── High-level narrative or presentation artifacts (optional use)
│
├── python_analysis/
│   ├── __init__.py
│   ├── db_connection.py
│   ├── load_aggregated_transaction.py
│   ├── load_aggregated_user.py
│   ├── load_aggregated_insurance.py
│   ├── load_map_transaction.py
│   ├── test_db.py
│   │
│   └── visualization/
│       ├── visualize_analysis.py
│       ├── yearly_transaction_growth.png
│       ├── top_10_states_revenue.png
│       ├── transaction_type_distribution.png
│       ├── user_growth.png
│       └── insurance_growth.png
│
├── sql/
│   ├── analysis_queries.sql
│   └── schema_design.md
│
├── streamlit_app/
│   └── app.py
│
├── .gitignore
└── README.md
```

---

## 5. Analytical Process

### Step 1: Data Extraction & Preparation

* Structured ingestion of PhonePe Pulse data
* Data normalization for analytics readiness
* Logical separation of transaction, user, and insurance datasets

### Step 2: Database Design & SQL Analysis

* Schema designed for analytical querying
* SQL used to:

  * Aggregate transactions by year and state
  * Rank states by transaction value
  * Segment transactions by category
  * Analyze user growth trends
  * Track insurance transaction evolution

### Step 3: Python-Based Analysis

* Python used for:

  * Database connectivity
  * Data transformation and aggregation
  * Analytical validation
  * Visualization generation using Matplotlib

### Step 4: Visualization Layer

* Static visualizations created to ensure:

  * Performance efficiency
  * Consistent insight reproducibility
  * Clear executive storytelling

### Step 5: Streamlit Dashboard

* Executive-facing dashboard built using Streamlit
* Displays precomputed insights
* Avoids live database queries for performance and stability

---

## 6. Key Insights & Interpretations

### 6.1 Yearly Transaction Growth

* Transaction value shows **consistent year-over-year growth**
* Sharp acceleration observed post-2020
* Indicates structural shift toward digital payments and increased trust

### 6.2 Top Contributing States

* A small group of states contributes a disproportionate share of revenue
* Maharashtra, Karnataka, Telangana, and Tamil Nadu dominate
* Suggests regional concentration and uneven digital penetration

### 6.3 Transaction Type Distribution

* Peer-to-peer transactions form the largest share
* Merchant payments follow closely
* Financial services and insurance are smaller but growing segments

### 6.4 User Adoption Trends

* User base increases steadily with minimal churn indicators
* Growth is geographically uneven, highlighting expansion opportunities

### 6.5 Insurance Transaction Growth

* Insurance transactions show noticeable recent growth
* Still underpenetrated compared to payments
* Represents a strong long-term monetization lever

---

## 7. Strategic Recommendations

1. **Deepen Penetration in Tier-2 and Tier-3 States**
   Focus targeted campaigns and incentives to reduce regional concentration risk.

2. **Accelerate Insurance Product Awareness**
   Bundle insurance offerings with high-frequency payment use cases.

3. **Merchant Ecosystem Expansion**
   Strengthen merchant onboarding in emerging regions to balance P2P dominance.

4. **Data-Driven Regional Strategy**
   Use state-wise performance data to allocate marketing and infrastructure budgets.

---

## 8. Limitations & Assumptions

* Analysis is based on aggregated public data
* Individual user-level behavior is not available
* Real-time transaction dynamics are outside scope
* Findings are directional, not predictive

---

## 9. Tools & Technologies Used

* **Python** – Data processing, analysis, visualization
* **SQL** – Analytical querying and aggregation
* **Streamlit** – Dashboard and insight presentation
* **Matplotlib** – Static visualizations
* **Git & GitHub** – Version control and collaboration

---

## 10. How to Run the Dashboard

```bash
# Activate virtual environment
source venv/bin/activate

# Run Streamlit app
streamlit run streamlit_app/app.py
```

---

## 11. Conclusion

This project demonstrates a **full analytics lifecycle** - from raw data to executive insight - following industry best practices.
It is structured to be **auditable, extensible, and presentation-ready**, making it suitable for real-world analytics and decision support scenarios.

---

**Author**: Sai Sadhasivam
**Domain**: Data Analytics | Digital Payments | Business Intelligence
