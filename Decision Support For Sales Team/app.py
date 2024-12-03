import streamlit as st
import pandas as pd
import plotly.express as px

# Load data directly from Excel
@st.cache_data
def load_data():
    file_path = "/dataset/1-sales_records.xlsx"  # Adjust the path to your file
    data = pd.read_excel(file_path, sheet_name="Orders")
    return data

# Load data
orders_data = load_data()

# Streamlit app
st.title("Sales Dashboard 💹💹💹")

# Sales Trends
st.header("Sales Trends Over Years")
sales_trends = orders_data.groupby("year")["sales"].sum().reset_index()
fig_sales = px.line(sales_trends, x="year", y="sales", title="Yearly Sales Trend")
st.plotly_chart(fig_sales)

# Top Products by Sales
st.header("Top 5 Products by Sales")
top_products = orders_data.groupby("product_name")["sales"].sum().nlargest(5).reset_index()
fig_top_products = px.bar(
    top_products,
    x="product_name",
    y="sales",
    title="Top 5 Products by Sales",
    labels={"sales": "Sales ($)", "product_name": "Product"}
)
st.plotly_chart(fig_top_products)

# Shipment Mode
st.header("Most Common Shipment Mode")
ship_mode_counts = orders_data["ship_mode"].value_counts().reset_index()
ship_mode_counts.columns = ["ship_mode", "count"]  # Rename columns for clarity
fig_ship_mode = px.pie(
    ship_mode_counts, 
    names="ship_mode", 
    values="count", 
    title="Shipment Mode Distribution"
)
st.plotly_chart(fig_ship_mode)

# Profitability
st.header("Top Profitable Categories and Subcategories")
profitability = orders_data.groupby(["category", "sub_category"])["profit"].sum().nlargest(5).reset_index()
fig_profitability = px.bar(
    profitability,
    x="sub_category",
    y="profit",
    color="category",
    title="Top 5 Profitable Categories/Subcategories",
    labels={"profit": "Profit ($)", "sub_category": "Subcategory"}
)
st.plotly_chart(fig_profitability)

st.write("Explore more insights by modifying filters or adding new visualizations!")
