import winsound
def music(n):
    """n is a number to be converted into music"""
    n = str(n)
    ls = n.split('.')[0]
    ls = int(ls)
    rml = convert(ls)[::-1]
    tones, notes = get_tones(rml)
    
    if '.' in n:
        rs = n.split('.')[1]
        rs = int(rs)
        rmr = convert(rs)[::-1]
        tr, nr = get_tones(rmr)
        tones += tr
        notes += "." + " " + nr
        
    play(tones, notes)
    
def convert(n):
    r = []
    if n != 0:
        r += [n%26] + convert(n//26)
    return r

def get_tones(rm):
    t = []
    n = ''
    key = {0:["--", 37],
           1:['C5',523], 2:['C5#',554], 3:['D5',587], 4:['E5b',622], 5:['E5',659], 6:['F5',698], 7:['F5#',740], 8:['G5',784], 9:['G5#',831], 10:['A5',880], 11:['B5b',932], 12:['B5',988],
           13:['C6',1047], 14:['C6#',1109], 15:['D6',1175], 16:['E6b',1245], 17:['E6',1319], 18:['F6', 1397], 19:['F6#',1480], 20:['G6',1568], 21:['G6#',1661], 22:['A6',1760], 23:['B6b',1865], 24:['B6',1976],
           25:['C7',2093]}
    for d in rm:
        t += [key[d][1]]
        n += key[d][0] + ' '
    return t, n

def play(t, n):
    for i in range(0, len(t)):
        print(n.split(' ')[i] + ' ', end='')
        winsound.Beep(t[i], 250)

def number(music):
    """music is a sequence of notes to be converted into a number"""
    key = {'--':0,
           'C5':1, 'C5#':2, 'D5':3, 'E5b':4, 'E5':5, 'F5':6, 'F5#':7, 'G5':8, 'G5#':9, 'A5':10, 'B5b':11, 'B5':12,
           'C6':13, 'C6#':14, 'D6':15, 'E6b':16, 'E6':17, 'F6':18, 'F6#':19, 'G6':20, 'G6#':21, 'A6':22, 'B6b':23, 'B6':24,
           'C7':25}
    ml = music.split(' ')
    nl = []
    for n in ml:
        nl += [key[n]]
    num = base10(nl)
    return num
    
def base10(nl):
    num10 = 0
    for i in range(0, len(nl)):
        num10 += nl[::-1][i]*26**i
    return num10

"""testing"""
def test(music):
    """music is a string of notes to be played"""
    key = {'--':37,
           'C5':523, 'C5#':554, 'D5':587, 'E5b':622, 'E5':659, 'F5':698, 'F5#':740, 'G5':784, 'G5#':830, 'A5':880, 'B5b':932, 'B5':988,
           'C6':1047, 'C6#':1109, 'D6':1175, 'E6b':1245, 'E6':1319, 'F6':1397, 'F6#':1480, 'G6':1568, 'G6#':1661, 'A6':1760, 'B6b':1865, 'B6':1976,
           'C7':2093}
    ml = music.split(' ')
    for note in ml:
        winsound.Beep(key[note], 250)




"""
---SONGS---
Happy Birthday:
1332167136276872030246714304570633953903

Flight of the Bumblebee:
89698561999721618851268279899824821675877760836271314443201104451030

Rugrats:
10228090238140146623325720600773838
"""



