#Omnibase can convert any number in base 2-16 to its equivelant in base 2-16
class ob:
    def __init__(self, number, base):
        """number is a string containing any number from base 2 - 32,
        base is the current base the number is displayed in"""
        
        self.symbols = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F',
                       16:'G', 17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V'}

        self.digits = {'S':28, '4':4, '0':0, 'B':11, 'A':10, 'T':29, '1':1, 'M':22, '7':7, '9':9, 'D':13, 'U':30, 'G':16, 'J':19, 'P':25, 'R':27,
                        '6':6, 'V':31, 'E':14, 'L':21, '5':5, 'K':20, '8':8, 'N':23, 'O':24, '3':3, 'Q':26, 'I':18, 'F':15, 'H':17, 'C':12, '2':2}

        self.number = str(number)
        self.base = int(base)
        self.base_10 = int(self.to_base_ten(self.number, self.base))
        
    def to_base_ten(self, num, base):
        num_10 = 0
        for i in range(0, len(num)):
            num_10 += self.digits[num[::-1][i]]*base**i
        return num_10

    def c(self, base):
        return self.symbolise(self.convert(self.base_10, base))

    def convert(self, n, b):
        r = []
        if n != 0:
            r += [n%b] + self.convert(n//b, b)
        return r

    def symbolise(self, num_list):
        num_string = ""
        for n in num_list[::-1]:
            num_string += self.symbols[n]
        return num_string
        
    def __add__(self, other):
        return OmniBase(self.base_10 + other.base_10, 10).convert(self.base)

    def __sub__(self, other):
        return OmniBase(self.base_10 - other.base_10, 10).convert(self.base)

    def __mul__(self, other):
        return OmniBase(self.base_10 * other.base_10, 10).convert(self.base)
    
    def __repr__(self):
        return self.number
    
""" commented out until function can handle non integer values.
    def __div__(self, other):
        return OmniBase(self.base_10 / other.base_10, 10).convert(self.base)
"""


"""
class Binary(signed_twos_complement_number):
    pass
"""
