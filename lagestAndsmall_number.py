def largestNumber(num):
    large = num[0]
    for n in num:
        if n > large:
            large = n
    return large

def smallestNumber(num):
    small = num[0]
    for n in num:
        if small > n:
            small = n
    return small

def Main():
    print(f'Large: {largestNumber([3, 41, 12, 9, 74, 15])}')
    print(f'Small: {smallestNumber([3, 41, 12, 9, 74, 15])}')
    print(sys.argv[1])

if __name__ == '__main__':
    Main()
