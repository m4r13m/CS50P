months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            month, day, year = date.split("/")
            m = int(month)
            d = int(day)
            if m > 12 or d > 31:
                continue
            break
        elif "," in date:
            month, day, year = date.split(" ")
            m = months.index(month) + 1
            d = int(day.replace(",", ""))
            if d > 31:
                continue
            break
        else:
            continue
    except ValueError:
        pass

print(f"{year}-{m:02}-{d:02}")
