mycolors = {"red": (1, 0, 0), "green": (0, 1, 0), "blue": (0, 0, 1)}


print mycolors
print len(mycolors)

print mycolors["green"]
print mycolors["red"]
print mycolors["blue"]

# print mycolors.keys()
# print mycolors.values()
# print mycolors.items()

mycolors["yellow"] = (1, 1, 0)
# mycolors["red"] = "this is now red!"

print mycolors

if "orange" in mycolors:
    print "yes, the dictionary has a key called 'orange'"
else:
    print "no, the dictionary does not have a key called 'orange'"

del mycolors["red"]
print mycolors

for key in mycolors:
    print key, mycolors[key]

# print mycolorssss
# print globals()['mycolorssss']
# print sorted(globals().keys())
