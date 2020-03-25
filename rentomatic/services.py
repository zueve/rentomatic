from typing import Optional, List
from pydantic import BaseModel


class Room(BaseModel):
    code: str
    size: int
    price: int
    latitude: float
    longitude: float


class RoomFilter(BaseModel):
    code: Optional[str] = None
    price_min: Optional[int] = None
    price_max: Optional[int] = None


class RoomStorage:
    def get_rooms(self, filters: RoomFilter) -> List[Room]: ...


class RoomListUseCase:
    def __init__(self, repo: RoomStorage):
        self.repo = repo

    def show_rooms(self, filters: RoomFilter) -> List[Room]:
        rooms = self.repo.get_rooms(filters=filters)
        return rooms
