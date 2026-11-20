
import numpy as np

# Marks of 4 students in 3 subjects
marks = np.array([
    [80, 75, 90],
    [65, 70, 85],
    [90, 88, 92],
    [72, 78, 80]
])

print("Array shape:", marks.shape)

# Average marks for each student
student_avg = np.mean(marks, axis=1)
print("Student averages:", student_avg)

# Average marks for each subject
subject_avg = np.mean(marks, axis=0)
print("Subject averages:", subject_avg)

# Add 5 grace marks
grace_marks = marks + 5
print("Marks after grace:", grace_marks)

# Calculate weighted scores
weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(marks, weights)
print("Weighted scores:", weighted_scores)

import pandas as pd
from pathlib import Path

# Load employee data
data_folder = Path(__file__).resolve().parent.parent / "data"
df = pd.read_csv(data_folder / "employees.csv")

print("\nEmployee Information:")
df.info()

print("\nSalary Statistics:")
print(df.describe())

# Select rows using loc and iloc
print("\nFirst employee using loc:")
print(df.loc[0])

print("\nFirst employee using iloc:")
print(df.iloc[0])

# Filter employees earning above 50000
high_salary = df[df["salary"] > 50000]

print("\nEmployees earning above 50000:")
print(high_salary[["name", "salary"]])

# Create a separate working copy for data cleaning
dirty_df = df.copy()

# Add two missing salaries
dirty_df.loc[0, "salary"] = None
dirty_df.loc[1, "salary"] = None

# Add one duplicate row
dirty_df = pd.concat([dirty_df, dirty_df.iloc[[2]]], ignore_index=True)

print("\nBefore cleaning:")
print("Missing salaries:", dirty_df["salary"].isna().sum())
print("Duplicate rows:", dirty_df.duplicated().sum())

# Fill missing salaries using the median
median_salary = dirty_df["salary"].median()
dirty_df["salary"] = dirty_df["salary"].fillna(median_salary)

# Remove duplicate rows
clean_df = dirty_df.drop_duplicates().copy()

# Correct data types
clean_df["id"] = clean_df["id"].astype(int)
clean_df["salary"] = clean_df["salary"].astype(float)

print("\nAfter cleaning:")
print("Missing salaries:", clean_df["salary"].isna().sum())
print("Duplicate rows:", clean_df.duplicated().sum())
print(clean_df)

# Department-wise salary summary
department_summary = df.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)

print("\nDepartment Summary:")
print(department_summary)

# Load department details
departments = pd.read_csv(data_folder / "departments.csv")

# Inner join: only matching departments
inner_join = pd.merge(df, departments, on="department", how="inner")
print("\nInner Join:")
print(inner_join)

# Left join: keep all departments, even without employees
left_join = pd.merge(departments, df, on="department", how="left")
print("\nLeft Join:")
print(left_join)

# Outer join: keep records from both tables
outer_join = pd.merge(df, departments, on="department", how="outer")
print("\nOuter Join:")
print(outer_join)

# Find departments without employees
no_employees = departments[
    ~departments["department"].isin(df["department"])
]

print("\nDepartments without employees:")
print(no_employees["department"].tolist())

import matplotlib.pyplot as plt

# Create the reports folder if it does not exist
reports_folder = data_folder.parent / "reports"
reports_folder.mkdir(exist_ok=True)

# 1. Bar chart - employee count by department
department_counts = df["department"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(department_counts.index, department_counts.values, label="Employees")
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig(reports_folder / "department_bar.png")
plt.close()

# 2. Histogram - salary distribution
plt.figure(figsize=(8, 5))
plt.hist(df["salary"], bins=5, edgecolor="black", label="Salaries")
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig(reports_folder / "salary_histogram.png")
plt.close()

# 3. Scatter plot - employee ID and salary
plt.figure(figsize=(8, 5))
plt.scatter(df["id"], df["salary"], label="Employee Salary")
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig(reports_folder / "salary_scatter.png")
plt.close()

# 4. Line chart - average salary by department
average_salaries = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
plt.plot(
    average_salaries.index,
    average_salaries.values,
    marker="o",
    label="Average Salary"
)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()
plt.tight_layout()
plt.savefig(reports_folder / "average_salary_line.png")
plt.close()

print("\nAll four charts saved successfully!")

# One insight for each chart
print("\nChart Insights:")
print("1. Bar: IT has the most employees (3).")
print("2. Histogram: Salaries range from 30000 to 90000.")
print("3. Scatter: Employee 5 has the highest salary (90000).")
print("4. Line: Finance has the highest average salary (90000).")
