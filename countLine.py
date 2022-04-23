def countLine(filename):
    lines = open(filename)
    count = 0
    for line in lines:
        count += 1
    return count

def Main():
    print(f'Number of Line: {countLine("convertBinToDec.py")}')

if __name__ == '__main__':
    Main()