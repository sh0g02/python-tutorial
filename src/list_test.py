import copy

list = [1, 2, 3]

list.append(4)

# [1, 2, 3, 4]
print(list)

list.extend([5])

# [1, 2, 3, 4, 5]
# 末尾に反復可能体の全アイテムを追加することでリストを伸長する
print(list)

list.insert(2, 6)

# [1, 2, 6, 3, 4, 5]
print(list)

list.remove(6)

# [1, 2, 3, 4, 5]
print(list)

# シャローコピーを返す
# つまり、list2とlist3は同じオブジェクト
list2 = list[:]
list3 = list.copy()
list4 = copy.deepcopy(list3)

print(list2)
print(list3)
print(list4)
print(id(list2))
print(id(list3))
print(id(list4))
