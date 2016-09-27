# for <loop variable> in <something to loop over>:
    # block of code to be repeated

print range(5)  # count from zero to 5 (not including 5)
print range(3, 14)  # start at 3, count to 14 (not incl. 14)

# construct a "list" manually:
mylist = [0, 1, 3, 67, -12, 5, "hello!"]
print mylist
print len(mylist)

for i in range(5):
    a = i * 2 + 4
    print i, a

# print "hello"
