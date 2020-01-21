def base_convert(number, current, new):
    'number is a string containing a number, current is the base of the input number, new is the desired base'    
    key1 = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H',
           18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V'}
    b10 = base10(number, current)
    a = convert(b10, new)[::-1]
    bx = ''
    for d in a:
        bx += key1[d]
    return bx

def base10(num, base):
    key2 = {'S':28, '4':4, '0':0, 'B':11, 'A':10, 'T':29, '1':1, 'M':22, '7':7, '9':9, 'D':13, 'U':30, 'G':16, 'J':19, 'P':25, 'R':27, '6':6,
            'V':31, 'E':14, 'L':21, '5':5, 'K':20, '8':8, 'N':23, 'O':24, '3':3, 'Q':26, 'I':18, 'F':15, 'H':17, 'C':12, '2':2}
    num_10 = 0
    for i in range(0, len(num)):
        num_10 += key2[num[::-1][i]]*base**i
    return num_10
    
def convert(n, b):
    """n is a base 10 number, b is the desired base.
    returns a list containing the un-symbolised number"""
    r = []
    if n != 0:
        r += [n%b] + convert(n//b, b)
    return r
