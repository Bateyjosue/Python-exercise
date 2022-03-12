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
    ans = 'yes'
    while (ans.lower() == 'yes'):
        print("Begin:\n")
        op = input("Which Operation do you wanna perform? \n1. Bin to Dec\n2. Dec to Bin\n>> ")
        if(op == '1'):
            number = int(input("Enter a Binary number: "))
            print(binToDec(number))
        elif (op == '2'):
            number = int(input("Enter a Decimal number: "))
            print(decToBin(number))
        else:
            print("Invalid Choice!!!")
        print("\nEnd:")
        ans = input("Do wanna retry? (yes/no)")

if __name__ == '__main__':
    Main()