def main():
    percentage = fuel_gauge()
    the_output = outputting(percentage)
    print(the_output)


def fuel_gauge():

    while True:
        try:
            frac = input("Fraction: ").split("/")
            x,y = [int(i) for i in frac]
            return round((x/y) * 100)
        except (ValueError, ZeroDivisionError):
            pass

def outputting(perc):
    if perc == 100:
        return("F")
    elif perc == 0:
        return("E")
    else:
        return(f"{perc}%")



main()


def fuel():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            return (int(x) / int(y))*100
        except (ZeroDivisionError or ValueError):
            pass


def the_perc(x):
    x = round (x,-1)
    print
    if x == 0:
        return "E"
    elif x == 100:
        return "F"
    else:
        return f"{x}%"


main()

