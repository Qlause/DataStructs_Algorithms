a = [[0 for x in range(6)] for y in range(6)]
parentWord = "hello"
childWord = "hetto"

for index, value in enumerate(parentWord):
    for indexChild, valueChild in enumerate(childWord):
        if index == indexChild and value == valueChild:
            a[index][indexChild] = a[index][indexChild] + 1
        if a[index + 1][indexChild] < a[index][indexChild]:
            a[index + 1][indexChild] = a[index][indexChild]
        if a[index][indexChild + 1] < a[index][indexChild]:
            a[index][indexChild + 1] = a[index][indexChild]

print(a[len(parentWord) - 1][len(childWord) - 1])