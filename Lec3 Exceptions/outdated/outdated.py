mounths = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

while True:
    try:
        date = input("Dates:").strip().title()

        if "/" in date:
            mounth, day, year = map(int, date.split("/"))
            if day <= 31 and mounth <= 12:
                print(f"{year:04d}-{mounth:02d}-{day:02d}")
                break

        elif "," in date:
            mounth_name, day, year = date.replace(",", "").split()
            if mounth_name in mounths:
                mounth = mounths.index(mounth_name) + 1
                day, year = int(day), int(year)
                if day <= 31:
                    print(f"{year:04d}-{mounth:02d}-{day:02d}")
                    break

    except (ValueError, IndexError):
