# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser = defaultdict(int)
        players = set()
        for win,los in matches:
            loser[los] +=1
            players.add(los)
            players.add(win)
        ans = [[],[]]
        for player in players:
            if player not in loser:
                ans[0].append(player)
            if loser[player] == 1:
                ans[1].append(player)
        ans[0].sort()
        ans[1].sort()
        return ans
        
        