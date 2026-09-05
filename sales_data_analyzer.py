# Sales Data Analyzer

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": [
        "Laptop",
        "Phone",
        "Tablet",
        "Laptop",
        "Phone",
        "Tablet"
    ],
    "Sales": [
        75000,
        50000,
        30000,
        90000,
        60000,
        40000
    ]
}

df = pd.DataFrame(data)

print("===== SALES DATA =====")
print(df)

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()

product_sales = df.groupby("Product")["Sales"].sum()

best_product = product_sales.idxmax()

print("\n===== SALES ANALYSIS =====")
print("Total Sales:", total_sales)
print("Average Sale:", round(average_sales, 2))
print("Best Selling Product:", best_product)

print("\n===== PRODUCT-WISE SALES =====")
print(product_sales)

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()