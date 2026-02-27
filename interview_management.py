import pandas as pd

# -----------------------------
# Load Excel file
# -----------------------------
file_path = "students_data.xlsx"
df = pd.read_excel(file_path)

print("\n===== Current Student Data =====")
print(df)

# -----------------------------
# Add New Student
# -----------------------------
new_student = {
    "StudentID": 121,
    "Name": "Rahul Verma",
    "Percentage": 88,
    "Result": "",
    "PlacementStatus": "Not Placed"
}

df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)

print("\nNew student added successfully!")

# -----------------------------
# Auto Calculate Result (Pass/Fail)
# -----------------------------
df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# -----------------------------
# Find Topper
# -----------------------------
topper = df.loc[df["Percentage"].idxmax()]

print("\n===== Topper Details =====")
print(topper)

# -----------------------------
# Summary Report
# -----------------------------
total_students = len(df)
pass_count = len(df[df["Result"] == "Pass"])
fail_count = len(df[df["Result"] == "Fail"])
placed_count = len(df[df["PlacementStatus"] == "Placed"])
not_placed_count = len(df[df["PlacementStatus"] == "Not Placed"])

print("\n===== Summary Report =====")
print(f"Total Students: {total_students}")
print(f"Pass Students: {pass_count}")
print(f"Fail Students: {fail_count}")
print(f"Placed Students: {placed_count}")
print(f"Not Placed Students: {not_placed_count}")

# -----------------------------
# Save Updated Excel
# -----------------------------
df.to_excel(file_path, index=False)

print("\nExcel file updated successfully!")