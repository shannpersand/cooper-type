def add_suffix(this_name, ss_number):
  suffix = ".ss%02i" % ss_number
  full_name = this_name + suffix
  return full_name

glyph_names = ["a", "b", "c", "cacute", "aacute"]
separator = ", "
#initialize empty string
result = ""

# adds the results of the loop to the variable
for this_name in glyph_names:
  result += add_suffix(this_name, 1) + separator
  if len(this_name) == 1:
    result += add_suffix(this_name, 2) + separator
  else:
    result += add_suffix(this_name, 3) + separator

print result
print type(result)

# slicing
print "abcdefghijklmnopqrstuvwxyz"[:5] #prints first 5 items
print "abcdefghijklmnopqrstuvwxyz"[5:] # prints from 5 on
print "abcdefghijklmnopqrstuvwxyz"[::-1] # reverse the string
print "abcdefghijklmnopqrstuvwxyz"[::2] # every other item
print "abcdefghijklmnopqrstuvwxyz"[-1] # last item
print "    abcdefghijklmnopqrstuvwxyz  ".strip().upper()
print "a,b,c,d,e,f,g".split(",")

print glyph_names[::-1]
print "-" * 3

# help(str.upper)

