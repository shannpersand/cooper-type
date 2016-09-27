g = CurrentGlyph()

g.prepareUndo("mess around")

# mess around
# g.scale(2)  # make the shape twice as big
# g.scale(1.2, center=(300, 300))  # specify the center of scaling

# g.scale((1.5, 0.44))  # scale x and y independently

# g.move((100, 200))  # move the shape

# g.move((-300, -300))
# g.rotate(45)
# g.move((300, 300))

# g.skew(-12)

g.update()
g.performUndo()

# help(g.scale)
# help(g.rotate)
# help(g.skew)
