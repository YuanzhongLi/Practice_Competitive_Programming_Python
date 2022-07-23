from heapq import heapify, heappop, heappush

class SeatManager:
    def __init__(self, n: int):
        self.seats = [i for i in range(1, n+1)]
        heapify(self.seats)

    def reserve(self) -> int:
        return heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seats, seatNumber)
