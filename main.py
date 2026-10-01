import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Sales Analysis", layout="wide")
st.title("Project 1: Time Series & Category Charts")
st.write("Exploratory Data Analysis and Visualization on Sales Data")

# 1. Sample Dataset
np.random.seed(42)
dates = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")
categories = ["Electronics", "Clothing", "Home & Kitchen", "Books"]

data = {
    "Date": np.random.choice(dates, size=1000),
    "Category": np.random.choice(categories, size=1000, p=[0.4, 0.25, 0.2, 0.15]),
    "Sales": np.random.randint(20, 500, size=1000),
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").reset_index(drop=True)

# -------------------------------------------------------------
# Chart 1: Time Series Plot
# -------------------------------------------------------------
st.subheader("1. Monthly Sales Trend (Line Chart)")
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()
monthly_sales["Month"] = monthly_sales["Month"].astype(str)

fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(monthly_sales["Month"], monthly_sales["Sales"], marker="o", color="#1f77b4", linewidth=2.5)
ax1.set_title("Monthly Sales Trend (2025)", fontsize=14, fontweight="bold")
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Total Sales ($)", fontsize=12)
plt.xticks(rotation=45)
st.pyplot(fig1)

# -------------------------------------------------------------
# Chart 2 & 3: Category Charts side-by-side
# -------------------------------------------------------------
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False).reset_index()

col1, col2 = st.columns(2)

with col1:
    st.subheader("2. Total Sales by Category (Bar Chart)")
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    sns.barplot(data=category_sales, x="Category", y="Sales", palette="viridis", ax=ax2)
    ax2.set_title("Sales by Category", fontsize=14, fontweight="bold")
    ax2.set_xlabel("Category", fontsize=12)
    ax2.set_ylabel("Total Sales ($)", fontsize=12)
    st.pyplot(fig2)

with col2:
    st.subheader("3. Sales Share by Category (Pie Chart)")
    fig3, ax3 = plt.subplots(figsize=(6, 5))
    ax3.pie(
        category_sales["Sales"],
        labels=category_sales["Category"],
        autopct="%1.1f%%",
        startangle=140,
        colors=sns.color_palette("pastel"),
        explode=[0.05, 0, 0, 0]
    )
    ax3.set_title("Distribution by Category", fontsize=14, fontweight="bold")
    st.pyplot(fig3)
