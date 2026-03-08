import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    salaries = employee['salary'].drop_duplicates().nlargest(2)
    
    if len(salaries) < 2:
        secSalary = None
    else:
        secSalary = salaries.iloc[-1]

    return pd.DataFrame({'SecondHighestSalary':[secSalary]})