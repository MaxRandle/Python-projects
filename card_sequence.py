"""The following program will generate the sequence of stack placement
required to perform the 27 card favourite number trick."""
def card_sequence(number):
    x0 = number - 1
    p2 = x0 // 9
    x1 = x0 % 9
    p1 = x1 // 3
    x2 = x1 % 3
    p0 = x2
    sequence = [p0, p1, p2]
    for p in sequence:
        if p == 0:
            print("top")
        if p == 1:
            print("mid")
        if p == 2:
            print("bot")
            
    return card_sequence(int(input("Enter Favourite Number: ")))

card_sequence(int(input("Enter Favourite Number: ")))
