from functools import reduce

#Data set
users = [
    {"id": 1, "name": "Alice", "age": 34, "country": "US", "salary": 120000, "active": True},
    {"id": 2, "name": "Bob", "age": 28, "country": "CA", "salary": 95000, "active": False},
    {"id": 3, "name": "Charlie", "age": 40, "country": "US", "salary": 135000, "active": True},
    {"id": 4, "name": "Diana", "age": 25, "country": "UK", "salary": 70000, "active": True},
    {"id": 5, "name": "Evan", "age": 38, "country": "US", "salary": 160000, "active": False},
]

"""
Section 1 — map() (Transformations)
"""

"""
Extract all user names

Output

["Alice", "Bob", "Charlie", "Diana", "Evan"]


Constraint: Use map() only.
"""
usernames = list(map(lambda x : x["name"], users))
print(usernames)

"""
Create a list of (name, salary) tuples

Output

[("Alice", 120000), ("Bob", 95000), ...]
"""
name_salary = list(map(lambda x : (x["name"], x["salary"]), users))
print(name_salary)

"""
Normalize salaries to thousands (e.g., 120 → 120)

Output

[120, 95, 135, 70, 160]

"""
thousands=list(map(lambda x : x["salary"]//1000, users))
print(thousands)


"""
Section 2 — filter() (Selection)
"""

"""
Get only active users

Output: list of dictionaries
"""
active_users = list(filter(lambda x : x["active"], users))
print(active_users)

"""
Users older than 30 AND active

Constraint: Single filter() call.
"""
active_users = list(filter(lambda x : x["age"] > 30 and x["active"], users))
print(active_users)

"""
US-based users earning more than $130k

Think: multiple conditions inside filter.

"""
us_based_high_salary = list(filter(lambda x : x["country"] == "US" and x["salary"] > 130000, users))
print(us_based_high_salary)

"""
Section 3 — sorted() (Ordering)
"""

"""
7️Sort users by salary (ascending)
"""

sorted_by_salaries = list(sorted(users, key= lambda x : x["salary"] ))
print(sorted_by_salaries)

"""
Sort users by age (descending)
"""
sorted_by_age = list(sorted(users, key = lambda x : x["age"]))
print(sorted_by_age)

"""
Sort by country, then salary descending
"""
sorted_by_age = list(sorted(sorted(users, key = lambda x : x["country"]), key = lambda x:x["salary"], reverse=True))
print(sorted_by_age)

"""
Section 4 — reduce() (Aggregation)
"""

"""
from functools import reduce

Total payroll cost

Output

580000
"""
total_payroll = reduce(lambda x, y: x+y, map(lambda x:x["salary"], users))
print(total_payroll)

"""
Total salary of active users only

Constraint: combine filter() + reduce()
"""
total_payroll_active = reduce(lambda x, y: x+y, map(lambda x:x["salary"], filter(lambda x:x["active"],users)))
print(total_payroll_active)

"""
Find highest-paid user
"""
highest_paid_user = max(users, key = lambda x:x["salary"])
print(highest_paid_user)

"""
Section 5 — Combined (Interview-Style)
"""

"""
Average salary of US-based active users
"""
total_payroll_active_us_based = reduce(lambda x, y: x+y, map(lambda x:x["salary"], filter(lambda x:x["active"] and x["country"] == "US",users)))
print(total_payroll_active_us_based)


"""
Create a dict keyed by country with total salary
"""
def get_total_salary_by_country(code):
    return list(map(lambda x:x["salary"], filter(lambda x:x["country"] == code, users)))

total_salary_by_country = {
    "US": reduce(lambda x,y:x+y, get_total_salary_by_country("US")),
    "CA": reduce(lambda x,y:x+y, get_total_salary_by_country("CA")),
    "UK": reduce(lambda x,y:x+y, get_total_salary_by_country("UK"))
}
print(total_salary_by_country)

"""
Detect salary outliers
"""
salary_outlier = list(map(lambda x : x["name"], filter(lambda x:x["salary"] > (total_payroll / len(users))*1.3, users)))
print(salary_outlier)

"""
Detect salary outliers
"""
index = reduce(
    lambda acc, u: {**acc, u["id"]: {"name": u["name"], "age": u["age"]}},
    users,
    {}
)

print(index)