# Write your code here
from typing import Optional, List

from pydantic import BaseModel
from datetime import date


class MovieBase(BaseModel):
    id: int
    name: str
    date: date
    score: float
    overview: Optional[str]

    class Config:
        orm_mode = True
        from_attributes = True


class MoviesListResponseSchema(BaseModel):
    movies: List[MovieBase]
    prev_page: Optional[str]
    next_page: Optional[str]
    total_pages: int
    total_items: int
