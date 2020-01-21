def dec_bin(dec):
    bin_num = ""
    dec_num = dec
    while dec_num > 0:
        bin_num += str(dec_num%2)
        dec_num = dec_num//2
    return bin_num[::-1]
