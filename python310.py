#!/usr/bin/env python3

from common import Person, Subscriber, Vehicle, feed, feed_data

def handle_activity(payload):
    match payload:
        case Person(age=age) if age < 13:
            print(f"User {payload.id} is {age}")
        case Person(mobile_os="iOS", vehicle=Vehicle(make=make)) if make == "fisher price":
            print("Read skeumorphic weekly")
        case Subscriber(vehicle=Vehicle(wheels=wheels)) if wheels < 4:
            print(
                f"Hey {payload.name}, subscribe to our sister magazine, wheels up for information on {wheels}-wheeled vehicles."
            )
        case _:
            print("Do nothing")

def handle_activity_json(payload):
    match payload:
        case {"$type": "person", "data": { "age": int(age) }} if age < 13:
            print(f"User {payload['data']['id']} is {age}")
        case {"$type": "person", "data": {"mobile_os": "iOS", "vehicle": {"make": make}}} if make == "fisher price":
            print("Read skeumorphic weekly")
        case {"$type": "subscriber", "data": { "vehicle": { "wheels": int(wheels) }}} if wheels < 4:
            print(
                f"Hey {payload['data']['name']}, subscribe to our sister magazine, wheels up for information on {wheels}-wheeled vehicles."
            )
        case _:
            print("Do nothing")

if __name__ == "__main__":
    print("  Dataclasses\n  ===========")
    for pos, item in enumerate(feed):
        print(pos + 1, end=" ")
        handle_activity(item)

    print("\n\n  JSON\n  ====")
    for pos, item in enumerate(feed_data):
        print(pos + 1, end=" ")
        handle_activity_json(item)
