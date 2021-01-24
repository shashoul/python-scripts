if __name__ == "__main__":
    arr = [0,0,0,3,4,50,0,5410,2,2,3,0,0,0,0,33,22,33,1,4,5,6,0]
    length = len(arr)
    i=0
    pos=0
    while i < length:
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
        i += 1
    while pos < length:
        arr[pos] = 0
        pos += 1
    
    print(arr)

    terms = {}
    print(terms.get('4'),'4' in terms,terms.values())
    terms['4'] = "four"
    terms['5'] = "five"
    terms['6'] = "six"
    terms['7'] = "seven"
    print(terms.get('4'),'4' in terms,terms.values())
    for val in terms.values():
        print(val)    