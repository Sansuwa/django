# LIST
# dir(list) -shows all its functions
# help(list.append) -shows its use

#list APPEND
# students = ["ram","shyam","hari","gita"]
# students.append("john") -appends then anything as it is [eg:john in students at last]
#EMPTY
#students.clear() -empties the list

#COPY
#b = students.copy() -copies list uniquely

#COUNT
#count -counts the number of repetition [synt:a.count(4)]
# e=[1,2,3,4,2,3,4,1,2,3,4]
# >>> e.count(3)
# 3
# >>> e.count(4)
# 3
# >>> e.count(2)
# 3

#EXTEND
#extends - appends the value ony (s.extend(y))
# s=[1,2,3,4]
# >>> y=[5,6,7,8]
# >>> s.extend(y)
# >>> s
# [1, 2, 3, 4, 5, 6, 7, 8]
# >>> s.append(y)
# >>> s
# [1, 2, 3, 4, 5, 6, 7, 8, [5, 6, 7, 8]]

#INDEXING
#index -shows the position of the first value [synt:e.index(3)]
#e.index(2,3) shows the position of 2 after position 3
# e=[1,2,3,4,2,3,4,1,2,3,4]
#  e.index(2)
# 1
# >>> e.index(2,3)
# 4

# #INSERT
# a.insert(2,60) inserts value at certain position in list [eg:insert 60 at position 2]
# >>> q.insert(2,60)
# >>> q
# [1, 2, 60, 3]

#POP
#b.pop() -removes value from the last in list
#q.pop(1)-removes specific value from the given indexed value

#EXAMPLE
# >>> q
# [1, 2, 60, 3]
# >>> q.pop(1)
# 2
# >>> q
# [1, 60, 3]
# >>> var =q.pop(1)
# >>> q
# [1, 3]
# >>> var
# 60

#REMOVE
#removes

#REVERSE
#b.reverse() -reverse the list
#b.sort() -arranges in ascending order
#b.sort(reverse=True) _arranges in desceding order

#EXAMPLE
# f=[1,2,3,4,5]
# >>> f
# [1, 2, 3, 4, 5]
# >>> f.reverse
# <built-in method reverse of list object at 0x00000194759B8E80>
# >>> f.reverse()
# >>> f
# [5, 4, 3, 2, 1]
# >>> f.sort()
# >>> f
# [1, 2, 3, 4, 5]
# >>> f.sort(reverse=True)
# >>> f
# [5, 4, 3, 2, 1]

#SYSIMPORT
# >>> import sys
# >>> a=[]
# >>> b=()
# >>> sys.getsizeof(a)
# 56
# >>> sys.getsizeof(b)
# 40
# >>> a=[1,2,3,4,5,6,7,8,9,10]
# >>> b=(1,2,3,4,5,6,7,8,9,10)
# >>> sys.getsizeof(a)
# 152
# >>> sys.getsizeof(b)
# 120

# SET
# r={"fox","cat","rat","bat"}
# >>> r
# {'fox', 'rat', 'bat', 'cat'}
# >>> r
# {'fox', 'rat', 'bat', 'cat'}