
def sortList(list, sort):
    sorted = []
    if sort == None:
        sorted = (list)
    elif sort == 'asc':
        sorted =  list.sort(reverse=True)
    elif sort == 'desc':
        sorted =  list.sort()
    return sorted
def Main():
    print(sortList([2, 4, 8, 3, 1, 0, 4, 8, 3], 'asc'))
    print(sortList([2, 4, 8, 3, 1, 0, 4, 8, 3], 'desc'))
    print(sortList([2, 4, 8, 3, 1, 0, 4, 8, 3], None))

if __name__ == '__main__':
    Main()