f = CurrentFont()

g = f["a"]  # give me the glyph with glyphname 'a'

g.prepareUndo("mess with stuff")

g2 = g.copy()
g2.move((50, 40))

f["b"] = g & g2  # the intersection, where both shapes overlap
f["c"] = g | g2  # the union, the two shapes merged
f["d"] = g % g2  # g minus g2
f["e"] = g2 % g  # g2 minus g


g.update()
g.performUndo()
