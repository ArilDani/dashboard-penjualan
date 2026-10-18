import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="DigiMart Analytics", page_icon="📊", layout="wide")
st.title("DigiMart Sales Dashboard")
st.caption("From Raw Data to Business Insight")

df = pd.read_csv("digimart_clean.csv")
df["order_date"] = pd.to_datetime(df["order_date"])

st.sidebar.header("Dashboard Filters")
cities = st.sidebar.multiselect("Select City", sorted(df["city"].unique()),
                                default=sorted(df["city"].unique()))
categories = st.sidebar.multiselect("Select Category", sorted(df["category"].unique()),
                                    default=sorted(df["category"].unique()))
filtered = df[df["city"].isin(cities) & df["category"].isin(categories)]

c1, c2, c3 = st.columns(3)
c1.metric("Total Revenue", f"Rp{filtered['revenue'].sum():,.0f}")
c2.metric("Units Sold", f"{filtered['quantity'].sum():,}")
c3.metric("Transactions", f"{filtered['order_id'].nunique():,}")

category_data = filtered.groupby("category", as_index=False)["revenue"].sum()
product_data = filtered.groupby("product", as_index=False)["quantity"].sum()
daily_data = filtered.groupby("order_date", as_index=False)["revenue"].sum()

left, right = st.columns(2)
with left:
    st.plotly_chart(px.bar(category_data, x="category", y="revenue",
                           title="Revenue by Category"), use_container_width=True)
with right:
    st.plotly_chart(px.bar(product_data, x="product", y="quantity",
                           title="Units Sold by Product"), use_container_width=True)

st.plotly_chart(px.line(daily_data, x="order_date", y="revenue",
                        markers=True, title="Daily Revenue Trend"),
                use_container_width=True)
st.subheader("Transaction Details")
st.dataframe(filtered, use_container_width=True)
st.download_button("Download Filtered Data",
                   data=filtered.to_csv(index=False),
                   file_name="digimart_filtered.csv",
                   mime="text/csv")
