# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkin = {} # key = id,value = [city,time]
        self.average = defaultdict(list)# key = (city1 , value =[[city2,sum,count]]
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName,t]
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        city1,time1= self.checkin[id]
        if city1 in self.average:
            for lis in self.average[city1]: #[[city2,sum,count]] 
                cityname,sum,cnt = lis
                if cityname == stationName:
                    lis[1] += (t - time1)
                    lis[2] += 1
                    return
        self.average[city1].append([stationName,t - time1,1])


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        for lis in self.average[startStation]:
            cityname,sum,cnt = lis
            if cityname == endStation: 
                return lis[1]/lis[2]
    


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)