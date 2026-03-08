import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    valid_mails = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\.-]*@leetcode(\?com)?\.com$')]

    return valid_mails