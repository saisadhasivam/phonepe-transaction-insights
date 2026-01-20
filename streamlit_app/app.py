import streamlit as st
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="PhonePe Transaction Dashboard",
    layout="wide"
)

st.title("📊 PhonePe Transaction Dashboard")

st.markdown(
    "### Precomputed Insights (Static Visualizations)"
)

# --------------------------------------------------
# IMAGE DIRECTORY
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
IMAGE_DIR = BASE_DIR / "python_analysis" / "visualization"

# --------------------------------------------------
# HELPER FUNCTION
# --------------------------------------------------
def show_image(title: str, filename: str):
    st.subheader(title)
    img_path = IMAGE_DIR / filename

    if img_path.exists():
        st.image(str(img_path))
    else:
        st.error(f"❌ Image not found: {filename}")

# --------------------------------------------------
# DASHBOARD SECTIONS
# --------------------------------------------------

show_image(
    "📈 Yearly Transaction Growth",
    "yearly_transaction_growth.png"
)

show_image(
    "👥 User Growth Over Time",
    "user_growth.png"
)

show_image(
    "💳 Transaction Type Distribution",
    "transaction_type_distribution.png"
)

show_image(
    "🏆 Top 10 States by Revenue",
    "top_10_states_revenue.png"
)

show_image(
    "🛡️ Insurance Transaction Growth",
    "insurance_growth.png"
)

# --------------------------------------------------
# SUCCESS MESSAGE
# --------------------------------------------------
st.success("✅ Dashboard loaded successfully")
