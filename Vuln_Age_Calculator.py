Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: D:\Users\kyle.brogan\Desktop\Python Automations\Calculate age of vulnerabilities\Vuln_Age_Calculator.py

Warning (from warnings module):
  File "D:\Users\kyle.brogan\Desktop\Python Automations\Calculate age of vulnerabilities\Vuln_Age_Calculator.py", line 32
    grouped = df.groupby(["Time Bucket", "Original Risk Rating"]).size().unstack(fill_value=0)
FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.

📊 POA&M Risk Rating Counts by Time Bucket (Detection ➜ Completion):

Original Risk Rating  High  Low  Medium
Time Bucket                            
0-30 days                8    0       0
31-60 days              89    0       0
61-90 days               0    0      71
91-180 days              0    1     338

🧮 Totals for each Risk Rating across all time buckets:
Original Risk Rating
High       97
Low         1
Medium    409
dtype: int64

🔁 Cross-Check: Total Count of Original Risk Ratings (All Rows)

Original Risk Rating
Medium    409
High       97
Low        19
Name: count, dtype: int64

==================================== RESTART: D:\Users\kyle.brogan\Desktop\Python Automations\Calculate age of vulnerabilities\Vuln_Age_Calculator.py ===================================

Warning (from warnings module):
  File "D:\Users\kyle.brogan\Desktop\Python Automations\Calculate age of vulnerabilities\Vuln_Age_Calculator.py", line 32
    grouped = df.groupby(["Time Bucket", "Original Risk Rating"]).size().unstack(fill_value=0)
FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.

📊 POA&M Risk Rating Counts by Time Bucket (Detection ➜ Completion):

Original Risk Rating  High  Low  Medium
Time Bucket                            
0-30 days                8    0       0
31-60 days              89    0       0
61-90 days               0    0      71
91-180 days              0    1     338

🧮 Totals for each Risk Rating across all time buckets:
Original Risk Rating
High       97
Low         1
Medium    409
dtype: int64

🔁 Cross-Check: Total Count of Original Risk Ratings (All Rows)

Original Risk Rating
Medium    409
High       97
Low        19
Name: count, dtype: int64

==================================== RESTART: D:\Users\kyle.brogan\Desktop\Python Automations\Calculate age of vulnerabilities\Vuln_Age_Calculator.py ===================================

Warning (from warnings module):
  File "D:\Users\kyle.brogan\Desktop\Python Automations\Calculate age of vulnerabilities\Vuln_Age_Calculator.py", line 32
    grouped = df.groupby(["Time Bucket", "Original Risk Rating"]).size().unstack(fill_value=0)
FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.

📊 POA&M Risk Rating Counts by Time Bucket (Detection ➜ Completion):

Original Risk Rating  High  Low  Medium
Time Bucket                            
0-30 days                8    0       0
31-60 days              89    0       0
61-90 days               0    0      71
91-180 days              0    1     338

🧮 Totals for each Risk Rating across all time buckets:
Original Risk Rating
High       97
Low         1
Medium    409
dtype: int64

🔁 Cross-Check: Total Count of Original Risk Ratings (All Rows)

Original Risk Rating
Medium    409
High       97
Low        19
Name: count, dtype: int64

✅ Verifying Totals Match:
✔️ 'High' OK: 97
✔️ 'Moderate' OK: 0
❌ MISMATCH for 'Low': Grouped = 1, Full = 19

⚠️ Discrepancies found — check time bucket logic or missing data.

==================================== RESTART: D:\Users\kyle.brogan\Desktop\Python Automations\Calculate age of vulnerabilities\Vuln_Age_Calculator.py ===================================

Warning (from warnings module):
  File "D:\Users\kyle.brogan\Desktop\Python Automations\Calculate age of vulnerabilities\Vuln_Age_Calculator.py", line 32
    grouped = df.groupby(["Time Bucket", "Original Risk Rating"]).size().unstack(fill_value=0)
FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.

📊 POA&M Risk Rating Counts by Time Bucket (Detection ➜ Completion):

Original Risk Rating  High  Low  Medium
Time Bucket                            
0-30 days                8    0       0
31-60 days              89    0       0
61-90 days               0    0      71
91-180 days              0    1     338

🧮 Totals for each Risk Rating across all time buckets:
Original Risk Rating
High       97
Low         1
Medium    409
dtype: int64

🔁 Cross-Check: Total Count of Original Risk Ratings (All Rows)

Original Risk Rating
Medium    409
High       97
Low        19
Name: count, dtype: int64

✅ Verifying Totals Match:
✔️ 'High' OK: 97
✔️ 'Medium' OK: 409
❌ MISMATCH for 'Low': Grouped = 1, Full = 19

⚠️ Discrepancies found — check time bucket logic or missing data.
