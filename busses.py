def bus_calc(students):
    busses = students // 52
    remainder = students % 52
    if remainder > 0:
        busses = busses + 1
    return busses
def main():
    students = int(input("How many students are there: "))
    busses = bus_calc(students)
    if busses == 1:
        print(f'You will need 1 bus')
    elif busses > 1:
        print(f'You will need {busses} busses')
main()