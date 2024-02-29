class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=0
        ans=0
        for i in range(k):
            if blocks[i] == 'B':
                count+=1
        ans=max(count,ans)
        for i in range(k,len(blocks)):
            if blocks[i-k] == 'B' and blocks[i] == 'W':
                count-=1
            elif blocks[i-k] == 'W' and blocks[i] == 'B':
                count+=1
            else:
                pass
            ans=max(count,ans)
        return k-ans

        