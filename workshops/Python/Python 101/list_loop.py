def addSuffixToName(any_name, set_number):
  """
  Adds stylistic set suffix to name
  uses setNumber to determine the set

  useage:
  addSuffixToName("a", 4)
  --> a.ss04
  """
# take setNumber and put it into the formatted string as defined with 02i
  suffix = ".ss%02i" % set_number # adds formatting for the string indicated by %; 0 padded, 2 digits, i integer, % placeholder
  suffixed_name = any_name + suffix # create the name and assign to variable
  return suffixed_name # return the new name

  # same thing in one line, %s string placeholder, tuple: immutable/unchangeable list
  # return "%s.ss%02i" % (any_name, set_number)

# list:
# prints list as is
# print ["a", "adieresis", "aacute", "agrave", "b", "c", "ccaron"]

# assigns variable to list
glyph_names_list = ["a", "adieresis", "aacute", "agrave", "b", "c", "ccaron"]

# prints list via variable
# print glyph_names_list

# loop variable: temporary variable that items are stored in for the duration of the loop
# loops and prints out each item in the list and concatenates ending
for any_name in glyph_names_list:
  print addSuffixToName(any_name, 1)
#  print any_name + ".ss01"

  # built in length function with comparison operator
  # stylistic set for non-compounds ss02
  if len(any_name) == 1:
    print addSuffixToName(any_name, 2)
    # print any_name + ".ss02"
  else:
    print addSuffixToName(any_name, 3)
    # print any_name + ".ss03"

print "Done."