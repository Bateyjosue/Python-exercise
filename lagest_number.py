def largestNumber(num):
    large = 0
    for n in num:
        if n > large:
            large = n
    return large


def Main():
    print(largestNumber([3, 41, 12, 9, 74, 15]))

if __name__ == '__main__':
    Main()
