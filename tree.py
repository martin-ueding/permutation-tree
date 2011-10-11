lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def iterate(listnumber, level=0):
    for element in lists[listnumber]:
        print "  "*level,
        if listnumber < len(lists)-1:
            print element
            iterate(listnumber+1, level+1)
        else:
            print element

iterate(0)
