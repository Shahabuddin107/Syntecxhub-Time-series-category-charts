import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Style set karna
sns.set_theme(style="whitegrid")

# 1. Sample Dataset Banana
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
# Chart 1: Time Series Plot (Monthly Sales Trend)
# -------------------------------------------------------------
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()
monthly_sales["Month"] = monthly_sales["Month"].astype(str)

plt.figure(figsize=(10, 5))
plt.plot(
    monthly_sales["Month"],
    monthly_sales["Sales"],
    marker="o",
    color="#1f77b4",
    linewidth=2.5,
)
plt.title("Monthly Sales Trend (2025)", fontsize=14, fontweight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=300)
plt.close()
print("Saved: monthly_sales_trend.png")

# -------------------------------------------------------------
# Chart 2: Category Bar Chart (Comparison)
# -------------------------------------------------------------
category_sales = (
    df.groupby("Category")["Sales"].sum().sort_values(ascending=False).reset_index()
)

plt.figure(figsize=(8, 5))
sns.barplot(
    data=category_sales,
    x="Category",
    y="Sales",
    hue="Category",
    palette="viridis",
    legend=False,
)
plt.title("Total Sales by Category", fontsize=14, fontweight="bold")
plt.xlabel("Category", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.tight_layout()
plt.savefig("category_sales_bar.png", dpi=300)
plt.close()
print("Saved: category_sales_bar.png")

# -------------------------------------------------------------
# Chart 3: Category Share (Pie Chart)
# -------------------------------------------------------------
plt.figure(figsize=(7, 7))
plt.pie(
    category_sales["Sales"],
    labels=category_sales["Category"],
    autopct="%1.1f%%",
    startangle=140,
    colors=sns.color_palette("pastel"),
    explode=[0.05, 0, 0, 0],
)
plt.title("Sales Distribution by Category", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("category_share_pie.png", dpi=300)
plt.close()
print("Saved: category_share_pie.png")

print("All charts generated successfully!")