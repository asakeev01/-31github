quantity = input()
students = input().split(" ")
students = [int(digit) for digit in students]
students.sort()
taxis = 0
first = 0
taxi = 0
last = len(students) - 1
while last >= first:
    if students[last] == 4:
        taxis += 1
        last -= 1
    elif students[last] == 3 and students[first] == 1:
        taxis += 1
        last -= 1
        first += 1
    elif students[last] == 3:
        taxis += 1
        last -= 1
    else:
        taxi += int(students[last])
        if taxi == 4:
            taxis += 1
            taxi = 0
        last -= 1
if taxi != 0:
    taxis += 1
print(taxis)