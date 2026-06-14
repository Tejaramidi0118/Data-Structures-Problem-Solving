class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = float('-inf')

        for account in accounts:
            temp = sum(account)

            if temp > maxi:
                maxi = temp
        
        return maxi