

for g in CurrentFont():
    pen = g.getPen()
    
    g.prepareUndo("Draw Bounding Box")

    if not g.box:
        continue
    # tuple, like a list but immutable
    xMin, yMin, xMax, yMax = g.box

    pen = g.getPen()

    additionalSpace = 20

    pen.moveTo((xMin - additionalSpace, yMin))
    pen.lineTo((xMin - additionalSpace, yMax))
    pen.lineTo((xMin, yMax + additionalSpace))
    pen.lineTo((xMax, yMax + additionalSpace))
    pen.lineTo((xMax + additionalSpace, yMin))
    pen.closePath()

g.performUndo()