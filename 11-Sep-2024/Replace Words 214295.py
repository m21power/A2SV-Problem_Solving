# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Trie:
    def __init__(self):
        self.is_end = False
        self.child = [None for _ in range(26)]
class Solution:
    def __init__(self):
        self.root = Trie()
    def inserting(self,word):
        cur = self.root
        for ch in word:
            idx = ord(ch) - 97
            if not cur.child[idx]:
                cur.child[idx] = Trie()
            cur = cur.child[idx]
        cur.is_end = True
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.inserting(word)
        sentence = sentence.split()
        ans = []
        def find(word,pack):
            cur = self.root
            for ch in word:
                idx = ord(ch) - 97
                if cur.child[idx]:
                    if cur.is_end: return pack
                    pack += ch
                    cur = cur.child[idx]
                else:
                    return pack if cur.is_end else word
            return pack
        for word in sentence:
            ans.append(find(word,''))
        return ' '.join(ans)
         
            

        