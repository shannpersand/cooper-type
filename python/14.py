#g = CurrentGlyph()
f = CurrentFont()

# gets the glyph with name 'a'
g = f["g"]

g.prepareUndo("Mess")

g2 = g.copy()
g2.move((10, 10))

# get the union of the two shapes
# f["a"] = g | g2

# get the intersection of the two shapes
# f["g"] = g & g2

# original minus the moved copy
# f["g"] = g2 % g
f["g"] = g % g2

g.update()
g.performUndo()