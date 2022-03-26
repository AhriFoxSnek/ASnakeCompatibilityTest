def cocktail(a):
    for i in range(len(a)//2):
        swap = False
        for j in range(1+i, len(a)-i):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                swap = True
        if not swap:
            break
        swap = False
        for j in range(len(a)-i-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                swap = True
        if not swap:
            break
test1 = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]
cocktail(test1)
print(test1)
 
test2=list('big fjords vex quick waltz nymph')
cocktail(test2)
print(''.join(test2))
