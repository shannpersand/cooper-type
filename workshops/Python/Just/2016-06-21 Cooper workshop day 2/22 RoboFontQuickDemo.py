from random import randint

print "Hello from RoboFont!"

# print AllFonts()

# f = CurrentFont()

g = CurrentGlyph()

print g.width
# g.width = g.width - 10
print g.name
print g.unicode, hex(g.unicode)  # U+0061

g.prepareUndo("Messing things up")
# print g.selection
for contour in g:
    for pt in contour.points:
        if pt.name == "important_point":
            print pt.name, pt
        if pt.selected:
            print pt, "selected?"
        # print pt.x, pt.y
        if pt.y < 250:
            pt.x = pt.x + randint(-50, 50)
g.update()
g.performUndo()
