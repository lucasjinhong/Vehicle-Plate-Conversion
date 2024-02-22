def reverse_plate (plateSyms) :
    if not plateSyms[0].isdigit() or not plateSyms[1].isdigit() :
        return plateSyms[2:] + plateSyms[:2]
    else :
        return plateSyms[4:] + plateSyms[:4]

if __name__ == '__main__' :
    while True :
        s = input('Enter 6 symbol license plate: ')
        if len(s) != 6 :
            print('Wrong format')
            continue
        print(reverse_plate(s))
