from collections import Counter

def most_common(numbers):
    counts = Counter(numbers)
    top = counts.most_common()

    return top

def Main():
    print(most_common([1,1,5,2,3,5,2,1,4]))

if __name__ == '__main__':
    Main()