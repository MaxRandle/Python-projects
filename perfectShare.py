#perfect sharing algorithm

#2 parties
#abbabaab

def shareError2():
    errorsum = 0
    for i in range(1,101):
        if i%2 == 0:
            errorsum -= 1/i
        else:
            errorsum += (1/i)
        print(errorsum)

#3 parties
#ABCCBA BCAACB CABBAC
def shareError3():
    pass
