my_list = [2,4,6,8,10,15,20]
print(my_list[0:2])
print(my_list[3:5])
my_list[3] = "word"
print(my_list)
print(my_list.index("word"))
print(my_list.index(15))

my_list = [9,4,82,751,962,3,10]
print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse = True)
print(my_list)

my_list = [2,4,6,8,10,15,20]
my_list.append(60)
print(my_list)
my_list.insert(3,2)
print(my_list)
my_list.remove(4)
print(my_list)
my_list.pop(4)
print(my_list)

