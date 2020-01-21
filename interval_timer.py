import winsound
import time

def intTime(t, d=600, f=880):
    """t is the number of seconds between each tone and f is the frequency of the beep"""
    while True:
        winsound.Beep(d, f)
        for i in range(t, 0, -1):
            time.sleep(1)
            print(i)
            
