#!/usr/bin/env python
# coding: utf-8

# # Employee Data Analysis
# 
# ## Week 1 Python and Data Engineering Assessment
# 
# This notebook explores employee data using NumPy and Pandas.
# It includes data analysis, data cleaning, and performance testing.

# In[1]:


import numpy as np
import pandas as pd

print("NumPy and Pandas imported successfully!")


# ## Employee Data Analysis
# 
# Load the employee dataset and calculate department-wise statistics.

# 

# In[3]:


from pathlib import Path

# Find the employee CSV file
data_path = Path.cwd().parent / "data" / "employees.csv"

# Load employee data
employees = pd.read_csv(data_path)

print("Total employees:", len(employees))
print(employees.head())

# Department-wise employee count and average salary
summary = employees.groupby("department").agg(
    employee_count=("id", "count"),
    average_salary=("salary", "mean")
)

print(summary)


# ## Performance Testing
# 
# Measure how quickly Pandas calculates the average employee salary.

# 

# In[ ]:


# Measure the execution time
print("Average salary:", employees["salary"].mean())
