g = CurrentGlyph()

# (1, 2, 3, 4) tuple, it's like a list, except it is "immutable"

xMin, yMin, xMax, yMax = g.box

# print xMin, yMin, xMax, yMax

g.prepareUndo("draw bounding box")

pen = g.getPen()

pen.moveTo((xMin, yMin))
pen.lineTo((xMin, yMax))
pen.lineTo((xMax, yMax))
pen.lineTo((xMax, yMin))
pen.closePath()

g.performUndo()