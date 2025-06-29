import pandas as pd
from datetime import datetime

# Load the CSV
df = pd.read_csv("Latest-POAM_TU_instances.csv", dtype=str)
df.columns = df.columns.str.strip()

# Parse date columns
df["Original Detection Date"] = pd.to_datetime(df["Original Detection Date"], errors="coerce")
df["Scheduled Completion Date"] = pd.to_datetime(df["Scheduled Completion Date"], errors="coerce")

# Drop rows with missing or invalid dates
df = df.dropna(subset=["Original Detection Date", "Scheduled Completion Date"])

# Calculate time delta in days
df["Days Between"] = (df["Scheduled Completion Date"] - df["Original Detection Date"]).dt.days

# Define bins and labels
bins = [0, 30, 60, 90, 180]
labels = ["0-30 days", "31-60 days", "61-90 days", "91-180 days"]

# Assign buckets
df["Time Bucket"] = pd.cut(df["Days Between"], bins=bins, labels=labels, right=True)

# Normalize Original Risk Rating
df["Original Risk Rating"] = df["Original Risk Rating"].str.strip().str.title()

# Filter to just High/Moderate/Low
df = df[df["Original Risk Rating"].isin(["High", "Medium", "Low"])]

# Group and count
grouped = df.groupby(["Time Bucket", "Original Risk Rating"]).size().unstack(fill_value=0)

# Display results
print("\n📊 POA&M Risk Rating Counts by Time Bucket (Detection ➜ Completion):\n")
print(grouped)

# Totals calculated for previous table 
column_totals = grouped.sum(axis=0)
print("\n🧮 Totals for each Risk Rating across all time buckets:")
print(column_totals)

# Cross-check total Original Risk rating column for raw count check
print("\n🔁 Cross-Check: Total Count of Original Risk Ratings (All Rows)\n")
total_counts = df["Original Risk Rating"].value_counts()
print(total_counts)

# Compare bucketed totals vs full column totals
print("\n✅ Verifying Totals Match:")

errors_found = False
for rating in ["High", "Medium", "Low"]:
    grouped_count = column_totals.get(rating, 0)
    total_count = total_counts.get(rating, 0)
    
    if grouped_count != total_count:
        errors_found = True
        print(f"❌ MISMATCH for '{rating}': Grouped = {grouped_count}, Full = {total_count}")
    else:
        print(f"✔️ '{rating}' OK: {grouped_count}")

if not errors_found:
    print("\n✅ All totals match between grouped table and full dataset.")
else:
    print("\n⚠️ Discrepancies found — check time bucket logic or missing data.")

