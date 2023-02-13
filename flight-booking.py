class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * n
        for first, last, seats_reserved in bookings:
            seats[first - 1] += seats_reserved
            if last < n:
                seats[last] -= seats_reserved
        for i in range(1, n):
            seats[i] += seats[i - 1]
        return seats
