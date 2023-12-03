
# def find():
#     quantity = input()
#     allNums = input().split(" ")
#     for j in range(len(allNums)):
#         allNums[j] = int(allNums[j])
#     allNums.sort()
#     for i in range(len(allNums) - 1):
#         if allNums[i + 1] - allNums[i] != 1:
#             return allNums[i] + 1
#     return quantity
# print(find())
#
# def find():
#     allDna = input()
#     counter = 0
#     tempCounter = 1
#     for i in range(len(allDna) - 1):
#         if allDna[i] == allDna[i + 1]:
#             tempCounter += 1
#         else:
#             counter = max(counter, tempCounter)
#             tempCounter = 1
#     counter = max(counter, tempCounter)
#     return counter
# print(find())
#
# def find():
#     number = 0
#     quantity = int(input())
#     for i in range(quantity):
#         operation = input()
#         if "-" in operation:
#             number -= 1
#         else:
#             number += 1
#     return number
#
# print(find())
#
# def find():
#     numbers = input().split(" ")
#     target = int(numbers[1]) - 1
#     if target % 2 == 0:
#         return 1
#     else:
#         l = 1
#         for i in range(int(numbers[0]) - 1):
#             l = l * 2 + 1
#         left = 0
#         right = l - 1
#         init = int(numbers[0])
#         while left <= right:
#             if target == (left + right) // 2:
#                 return init
#             elif target > (left + right) // 2:
#                 init -= 1
#                 left = (left + right) // 2 + 1
#             else:
#                 init -= 1
#                 right = (left + right) // 2 - 1
#     return target
#
# print(find())
#
# def find(num):
#     first = 0
#     last = num
#     stop = True
#     while stop:
#         start = 2
#         for i in range(start, num):
#             if isPrime(i) == True:
#                 start = i
#                 second = num - start
#                 if isPrime(second):
#                     return str(num) + " = " + str(start) + " + " + str(second)
#
#
# def isPrime(num):
#     for j in range(2, num):
#         if num % j == 0:
#             return False
#     return True
#
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     print(find(num))



def find():
    quantity = int(input())
    stringNums = input().split(" ")
    nums = [int(i) for i in stringNums]
    if quantity == 1:
        return nums[0]
    dp = []
    dp.append(nums[0])
    dp.append(max(nums[0], nums[1]))
    for i in range(2, len(nums)):
        dp.append(max(nums[i] + dp[i - 2], dp[i - 1]))
    return dp[quantity - 1]
print(find())
