from typing import List
from rentomatic import services as i


class MemoryStorage(i.RoomStorage):

    def __init__(self):
        self._storage: List[i.Room] = [
            i.Room(code='test', size=100, price=200, latitude=0.0, longitude=0.0)
        ]

    def get_rooms(self, filters: i.RoomFilter) -> List[i.Room]:
        result = []
        for room in self._storage:
            if (
                (filters.code is None or room.code == filters.code)
                and
                (filters.price_min is None or room.price >= filters.price_min)
                and
                (filters.price_max is None or room.price > filters.price_max)
            ):
                result.append(room)
        return result
