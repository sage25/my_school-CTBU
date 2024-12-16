# lst1 = []
# for i in range(100,1000):
#     a = i // 100
#     temp = i % 100
#     b = temp // 10
#     c = temp % 10
#     if a**3 + b**3 + c**3 == i:
#         lst1.append(str(i))
# print(','.join(lst1))


# ################################################3
# lst2 = []
# for i in range(100,1000):
#     i = str(i)
#     if int(i[0])**3 + int(i[1])**3 + int(i[2])**3 == int(i):
#         lst2.append(i)
# print(','.join(lst2))


lst3 = [str(i) for i in range(100,1000) if int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3 == int(i)]
print(','.join(lst3))