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

                import numpy as np
                import matplotlib.pyplot as plt

                st.subheader("📉 Bond Price vs YTM Curve")

                ytm_range = np.linspace(0.01, 0.20, 100)
                price_list = [
                    sum(cf / (1 + r) ** t for cf, t in zip(cash_flows, times))
                    for r in ytm_range
                ]

                fig, ax = plt.subplots(facecolor='#0e1117')
                ax.set_facecolor('#0e1117')
                ax.plot(ytm_range * 100, price_list, color='cyan', linewidth=2)
                ax.set_title("Price vs Yield to Maturity")
                ax.set_xlabel("Yield to Maturity (%)")
                ax.set_ylabel("Bond Price (₹)")
                ax.grid(True, linestyle='--', alpha=0.3, color='gray')
                ax.tick_params(colors='white')
                ax.xaxis.label.set_color('white')
                ax.yaxis.label.set_color('white')
                ax.title.set_color('white')

                st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Error: {e}")