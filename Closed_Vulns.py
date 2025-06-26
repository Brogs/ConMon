import pandas as pd

# Load the CSV files
old = pd.read_csv("Old_Findings.csv", dtype=str)
new = pd.read_csv("Latest-POAM_TU_instances.csv", dtype=str)

# Clean and normalize 'Weakness Name' column for reliable comparison
old["Weakness Name"] = old["Weakness Name"].str.strip().str.upper()
new["Weakness Name"] = new["Weakness Name"].str.strip().str.upper()

# Create sets of unique weakness names
old_set = set(old["Weakness Name"].dropna().unique())
new_set = set(new["Weakness Name"].dropna().unique())

# Identify closed findings (in old but not in new)
closed = old[old["Weakness Name"].isin(old_set - new_set)]

# Optional: Show counts by risk rating if available
if "Original Risk Rating" in closed.columns:
    print("\n📉 Closed Findings by Original Risk Rating:\n")
    print(closed["Original Risk Rating"].str.strip().value_counts())

# Summary and save
print(f"\n✅ Closed findings identified: {len(closed)}")
if not closed.empty:
    closed.to_csv("closed_findings.csv", index=False)
    print("Saved closed results to 'closed_findings.csv'")
else:
    print("No closed findings detected.")
