from datetime import datetime
import streamlit as st
import re

st.title("🔎 Find Bond by ISIN or Issuer Name")

# Input field
user_input = st.text_input("Enter ISIN or Issuer Name")

# Basic ISIN pattern (India-specific)
isin_pattern = r"^INE[A-Z0-9]{9}$"

if user_input:
    user_input_clean = user_input.strip()
    
    if re.match(isin_pattern, user_input_clean):
        # ISIN input → direct to details page
        search_url = f"https://dev.meradhan.co/bonds/details/{user_input_clean}"
        label = f"🔗 View {user_input_clean} on Meradhan"
    else:
        # Issuer input → redirect to search
        search_term = user_input_clean.replace(" ", "+")
        search_url = f"https://dev.meradhan.co/bonds?search={search_term}"
        label = "🔎 Search Bonds by Issuer on Meradhan"
    
    st.markdown(
        f'<a href="{search_url}" target="_blank" rel="noopener">{label}</a>',
        unsafe_allow_html=True
    )

# Divider and optional YTM calculator
st.divider()

st.subheader("💼 Quick YTM Estimator (Optional)")

coupon_rate = st.number_input("Coupon Rate (% annually)", min_value=0.0)
face_value = st.number_input("Face Value (₹)", min_value=0.0)

# Custom maturity date input
date_str = st.text_input("Enter Maturity Date (DD-MMM-YYYY)", placeholder="e.g., 06-Jul-2027")

price = st.number_input("Current Market Price (₹)", min_value=0.0)

if st.button("Estimate YTM"):
    try:
        # Parse date from string
        maturity_date = datetime.strptime(date_str, "%d-%b-%Y").date()

        coupon = (coupon_rate / 100) * face_value
        today = datetime.today().date()
        days_to_maturity = (maturity_date - today).days
        years = days_to_maturity / 365

        if years <= 0:
            st.error("Maturity date must be in the future.")
        else:
            ytm_approx = (coupon + (face_value - price) / years) / ((face_value + price) / 2)
            st.success(f"📈 Approximate YTM: {ytm_approx * 100:.2f}%")
    except ValueError:
        st.error("❌ Invalid date format. Use DD-MMM-YYYY (e.g., 06-Jul-2027)")