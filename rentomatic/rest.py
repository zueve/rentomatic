from typing import List
from fastapi import FastAPI, Depends
from rentomatic import services, adapters

app = FastAPI()


def get_use_case() -> services.RoomListUseCase:
    return services.RoomListUseCase(adapters.MemoryStorage())


@app.post("/rooms", response_model=List[services.Room])
def rooms(filters: services.RoomFilter, use_case=Depends(get_use_case)):
    return use_case.show_rooms(filters)
