class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        word_set = set(wordList)
        
        if endWord not in word_set: # If endWord is not in the wordList
            return 0
        
        queue = deque([(beginWord, 1)])  # (current_word, current_length)
        
        while queue:
            current_word, level = queue.popleft()
            
            for i in range(len(current_word)):
                # Try changing the letter at position i
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # Create a new word by changing the i-th character
                    new_word = current_word[:i] + c + current_word[i+1:]

                    if new_word == endWord:
                        return level + 1
                    
                    if new_word in word_set:
                        queue.append((new_word, level + 1))
                        word_set.remove(new_word)  
        
        # If no transformation sequence is found, return 0
        return 0
