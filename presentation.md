---
title: Pattern Matching
author: Aru Sahni
...

# A Problem?

Got some data coming in from a pipeline


```python
Person(
    id=1,
    name="Lucille",
    age=40,
)
```

---

Taking action on data


```python
def handler(item):
    if isinstance(item, Person) and age < 13:
        print("Go to bed!")
    else:
        print("Welcome!")
```

---

# Things are never this simple

```python
Person(
    id=1,
    name="Lucille",
    age=40,
    mobile_os="iOS",
    vehicle=Vehicle(wheels=4, make="mazda"),
)
```

---

```python
if isinstance(payload, Person) and payload.age < 13:
    ...
elif (
    isinstance(payload, Person)
    and payload.mobile_os == "iOS"
    and payload.vehicle.make == "fisher price"
):
    ...
elif isinstance(payload, Subscriber) and payload.vehicle.wheels < 4:
    ...
```

---

What about JSON?

```python
{
    "$type": "person",
    "data": {
        "id": 1,
        "name": "Lucille",
        "age": 40,
        "mobile_os": "iOS",
        "vehicle": {"wheels": 4, "make": "mazda"},
    },
}
```

---

Woof.

```python
if (
    isinstance(payload, dict)
    and payload.get("$type") == "person"
    and isinstance(payload.get("data", {}).get("age"), int)
    and payload["data"]["age"] < 13
):
    ...
elif (
    isinstance(payload, dict)
    and payload.get("$type") == "person"
    and payload.get("data", {}).get("mobile_os") == "iOS"
    and payload.get("data", {}).get("vehicle", {}).get("make") == "fisher price"
):
    ...
elif (
    isinstance(payload, dict)
    and payload.get("$type") == "subscriber"
    and isinstance(payload.get("data", {}).get("vehicle", {}).get("wheels"), int)
    and payload["data"]["vehicle"]["wheels"] < 4
):
    ...
```

---

# Write Once, Pain Forever

How do we avoid this? This isn't a problem unique to Python.

Elixir:

Rust:

---

```python
if (
    isinstance(payload, dict)
    and payload.get("$type") == "person"
    and isinstance(payload.get("data", {}).get("age"), int)
    and payload["data"]["age"] < 13
):
    ...
```

```python
match payload:
    case Person(age=int(age)) if age < 13:
        ...
```

---

# PEG Parser

* Python used to use an LL(1) parser
    * tl;dr: when trying to read source code, Python only used to look at the next word
        * Deterministic Context Free Grammar (DCFG)
    * If the token `match` is encountered, Python 3.8 would assume it was a variable
    * To turn it into a keyword, the variable name must be removed from the language
    * This happend with async, and broke code that used `async` as a name.

* Introduced in Python 3.9
    * tl;dr: when trying to read source code, Python can now try different options, moving
      onto the next one when the parser encounters an error.
    * If the token `match` is encountered, Python 3.10 can first see if it's the start of a `match`
      statement, and will treat it like a keyword. Otherwise, it'll treat it like a name.
    * This way, introducing new keywords will be backwards compatible.

---

## Message handler

Python 3.9
```bash
docker run -it -v ${PWD}:/root/ --rm python:3.10-rc-buster-meetup python3 /root/python39.py
```

Python 3.10
```bash
docker run -it -v ${PWD}:/root/ --rm python:3.10-rc-buster-meetup python3 /root/python310.py
```

---

## Shortcomings

**Not exhaustive.** Other languages will panic if all cases of an enum, for
example, aren't handled. This is an important aspect of functional languages.

**Don't return anything.** Pre-walrus operator, Python statements couldn't be
assigned to a variable (with exceptions for ternaries).
A common pattern in other languages such as Rust and Elixir involves assigning
the return value of a branch to a variable. Sadly, this cannot be done in Python.

```python
point := match user_input:
    case (x, y):
        Point(x, y, 0)
    case (x, y, z):
        Point(x, y, z)
    case _:
        Point(0, 0)
```

---

## Reception

Tumultuous at best.

* New syntax
* Better received than `:=`
