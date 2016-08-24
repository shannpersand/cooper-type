g = CurrentGlyph()

g.prepareUndo("cornerify")

for contour in g:
    for point in contour.points:
        # turn ALL points into corner points
        point.type = "line"

g.update()
g.performUndo()
