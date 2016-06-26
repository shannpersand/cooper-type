# f = CurrentFont()
# print f

g = CurrentGlyph()
print g

print g.name
print g.unicode
print g.width
print len(g)

# g.width = g.width * 2

print g.box #(x, y bottom left, x,y top left)