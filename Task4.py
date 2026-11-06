import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# TASK 4 : CUSTOMER DATA ANALYSIS
# --------------------------------------------------

data = pd.read_csv(
    "cleaned_data/sales_cleaned.csv"
)

print("\n========== CUSTOMER DATA ANALYSIS ==========")

# --------------------------------------------------
# CUSTOMER SUMMARY
# --------------------------------------------------

customer_summary = (
    data.groupby("CustomerID")
    .agg(
        TotalOrders=("OrderID", "count"),
        TotalQuantity=("Quantity", "sum"),
        TotalSales=("Sales", "sum"),
        AverageAge=("Age", "mean")
    )
    .reset_index()
)

print("\nCUSTOMER SUMMARY")
print(customer_summary)

# --------------------------------------------------
# TOP CUSTOMERS
# --------------------------------------------------

top_customers = (
    customer_summary
    .sort_values(
        "TotalSales",
        ascending=False
    )
    .head(10)
)

print("\nTOP 10 CUSTOMERS BY SALES")
print(top_customers)

# --------------------------------------------------
# CUSTOMER SEGMENT BY AGE
# --------------------------------------------------

def age_group(age):

    if age < 25:
        return "Young"

    elif age < 40:
        return "Adult"

    else:
        return "Senior"


data["AgeGroup"] = data["Age"].apply(age_group)

age_group_sales = (
    data.groupby("AgeGroup")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSALES BY AGE GROUP")
print(age_group_sales)

# --------------------------------------------------
# CUSTOMER SALES BY CITY
# --------------------------------------------------

city_customer_sales = (
    data.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCUSTOMER SALES BY CITY")
print(city_customer_sales)

# --------------------------------------------------
# MOST VALUABLE CUSTOMER GROUP
# --------------------------------------------------

best_age_group = age_group_sales.idxmax()

best_city = city_customer_sales.idxmax()

print("\n========== CUSTOMER INSIGHTS ==========")

print(
    "Most valuable age group:",
    best_age_group
)

print(
    "Highest purchasing city:",
    best_city
)

print(
    "Highest customer sales:",
    round(
        customer_summary["TotalSales"].max(),
        2
    )
)

# --------------------------------------------------
# VISUAL REPORT 1
# --------------------------------------------------

plt.figure(figsize=(8, 5))

age_group_sales.plot(kind="bar")

plt.title("Sales by Customer Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig(
    "visualizations/customer_age_groups.png"
)

plt.show()

# --------------------------------------------------
# VISUAL REPORT 2
# --------------------------------------------------

plt.figure(figsize=(9, 5))

city_customer_sales.plot(kind="bar")

plt.title("Customer Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "visualizations/customer_sales_by_city.png"
)

plt.show()

# --------------------------------------------------
# SAVE CUSTOMER ANALYSIS
# --------------------------------------------------

customer_summary.to_csv(
    "customer_analysis.csv",
    index=False
)

print("\nCUSTOMER ANALYSIS SAVED SUCCESSFULLY")
print("customer_analysis.csv")