# for g in CurrentFont():
#     if not g.box:
#         continue

g = CurrentGlyph()
xMin, yMin, xMax, yMax = g.box

g.prepareUndo("draw bounding box")

pen = g.getPen()

Z = 30

pen.moveTo((xMin - Z, yMin))
pen.lineTo((xMin - Z, yMax))
pen.curveTo((xMin - Z, yMax + Z), (xMin - Z, yMax + Z), (xMin, yMax + Z))
pen.lineTo((xMax, yMax + Z))
pen.curveTo((xMax + Z, yMax + Z), (xMax + Z, yMax + Z), (xMax + Z, yMax))
pen.lineTo((xMax + Z, yMin))
pen.curveTo((xMax + Z, yMin - Z), (xMax + Z, yMin - Z), (xMax, yMin - Z))
pen.lineTo((xMin, yMin - Z))
pen.curveTo((xMin - Z, yMin - Z), (xMin - Z, yMin - Z), (xMin - Z, yMin))
pen.closePath()

g.correctDirection()
g.performUndo()
