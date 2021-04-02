from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vehicle:
    wheels: int
    make: str


@dataclass
class Person:
    id: int
    name: str
    age: int
    mobile_os: str
    vehicle: Vehicle


@dataclass
class Subscriber(Person):
    start_date: datetime


feed = [
    Person(
        id=1,
        name="Lucille",
        age=40,
        mobile_os="iOS",
        vehicle=Vehicle(wheels=4, make="mazda"),
    ),
    Person(
        id=2,
        name="Maebe",
        age=14,
        mobile_os="iOS",
        vehicle=Vehicle(wheels=4, make="fisher price"),
    ),
    Person(
        id=3,
        name="George",
        age=3,
        mobile_os="iOS",
        vehicle=Vehicle(wheels=2, make="segway"),
    ),
    Subscriber(
        id=4,
        start_date=datetime.utcnow(),
        name="Oscar",
        age=35,
        mobile_os="Android",
        vehicle=Vehicle(wheels=3, make="fisher price"),
    ),
]

feed_data = [
    {
        "$type": "person",
        "data": {
            "id": 1,
            "name": "Lucille",
            "age": 40,
            "mobile_os": "iOS",
            "vehicle": {"wheels": 4, "make": "mazda"},
        },
    },
    {
        "$type": "person",
        "data": {
            "id": 2,
            "name": "Maebe",
            "age": 14,
            "mobile_os": "iOS",
            "vehicle": {"wheels": 4, "make": "fisher price"},
        },
    },
    {
        "$type": "person",
        "data": {
            "id": 3,
            "name": "George",
            "age": 3,
            "mobile_os": "iOS",
            "vehicle": {"wheels": 2, "make": "segway"},
        },
    },
    {
        "$type": "subscriber",
        "data": {
            "id": 4,
            "start_date": datetime.utcnow().isoformat(),
            "name": "Oscar",
            "age": 35,
            "mobile_os": "Android",
            "vehicle": {"wheels": 3, "make": "fisher price"},
        },
    },
]
