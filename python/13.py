g = CurrentGlyph()

g.prepareUndo("Mess around")

# mess around
# g.scale(1.2, center=(200,200)) # make it 2x as big
# g.scale((1.5, 0.44)) # scale x and y indpendently

g.move((-100, -100))
g.rotate(45,)
g.move((100, 100))

g.skew(12)

g.update()
g.performUndo()

# help(g.scale)