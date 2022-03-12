def binToDec(number):
    dec = 0
    leng = len(str(number))
    n = str(number)[::-1]
    for i in range(leng):
        dec += (int(n[i]) * (2**i))
        
    return dec

def decToBin(number):
    binary = []
    quot = 1
    while (quot != 0):
        if number // 2 != 0:
            quot = number // 2
            binary.append(number % 2)
            number = quot
        else:
            binary.append(number % 2)
            quot = 0
    binary.reverse()
    b = ' '.join(map(str, binary))
    return b

def Main():
    print("Begin:")
    print(binToDec(10000010))
    print(decToBin(130))
    print("End:")

if __name__ == '__main__':
    Main()