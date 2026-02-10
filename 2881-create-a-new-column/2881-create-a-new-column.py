import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
        employees["bonus"] = [sal*2 for sal in employees["salary"]]

        return employees