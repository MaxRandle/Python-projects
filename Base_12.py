class Dozenal:
    def __init__(self, dozenal_number):
        didgits = "0123456789de"
        self.doz = str(dozenal_number)
        for didgit in self.doz:
            if didgit not in didgits:
                self = None
                print("INVALID")
                return
        self.dec = self.doz_to_dec()

            
    def doz_to_dec(self):
        reverse = ""
        for number in range(len(self.doz)-1, -1, -1):
            reverse = reverse + self.doz[number]
        decimal_number = 0
        for position in range(0, len(reverse)):
            if reverse[position] == "d":
                decimal_number += 10 * 12**position
            elif reverse[position] == "e":
                decimal_number += 11 * 12**position
            else:
                decimal_number += int(reverse[position]) * 12**position
        return decimal_number

    def dec_to_doz(self):
        pass

    def __add__(self, other):
        return self.dec + other.dec

    def __repr__(self):
        return self.doz
