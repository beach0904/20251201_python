mysetA = {1, 2, 3} #建立一個集合
mysetB = set() #建立一個空集合

print(mysetA) #顯示集合mysetA
print(mysetB) #顯示集合mysetB
print("-------------------------------------------------------------------------------")
mysetB = mysetA.copy() #建立集合mysetA的淺層複製
mysetA.clear() #清空集合mysetA

print(mysetA) #顯示清空後的集合mysetA
print(mysetB) #顯示複製後的集合mysetB
print("-------------------------------------------------------------------------------")

mysetB.add(4) #新增元素4到集合mysetB中
mysetB.add(5) #新增元素5到集合mysetB中
mysetB.add(6) #新增元素6到集合mysetB中
mysetB.remove(2) #移除集合mysetB中的元素2
mysetB.discard(1) #移除集合mysetB中的元素1

print(mysetA) #顯示集合mysetA
print(mysetB) #顯示集合mysetB
print("-------------------------------------------------------------------------------")
mysetA = {4,5,6}
print("Set A:", mysetA) #顯示集合mysetA
print("Set B:", mysetB) #顯示集合mysetB
print()
intersectionSet = mysetA.intersection(mysetB) #集合交集
print("Intersection:", intersectionSet) #顯示交集結果
unionSet = mysetA.union(mysetB) #集合聯集
print("Union:", unionSet) #顯示聯集結果
differenceSet = mysetA.difference(mysetB) #集合差集
print("Difference:", differenceSet) #顯示差集結果
symmetricDifferenceSet = mysetA.symmetric_difference(mysetB) #集合對稱差集
print("Symmetric Difference:", symmetricDifferenceSet) #顯示對稱差集結果
print("-------------------------------------------------------------------------------")


