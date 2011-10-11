lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def iterate(listnumber):
    result = []
    for element in lists[listnumber]:
        if listnumber < len(lists)-1:
            result.append([element, iterate(listnumber+1)])
        else:
            result.append([element])
    return result

print iterate(0)
