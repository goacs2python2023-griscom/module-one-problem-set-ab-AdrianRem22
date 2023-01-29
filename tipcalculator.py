def tip_calc(bill,tip_per):
    tip_conv = tip_per * .01
    tip = tip_conv * bill
    total = tip + bill
    return total
def main():
    bill = int(input("How much is the bill: "))
    tip_per = int(input("What percentage would you like to tip: "))
    print(f' The total bill would be {tip_calc(bill,tip_per)} $')
main()


