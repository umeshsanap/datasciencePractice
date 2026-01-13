'''
tuple
representation of tuple
built in method in tuple
use of index 
use of count
how to merge two tuples
how to change the element in tuple
'''
# name = {"sakshi","akshada","radhika",True, 1, False, 0,"sakshi", 0.5, 1/2}
# print(name)
# print(len(name))
# rollno = {1,2,3,4,5}
# print(rollno)
# rollno = (0,0,0,1,"akshada","sakshi",True, 2.4, 3+7j,True, True, True, False)
# tupleToSet = set(rollno)
# print(tupleToSet)
# rollno = (1,2,3,4,5)
# name.update(rollno)
# name.add("MAHARASHTRA")
# print(rollno)
# print(name)]
# try:
name = {"sakshi","akshada","radhika",True, 1, False, 0,"sakshi", 0.5, 1/2}
rollno = {0,True, False, 0.5, "akshada",1,2,3,4,5}
no = {1,2,3,4,5,6,7,8}

# set3 = name.union(rollno, num)
newSet = name ^ rollno
print(newSet)
# name.discard(3)
# except:
#     print("Data not present")
