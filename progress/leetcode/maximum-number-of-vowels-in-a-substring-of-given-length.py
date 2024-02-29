class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=['a', 'e', 'i', 'o','u']
        count=0
        ans=0
        left=0
        right=k-1
        
        for i in range(0,k):
            if s[i] in vowel:
                count+=1
        ans = max(ans,count)
        for i in range(k,len(s)):
            if s[i-k] in vowel and s[i] in vowel:
                pass
            elif s[i-k] in vowel and s[i] not in vowel:
                count-=1
            elif s[i-k] not in vowel and s[i] in vowel:
                count+=1
            elif s[i-k] not in vowel and s[i] not in vowel:
                pass
            ans=max(count,ans)
            
        return ans


        