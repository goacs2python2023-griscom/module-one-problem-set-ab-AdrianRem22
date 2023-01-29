def compare_dates(month1, day1, year1, month2, day2, year2):
    date1 = (year1, month1, day1)
    date2 = (year2, month2, day2)
    if date1 < date2:
        return "before"
    elif date1 > date2:
        return "after"
    else:
        return "same"
def main():
    month1 = input("First date month?:")
    day1 = input("First date day?:")
    year1 = input("First date year?:")
    month2 = input("Second date month?:")
    day2 = input("Second date day?:")
    year2 = input("Second date year?:")
    print(f' The first date is before {compare_dates(month1, day1, year1, month2, day2, year2)} the second date')
main()