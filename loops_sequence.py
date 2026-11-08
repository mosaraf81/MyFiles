# # # """i = 1
# # # while i <= 5: #infinite loop
# # #      print(i)
# # #      i += 1
    
# # # print("Done")"""


# # # fruits = ["apple", "Banana", "Guava", "Cherry", "Orange"]
# # # # print(id(fruits))
# # # # print(type(fruits))
# # # # print(fruits[3])
# # # # print(fruits)
# # # # print(fruits[-3])
# # # """fruits[1] = "Jackfruit"
# # # print(fruits)
# # # print(id(fruits))
# # # print(len(fruits))
# # # print(fruits[1:4])"""
# # # fruits = ["Apple", "Banana", "Cherry", "Jackfruit"]
# # # print(fruits)
# # # fruits.append("Papaya")
# # # print(fruits)
# # # fruits.insert(0, "Strawberry")
# # # print(fruits)
# # # fruits.remove("Apple")
# # # print(fruits)
# # # s = fruits.pop(-2)
# # # print(s)
# # # print(fruits)
# # # fruits.sort(reverse= True)
# # # print(fruits)

# # fruits = ("apple", "Banana", "Guava", "Cherry", "Orange")
# # print(fruits)
# fruits = {"Apple", "Banana", "Guava", "Cherry", "Orange", "Apple"}
# print(fruits)

# a = {1, 2, 3, 4, 5}
# b = {0, 3, 4, 6}
# print(a)
# print(b)
# res = a.union(b)
# print(res)
# res1 = a.difference(b)
# res2 = b.intersection(a)
# print(res1)
# print(res2)
# fruits = ("Apple", "Cherry", "Guava")
# for fruit in fruits:
#     print(fruit)
#     break
#     print("----")
# print("Done!")
# fruits = ("Apple", "Cherry", "Guava")
# for fruit in fruits:
#     print(fruit)
#     continue
#     print("----")
# print("Done!")

# nums = [2, 6, 8, 11, 12]
# for num in nums:
#     if num % 2 == 1:
#         continue
#     print(num)
# print("done!")

# print(list(range(2, 10, 2)))


# for item in range(5):
#     print(item)

nums = [3, 6, 12, 24, 48, 96]
doublenums = [i * 2 for i in nums if i % 2 == 1]
#print(nums)
# for i in nums:
#     d = i * 2
#     doublenums.append(d)
print(doublenums)
