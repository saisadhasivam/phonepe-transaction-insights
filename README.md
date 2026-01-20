# PhonePe Transaction Insights

This project analyzes PhonePe Pulse data using SQL, Python, and Streamlit.

The goal is to extract insights on transactions, user engagement, and insurance adoption across India.

## Business Insights & Interpretation

### 1. Yearly Transaction Growth

The visualization shows a consistent year-on-year increase in transaction value across India.
This indicates strong adoption of digital payments and increasing trust in PhonePe as a transaction platform.
The growth acceleration after 2020 suggests a significant shift toward cashless payments post-pandemic.

### 2. Top 10 States Contributing to Revenue

A small number of states contribute a disproportionately large share of total transaction value.
States like Telangana, Karnataka, and Maharashtra dominate PhonePe revenue, indicating higher digital payment penetration and economic activity in these regions.
This highlights regional concentration and opportunities for expansion in underpenetrated states.

### 3. Dominant Transaction Types

Peer-to-peer payments contribute the highest transaction value, followed by merchant payments.
This indicates that PhonePe is primarily used for everyday personal transfers and retail usage rather than niche financial services.
Financial services and insurance transactions form a smaller but growing share.

### 4. User Adoption Trend

The number of registered users increases steadily each year, showing strong and sustained platform adoption.
There is no significant decline in any year, indicating low churn and increasing market acceptance.
This suggests PhonePe has achieved strong network effects.

### 5. Insurance Transaction Growth

Insurance transaction value shows noticeable growth in recent years.
Although smaller compared to payments, this trend indicates diversification beyond core payment services.
This suggests PhonePe is gradually expanding into financial product adoption.

## Streamlit Dashboard
- Built using Streamlit
- Displays precomputed insights as static visualizations
- Improves performance by avoiding live DB queries
- Run using:
  streamlit run streamlit_app/app.py

