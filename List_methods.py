# 1.Append method
list=[2,1,3]
print(list)
list.append(5)
print(list)

#sorting method in ascending = list.short
print(list.append(4))
print(list.sort()) #it will change the value inside string and will return "none"
print(list)

# sorting method in descending
list2=["banana","litchi","apple","papaya","guava","Guava"] #in strings it works in alphabetic oreder
print(list2.sort(reverse=True))
print(list2)
list3=['a','b','c','d','e']
list3.reverse()
print(list3)
list3.append('g')
print(list3)
print(list3.sort())
print(list3)

#insert method = used to insert element
lac=[3,2,5]
lac.insert(1,6) #it will put 6 in the index 1
lac.insert(0,8)
print(lac)

#remove method = it will remove an element
lac.remove(8)
print(lac)

#pop method= used to remove an element
lac.pop(2)
print(lac)