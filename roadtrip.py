def road_trip_cost(miles,mpg,costpg):
    total_cost = ((miles / mpg) * costpg)
    return total_cost
def main():
    miles = int(input("How long is the trip (miles):"))
    mpg = int(input("What is the miles per gallon of the car:"))
    costpg = int(input("What is the cost of gas per gallon:"))
    print(f'Your trip will cost {road_trip_cost(miles,mpg,costpg)}$ ')
main()