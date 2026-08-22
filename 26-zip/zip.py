"""zip() Combines multiple iterables (lists, tuples, sets, dict)
    into a single iterator of tuples. Makes managing multiple indices easier.
"""

import importlib.util
from pathlib import Path
from random import choice, randint


MALTA_PATH = Path(__file__).resolve().parent.parent / "27-faker" / "malta.py"

spec = importlib.util.spec_from_file_location("malta", MALTA_PATH)
malta = importlib.util.module_from_spec(spec)
spec.loader.exec_module(malta)

def create_maltese_person(count):
    names = list(zip(malta.FIRST_NAMES_MALE, malta.SURNAMES))[:count]
    return [
        (first, last, choice(malta.MOBILE_PREFIXES), choice(malta.LANDLINE_PREFIXES))
        for first, last in names
    ]



def main():
    names = create_maltese_person(10)

    for first, last, mobile, landline in names:
        mobile_number = f'+356 {mobile}{randint(100000, 999999)}'
        landline_number = f'+356 {landline}{randint(100000, 999999)}'
        print(f"{first} {last} - Mobile: {mobile_number}, Landline: {landline_number}")


if __name__ == "__main__":
    main()
