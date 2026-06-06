##GROUPBY

# groupby() by a single column
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

df=pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

team=df.groupby('Team')
print(team.first())

# groupby() by multiple columns
aggregated_data = df.groupby(['Team', 'Position']).agg(
    total_salarys=('Salary', 'sum'),
    average_salarys=('Salary', 'mean'),
    player_count=('Name', 'count')
)

print(aggregated_data)


# pivot
import pandas as pd
employees = pd.read_csv("day_11/emp.csv")
salary = pd.read_csv("day_11/salary.csv")

merged_data = pd.merge(employees, salary, on="ID")
print(merged_data)

#by inner merge()

import pandas as pd

employees = pd.read_csv("day_11/emp.csv")
salary = pd.read_csv("day_11/salary.csv")

merged_data = pd.merge(employees, salary, on="ID", how="inner")
print(merged_data)
     ## from the result ofinner merge() only the common records are merged and displayed.IDs 1, 2, and 3 appear in both files, so they are included.
     ## IDs 4 and 5 are not included because they are only present in one of the files.

## by right merge()

import pandas as pd

employees = pd.read_csv("day_11/emp.csv")
salary = pd.read_csv("day_11/salary.csv")

merged_data = pd.merge(employees, salary, on="ID", how="right")
print(merged_data)

## by left merge()

import pandas as pd

employees = pd.read_csv("day_11/emp.csv")
salary = pd.read_csv("day_11/salary.csv")

merged_data = pd.merge(employees, salary, on="ID", how="left")
print(merged_data)

## by outer merge()

import pandas as pd

employees = pd.read_csv("day_11/emp.csv")
salary = pd.read_csv("day_11/salary.csv")

merged_data = pd.merge(employees, salary, on="ID", how="outer")
print(merged_data)

## groupby() and merge() together

dept_salary = merged_data.groupby("Department")["Salary"].mean()

print(dept_salary)

### Pivot

import pandas as pd

df = pd.read_csv("day_11/hotel_bookings.csv")

pivot_table = df.pivot_table(
    index="hotel",
    columns="market_segment",
    values="adr",
    aggfunc="mean"
)

print(pivot_table)

## pivot with groupby

df.groupby("hotel")["is_canceled"].mean()



