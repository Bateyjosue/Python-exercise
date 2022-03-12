def binToDec(number):
    dec = 0
    leng = len(str(number))
    n = str(number)
    for i in range(leng):
        dec += (int(n[i]) * (2**i))
        
    return dec

def Main():
    print("Begin:")
    print(binToDec(11111))
    print("End:")

if __name__ == '__main__':
    Main()