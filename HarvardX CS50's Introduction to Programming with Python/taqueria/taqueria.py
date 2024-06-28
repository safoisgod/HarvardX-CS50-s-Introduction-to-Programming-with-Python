def main():
    d = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    x = order(d)


def order(d):
    Total = 0
    try:
        while True:
            item = input("Item: ").title()
            if item in d:
                Total += d[item]
                print (f"Total: ${Total}0")

    except EOFError:
        return None

main()
