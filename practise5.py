import copy

mytuple = (1, 2, 3)    
mydict = {'a': 1, 'b': 2, 'c': 3}
mydict2 = {} #建立一個空字典
mydict3 = {'e': 5, 'f': 6 , 'f':7} #建立另一個字典
mydict4 = ['python','c'],['java','R'],['c++','c#'] #建立一個字典


print(mytuple) #顯示元組
print(mydict) #顯示字典
print(mytuple[2]) #顯示元組的第三個元素
print(mydict['a']) #顯示字典中鍵'a'對應的值
mydict ['d'] = 4 #新增鍵'd'及其對應的值4
mydict ['b'] = 5 #修改鍵'b'對應的值為5
print(mydict) #顯示修改後的字典


print("-------------------------------------------------------------------------------")
newdict = copy.deepcopy(mydict) #建立字典的深層複製
print(mydict) #顯示原始字典
print(newdict) #顯示深層複製的字典
newdict.pop('a') #移除鍵'c'及其對應的值
newdict.popitem() #移除字典中的最後一個鍵值對
print(newdict) #顯示修改後的深層複製字典

print("-------------------------------------------------------------------------------")
newdict.clear() #清空字典
print(newdict) #顯示清空後的字典
del newdict #刪除字典


mydict2 ['x'] = 10 #新增鍵'x'及其對應的值10
mydict2 ['y'] = 20 #新增鍵'y'及其對應的
mydict2 ['z'] = 30 #新增鍵'z'及其對應的值30



mydict.update(mydict2) #將mydict2的鍵值對加入mydict中
print(mydict) #顯示更新後的字典
mydict = {**mydict, **mydict3} #合併兩個字典
print(mydict) #顯示合併後的字典

print("-------------------------------------------------------------------------------")
newdict = dict(mydict4) #使用可迭代物件建立字典
print(newdict) #顯示新建立的字典

print("-------------------------------------------------------------------------------")
for key,value in mydict.items(): #遍歷字典的鍵值對
    print(f"Key: {key}, Value: {value}") #顯示鍵和值

for key in mydict.keys(): #遍歷字典的鍵
    print(f"Key: {key}") #顯示鍵

for value in mydict.values(): #遍歷字典的值
    print(f"Value: {value}") #顯示值

for key in sorted(mydict.keys()): #遍歷排序後的字典鍵
    print(f"Sorted Key: {key}, Value: {mydict[key]}") #顯示排序後的鍵及其對應的值
