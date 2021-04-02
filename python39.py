#!/usr/bin/env python3

from common import Person, Subscriber, feed, feed_data


def handle_activity(payload):
    if isinstance(payload, Person) and payload.age < 13:
        print(f"User {payload.id} is {payload.age}")
    elif (
        isinstance(payload, Person)
        and payload.mobile_os == "iOS"
        and payload.vehicle.make == "fisher price"
    ):
        print("Read skeumorphic weekly")
    elif isinstance(payload, Subscriber) and payload.vehicle.wheels < 4:
        print(
            f"Hey {payload.name}, subscribe to our sister magazine, wheels up for information on {payload.vehicle.wheels}-wheeled vehicles."
        )
    else:
        print("Do nothing")


def handle_activity_json(payload):
    if (
        isinstance(payload, dict)
        and payload.get("$type") == "person"
        and isinstance(payload.get("data", {}).get("age"), int)
        and payload["data"]["age"] < 13
    ):
        print(f"User {payload['data']['id']} is {payload['data']['age']}")
    elif (
        isinstance(payload, dict)
        and payload.get("$type") == "person"
        and payload.get("data", {}).get("mobile_os") == "iOS"
        and payload.get("data", {}).get("vehicle", {}).get("make") == "fisher price"
    ):
        print("Read skeumorphic weekly")
    elif (
        isinstance(payload, dict)
        and payload.get("$type") == "subscriber"
        and isinstance(payload.get("data", {}).get("vehicle", {}).get("wheels"), int)
        and payload["data"]["vehicle"]["wheels"] < 4
    ):
        print(
            f"Hey {payload['data']['name']}, subscribe to our sister magazine, wheels up for information on {payload['data']['vehicle']['wheels']}-wheeled vehicles."
        )
    else:
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
