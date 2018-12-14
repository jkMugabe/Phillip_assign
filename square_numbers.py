def printList():
    square_numbers = []
    for x in range(1, 5):
        square = x**2

        square_numbers.append(square)

    print(square_numbers[0:5])


printList()
