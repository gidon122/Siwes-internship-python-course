metrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(metrix[2][1])

numbers = [1, 2, 2, 2, 2, 3, 4, 5, 6, 7]
numbers.append(18)
numbers.remove(2)
numbers.pop()
numbers.clear()
numbers.extend([9,19, 20])
numbers.insert(2, 21)
numbers.sort(reverse=True)

print (numbers)

duplicate = [1, 3, 3, 4, 5, 5, 6, 7, 12, 13, 16, 16, 16, 20]
uniques = []
for number in duplicate:
    if number not in uniques:
        uniques.append(number)
print(uniques)