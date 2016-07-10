# print range(10)

mylist = ["red", "green", "blue"]

# print mylist

# for item in mylist:
#     print item

myotherlist = [12, 432.0, -123, "abc"]

# indexing, negative indices go from the end of the list, -1 being the last item
print myotherlist[2], myotherlist[-1]
myotherlist[2] = 999999
del myotherlist[1]

print myotherlist


print len(myotherlist)
print len(mylist)

mynumberlist = [43, 2, 76, 15, 123, -2]
mynumberlist.append(122)
mynumberlist.insert(2, 44.445)
print mynumberlist
print sorted(mynumberlist)
print mynumberlist
mynumberlist.sort()
print mynumberlist

# [  -2,  2,   15,  43,  44.445,  76,   122,   123  ]
#   0   1    2    3    4         5    6      7      8

# slicing
print mynumberlist[2:7]
