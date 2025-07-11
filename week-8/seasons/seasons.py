from datetime import date
import re
import sys
import inflect
p = inflect.engine()


def main():
    try:
        DoB = input("Date of birth: ")
        d = convert_date(DoB)
        delta = date.today() - d
        minutes = delta.days * 24 * 60
        m = p.number_to_words(minutes, andword="").capitalize()
        print(f"{m} minutes")
    except ValueError:
        sys.exit("Invalid date")


def convert_date(dt):
    if matches := re.search(r'^(\d\d\d\d)-(\d\d)-(\d\d)$', dt):
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))
        return date(year, month, day)
    raise ValueError


if __name__ == "__main__":
    main()
