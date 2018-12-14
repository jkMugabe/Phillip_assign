marks = [23, 4, 5, 6, 64, 90, 67, 98, 45, 23, 67, 78, 89]
list1 = []
list2 = []
for mark in marks:
    if mark <= 10:
        list2.append(mark)
        print(mark, 'for repeat')
    elif mark > 19 and mark <= 39:
        list2.append(mark)
        print(mark, ' is avery poor')
    elif mark > 39 and mark <= 49:
        list2.append(mark)
        print(mark, 'is a poor')
    elif mark > 50 and mark <= 59:
        list1.append(mark)
        print(mark, 'is a poor')
    elif mark > 59 and mark <= 69:
        list1.append(mark)
        print(mark, 'is a good')
    elif mark > 69 and mark <= 89:
        list1.append(mark)
        print(mark, 'is avery good')

    else:
        list1.append(mark)
        print(mark, 'is Excellent')

print(sorted(list1))
print(list2)
