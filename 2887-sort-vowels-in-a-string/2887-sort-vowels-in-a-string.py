class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        vowel_chars = [c for c in s if c in vowels]
        vowel_chars.sort()

        result = []
        v_index = 0

        for c in s:
            if c in vowels:
                result.append(vowel_chars[v_index])
                v_index += 1
            else:
                result.append(c)

        return ''.join(result)
