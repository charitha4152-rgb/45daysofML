## DATA TRANSFORMATION & FEATURE CREATION

import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("Day-12/property_data.csv")
print(df)

print("Original Shape:", df.shape)

# Handle Missing Values
df["Area_sqft"] = df["Area_sqft"].fillna(df["Area_sqft"].mean())
df["Bedrooms"] = df["Bedrooms"].fillna(df["Bedrooms"].median())
print(df.isnull().sum())

# Remove Duplicates

df = df.drop_duplicates()
print(df.duplicated().sum())

# Outlier Removal using IQR

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

df = df[
    (df["Price"] >= lower_limit) &
    (df["Price"] <= upper_limit)
]

print("Shape after outlier removal:", df.shape)

# Price per Square Foot
df["sqft_rate"] = df["Price"] / df["Area_sqft"]

# Total Rooms
df["total_rooms"] = df["Bedrooms"] + df["Bathrooms"]

# Price per Room
df["price_per_room"] = df["Price"] / df["total_rooms"]

# Luxury House Flag
df["luxury_house"] = np.where(df["Price"] > 10000000, 1, 0)
print(df[[
    "Price",
    "Area_sqft",
    "sqft_rate",
    "total_rooms",
    "price_per_room",
    "luxury_house"
]].head())

# Area Category
df["area_category"] = pd.cut(
    df["Area_sqft"],
    bins=[0, 1000, 2000, 5000],
    labels=["Small", "Medium", "Large"]
)
print(df["area_category"].value_counts())

# Encoding
df = pd.get_dummies(df, columns=["Location"], drop_first=True)
print(df.head())

# Normalization
df["Area_Normalized"] = (
    (df["Area_sqft"] - df["Area_sqft"].min())
    /
    (df["Area_sqft"].max() - df["Area_sqft"].min())
)
print(df[["Area_sqft", "Area_Normalized"]].head())

# Save File
df.to_csv("transformed_property_data.csv", index=False)

print("Transformation Completed!")
print(df.shape)
print(df.head())



