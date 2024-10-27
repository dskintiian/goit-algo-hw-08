import heapq
from random import sample

def connect_all_cables(cables: list):
    cost = 0
    heapq.heapify(cables)
    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        print(f'Connecting {cable1} and {cable2}')
        cost += cable1 + cable2
        print(f'Current cost: {cost}')
        heapq.heappush(cables, cable1 + cable2)
        print(f'Cables: {cables}')

    print(f'Final cost: {cost}')

if __name__ == "__main__":
    cables = sample(range(1, 50), 10)
    connect_all_cables(cables)
