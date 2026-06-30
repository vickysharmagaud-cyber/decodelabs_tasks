import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/raw_dataset.csv")

# Fill missing values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Verify Total Price
df["CalculatedPrice"] = df["Quantity"] * df["UnitPrice"]

# Save cleaned dataset
df.to_csv("data/cleaned_dataset.csv", index=False)

print("✅ Data Cleaning Completed Successfully!")