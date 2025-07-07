import streamlit as st
import pandas as pd
from datetime import datetime
from ytm_solver import solve_ytm

st.title("📅 YTM Calculator – Date-based Cash Flows")

# Upload CSV file
uploaded_file = st.file_uploader("Upload Cash Flow CSV (with Dates)", type="csv")
price = st.number_input("Enter the Current Bond Price (₹)", min_value=0.0)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📊 Uploaded Cash Flows:", df)

    try:
        # Convert date column to datetime and calculate year difference from today
        df['Date'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
        df['Years'] = (df['Date'] - datetime.today()).dt.total_seconds() / (365.25 * 24 * 60 * 60)

        times = df['Years'].tolist()
        cash_flows = df['Cash Flow'].astype(float).tolist()

        # Guard clause for bond price
        if price <= 0:
            st.warning("Please enter a valid bond price greater than 0.")
        else:
            ytm = solve_ytm(cash_flows, times, price)
            if isinstance(ytm, str) and ytm.startswith("Error"):
                st.error(ytm)
            else:
                st.success(f"✅ Yield to Maturity: {ytm:.4f}%")

    except Exception as e:
        st.error(f"❌ Error: {e}")