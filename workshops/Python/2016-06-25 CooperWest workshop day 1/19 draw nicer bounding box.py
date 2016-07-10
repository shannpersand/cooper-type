for g in CurrentFont():
    if not g.box:
        continue
        
    xMin, yMin, xMax, yMax = g.box

    g.prepareUndo("draw bounding box")

    pen = g.getPen()

    additionalSpace = 30

    pen.moveTo((xMin - additionalSpace, yMin))
    pen.lineTo((xMin - additionalSpace, yMax))
    pen.lineTo((xMin, yMax + additionalSpace))
    pen.lineTo((xMax, yMax + additionalSpace))
    pen.lineTo((xMax + additionalSpace, yMax))
    pen.lineTo((xMax + additionalSpace, yMin))
    pen.lineTo((xMax, yMin - additionalSpace))
    pen.lineTo((xMin, yMin - additionalSpace))
    pen.closePath()

    g.performUndo()
