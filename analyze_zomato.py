
import pandas as pd
from pathlib import Path

# File paths
DATA_FILE = r"C:\zomato.csv"
OUTPUT_DIR = Path(r"C:\Zomato_Restaurant_Analysis_Project\outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load original data
df = pd.read_csv(DATA_FILE)

print("Original dataset:", df.shape)

# Work on a copy
clean = df.copy()

# Standardize column names for easier coding
clean.columns = (
    clean.columns
    .str.strip()
    .str.lower()
    .str.replace(r"[^\w]+", "_", regex=True)
    .str.strip("_")
)

# Clean text fields
text_columns = clean.select_dtypes(include=["str", "object"]).columns

for col in text_columns:
    clean[col] = clean[col].str.strip()

# Convert ratings such as '4.1/5' to numeric values
clean["rate"] = (
    clean["rate"]
    .astype("string")
    .str.extract(r"(\d+(?:\.\d+)?)", expand=False)
)

clean["rate"] = pd.to_numeric(clean["rate"], errors="coerce")

# Convert approximate cost to numeric
clean["approx_cost_for_two_people"] = pd.to_numeric(
    clean["approx_cost_for_two_people"]
    .astype("string")
    .str.replace(",", "", regex=False),
    errors="coerce"
)

# Convert votes to numeric
clean["votes"] = pd.to_numeric(clean["votes"], errors="coerce")

# Standardize Yes/No fields
for col in ["online_order", "book_table"]:
    clean[col] = clean[col].str.title()

# Save cleaned dataset
clean.to_csv(OUTPUT_DIR / "zomato_cleaned.csv", index=False)

# Save data quality report
quality_report = pd.DataFrame({
    "missing_count": clean.isna().sum(),
    "missing_percent": (clean.isna().mean() * 100).round(2),
    "data_type": clean.dtypes.astype(str)
})

quality_report.to_csv(OUTPUT_DIR / "data_quality_report.csv")

print("\nCleaned dataset:", clean.shape)
print("\nMissing values after cleaning:")
print(clean.isnull().sum())

print("\nRating summary:")
print(clean["rate"].describe())

print("\nCleaned dataset and quality report saved successfully!")


# -------------------------------
# EXPLORATORY DATA ANALYSIS (EDA)
# -------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset for analysis
print("\nStarting Exploratory Data Analysis...")

# 1. Top 10 locations by restaurant listings
top_locations = clean["location"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_locations.values, y=top_locations.index)
plt.title("Top 10 Locations by Restaurant Listings")
plt.xlabel("Number of Listings")
plt.ylabel("Location")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_10_locations.png", dpi=300)
plt.show()

# 2. Rating distribution
plt.figure(figsize=(10, 6))
sns.histplot(clean["rate"].dropna(), bins=15, kde=True)
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Listings")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "rating_distribution.png", dpi=300)
plt.show()

# 3. Top 10 cuisines
cuisine_counts = (
    clean["cuisines"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 6))
sns.barplot(x=cuisine_counts.values, y=cuisine_counts.index)
plt.title("Top 10 Cuisines")
plt.xlabel("Number of Listings")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_10_cuisines.png", dpi=300)
plt.show()

# 4. Online ordering availability
order_counts = clean["online_order"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    order_counts.values,
    labels=order_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Online Ordering Availability")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "online_ordering.png", dpi=300)
plt.show()

print("\nEDA charts saved successfully!")



# -------------------------------
# ADVANCED RESTAURANT ANALYSIS
# -------------------------------

# 5. Average rating by online ordering availability
online_rating = clean.groupby("online_order")["rate"].mean().dropna()

plt.figure(figsize=(8, 5))
sns.barplot(x=online_rating.index, y=online_rating.values)
plt.title("Average Rating: Online Ordering vs No Online Ordering")
plt.xlabel("Online Ordering")
plt.ylabel("Average Rating")
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "rating_by_online_order.png", dpi=300)
plt.show()

# 6. Top 10 restaurant types
restaurant_types = (
    clean["rest_type"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 6))
sns.barplot(x=restaurant_types.values, y=restaurant_types.index)
plt.title("Top 10 Restaurant Types")
plt.xlabel("Number of Listings")
plt.ylabel("Restaurant Type")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_10_restaurant_types.png", dpi=300)
plt.show()

# 7. Votes vs Rating
votes_data = clean.dropna(subset=["rate", "votes"]).copy()

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=votes_data,
    x="votes",
    y="rate",
    alpha=0.35
)
plt.title("Restaurant Ratings vs Votes")
plt.xlabel("Number of Votes")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "votes_vs_rating.png", dpi=300)
plt.show()

print("\nAdvanced analysis charts saved successfully!")
