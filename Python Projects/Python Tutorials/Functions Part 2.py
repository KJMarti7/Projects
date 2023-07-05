def kilometertoMiles(kilometer):
    return kilometer * 0.6214
#end method

def main():
    print("This driver program test the kilometerstoMiles() function \n")

    kilometers = float(input("Enter a distance a in kilometers: "))

    print()
    print(kilometers, "Kilometers =", kilometertoMiles(kilometers), "miles")

#end method


#Call main method
main()
