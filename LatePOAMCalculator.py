import pandas as pd
from datetime import datetime

# Load the CSV file
df = pd.read_csv("POAM.csv", dtype=str)

# Normalize column names
df.columns = df.columns.str.strip()

# Parse Scheduled Completion Date
df["Scheduled Completion Date"] = pd.to_datetime(df["Scheduled Completion Date"], errors="coerce")

# Today's date
today = pd.to_datetime(datetime.today().date())

# Get only late entries
late = df[df["Scheduled Completion Date"] < today].dropna(subset=["Scheduled Completion Date"])

print(f"\n📅 Late POA&M items: {len(late)}")
print(late["Original Risk Rating"].value_counts())

if not late.empty:
    late.to_csv("POAM_Late_Findings.csv", index=False)
    print("✅ Saved late findings to POAM_Late_Findings.csv")

    if "Severity" in late.columns:
        # Normalize severity values
        late["Severity"] = late["Severity"].str.strip().str.title()

        # Show all unique values (debug)
        print("\n🔍 Unique Severities Found:", late["Severity"].unique())

        severity_order = ["High", "Moderate", "Low"]

        print("\n🛡️ Detailed Late Findings by Severity:\n")
        for level in severity_order:
            group = late[late["Severity"] == level]
            if not group.empty:
                print(f"\n🔴 {level} Severity - {len(group)} Finding(s):")
                print(group.to_string(index=False))
    else:
        print("⚠️ Column 'Severity' not found in data.")
else:
    print("✅ No late findings found.")
