
import csv
import json
from pathlib import Path

data_folder = Path(__file__).resolve().parent.parent / "data"

# Read employee records
with open(data_folder / "employees.csv", "r", newline="") as file:
    employees = list(csv.DictReader(file))

print("Rows read:", len(employees))

# Save employee data as JSON
with open(data_folder / "employees.json", "w") as file:
    json.dump(employees, file, indent=4)

# Find employees earning above 50000
high_earners = [
    employee for employee in employees
    if int(employee["salary"]) > 50000
]

print("High earners:", len(high_earners))

# Save high earners as CSV
with open(data_folder / "high_earners.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(high_earners)


import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")

print("API key loaded:", api_key is not None)

# Get user data from the API
url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    users = response.json()

    for user in users[:3]:
        print(user["id"], "-", user["name"], "-", user["email"])

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Could not connect to the API")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

# Check the API response for a missing user
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        response.raise_for_status()

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Could not connect to the API")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)


# Extract nested user information and save it
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )
    response.raise_for_status()

    users = response.json()

    user_details = []

    for user in users:
        address = user.get("address", {})
        company = user.get("company", {})

        user_details.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": address.get("city"),
            "company": company.get("name")
        })

    with open(data_folder / "users.json", "w") as file:
        json.dump(user_details, file, indent=4)

    print("User details saved to users.json")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Could not connect to the API")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)
