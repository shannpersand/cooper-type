mystring = "Hello there!"

print len(mystring)
print mystring[-6:]

print mystring.startswith("x")
print mystring.startswith("H")
print mystring.startswith("He")
print mystring.startswith("Hell")
print mystring.startswith("Help")
print mystring.endswith("!")
print mystring.endswith("!!")
# does a substring occur in the string
print "ello" in mystring

print mystring.split()
print mystring.strip("!He")
print mystring.lstrip("!He")
print mystring.rstrip("!He")
print mystring