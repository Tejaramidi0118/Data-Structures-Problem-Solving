import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    k = employee['salary'].drop_duplicates().sort_values(ascending=False)
    val = k.iloc[1] if len(k)>=2 else None

    return pd.DataFrame({'SecondHighestSalary':[val]})