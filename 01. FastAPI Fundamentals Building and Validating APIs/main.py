from fastapi import FastAPI
from datetime import date
from typing import List
from pydantic import BaseModel

class Album(BaseModel):
    title: str
    release_date: date

class BandWithAlbums(BaseModel):
    id: int
    name: str
    genre: str
    albums: List[Album] = []

class Band(BaseModel):
    id: int
    name: str
    genre: str

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello, FastAPI!"}

BANDS = [
    {"id": 1, "name": "The Kinks", "genre": "Rock"},
    {"id": 2, "name": "Aphex Twin", "genre": "Electronic"},
    {"id": 3, "name": "Black Sabbath", "genre": "Metal"},
    {"id": 4, "name": "Wu-Tang Clan", "genre": "Hip-hop"},
]

# BAND = [
#     {"id": 5, "name": "The XXX", "genre": "XXX"}
# ]

@app.get("/bands")
async def get_bands():
    return BANDS

BANDS_WITH_ALBUMS = [
    {
        "id": 1,
        "name": "The Beatles",
        "genre": "Rock",
        "albums": [
            {"title": "Abbey Road", "release_date": "1969-09-26"},
            {"title": "Sgt. Pepper's Lonely Hearts Club Band", "release_date": "1967-06-01"},
        ],
    },
]

@app.get("/bands_with_albums", response_model=List[BandWithAlbums])
async def get_bands_with_albums():
    return BANDS_WITH_ALBUMS

@app.get("/bands_by_genre")
async def bands_by_genre(genre: str):
    return [band for band in BANDS if band["genre"].lower() == genre.lower()]

@app.post("/bands")
async def add_band(band: Band):
    BANDS.append(band.dict())
    return {"message": "Band added successfully!", "band": band}
