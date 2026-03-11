class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1

        def revbits(s):
            rev = ""
            for bit in s:
                if bit == '1':
                    rev += '0'
                else:
                    rev += '1'
            
            return rev
        
        def num2bin(n):
            s = ""

            while n > 0:
                s = str(n % 2) + s

                n //= 2
            
            return s
        
        def bin2num(s):
            n = 0
            power = 0

            for i in range(len(s)-1,-1,-1):
                if s[i] == '1':
                    n += 2 ** power
                
                power += 1

            return n

        return bin2num(revbits(num2bin(num)))
