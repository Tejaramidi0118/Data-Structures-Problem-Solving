class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = [""]
        temp = []

        def dfs(node):
            for ch in sorted(node.children.keys()):
                child = node.children[ch]
                if child.is_end_of_word:
                    temp.append(ch)
                    if len(temp) > len(ans[0]):
                        ans[0] = "".join(temp)
                    dfs(child)
                    temp.pop()

        dfs(trie.root)
        return ans[0]
