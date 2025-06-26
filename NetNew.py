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

# Identify net new weaknesses in the new report
net_new = new[new["Weakness Name"].isin(new_set - old_set)]

print(net_new["Original Risk Rating"].value_counts())

# Show summary and save results
print(f"Net new entries found: {len(net_new)}")
if len(net_new) > 0:
    net_new.to_csv("net_new_findings.csv", index=False)
    print("Saved net new results to 'net_new_findings.csv'")
else:
    print("No net new findings detected.")
