import streamlit as st

st.set_page_config(page_title="YTM Hub", layout="wide")

# Background Image CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("home_bg.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title + Subtitle with Overlay
st.markdown(
    """
    <div style='background-color: rgba(0, 0, 0, 0.5); padding: 30px 10px; border-radius: 10px; text-align: center;'>
        <h1 style='font-size: 42px; color: white;'>📈 Yield to Maturity (YTM) Hub</h1>
        <p style='font-size: 20px; color: lightgray;'>Your one-stop platform for accurate bond yield calculations.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Optional header image
# st.image("https://img.freepik.com/free-vector/investment-data-analytics-dashboard-finance-report_107791-17059.jpg", use_column_width=True)

st.markdown("---")

# Styled cards in 3 columns
card_style = """
    <div style="background-color: #1e1e1e; padding: 20px; border-radius: 10px; 
                box-shadow: 0 4px 10px rgba(0,0,0,0.4); transition: 0.3s; height: 220px;">
        <h3 style="color: white;">{title}</h3>
        <p style="color: #bbb;">{desc}</p>
        <a href="{link}" style="color: #00c4ff; font-weight: bold;">Go →</a>
    </div>
"""

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(card_style.format(
        title="📄 Time-based YTM",
        desc="Use simplified cash flows over fixed periods to estimate yield.",
        link="/time_in_years"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(card_style.format(
        title="📅 Date-based YTM",
        desc="Upload CSVs with real bond dates for precision YTM computation.",
        link="/date_based"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(card_style.format(
        title="🔎 Bond Finder",
        desc="Search bonds by ISIN or issuer, and quickly estimate their return.",
        link="/bond_finder"
    ), unsafe_allow_html=True)