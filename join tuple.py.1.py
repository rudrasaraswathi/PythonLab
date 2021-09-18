List = [(1, 2), (1, 3), (1, 4), (5, 6), (7, 8)]

print("The original list is: ")
print(List)

result = []
for sub in List:
   if result and result[-1][0] == sub[0]:
      result[-1].extend(sub[1:])
   else:
      result.append([ele for ele in sub])
result = list(map(tuple, result))

print("The joined list is: " )
print(result)
