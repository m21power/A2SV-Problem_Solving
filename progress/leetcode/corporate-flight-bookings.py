class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        output=[0]*n
        for book in bookings:
            output[book[0]-1]+=book[2]
            if book[1]<n:
                output[book[1]]-=book[2]
        for i in range(1,n):
            output[i]=output[i-1]+output[i]
        return output



        """output=[0]*n
        for book in bookings:
            start,last,seat=book
            for i in range(start-1,last):
                output[i]+=seat
        return output
        """