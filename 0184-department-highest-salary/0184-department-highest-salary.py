import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    max_salary = employee.groupby('departmentId')['salary'].transform('max')
    
    emp = employee[employee['salary'] == max_salary]
    
    result = emp.merge(department, left_on='departmentId', right_on='id')
    
    return result[['name_y','name_x','salary']].rename(
        columns={'name_y':'Department','name_x':'Employee','salary':'Salary'}
    )