import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # df = pd.DataFrame({
    #     "student_id": [id for id, _ in student_data], 
    #     "age": [age for _, age in student_data]
    # })
    
    # return df
    return pd.DataFrame(student_data, columns=['student_id', 'age'])
