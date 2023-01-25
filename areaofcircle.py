def square(x):
    y = x**2
    return y
def main():
    x = int(input("Enter the radius of a circle:"))
    area = (square(x))*(3.14159265359)
    print(f'The area of the circle is {area}')
    
main()