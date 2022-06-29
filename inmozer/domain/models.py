from dataclasses import dataclass


@dataclass
class Property:
    title: str
    price: int
    rooms: int
    surface: int
    floor: int
    summary: str
    telephone: str
    email: str
    agency: str
    num_photos: int
