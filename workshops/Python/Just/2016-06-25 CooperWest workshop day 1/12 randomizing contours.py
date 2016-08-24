import random

randomRange = 20

g = CurrentGlyph()

g.prepareUndo("Randomize points")

for contour in g:
    for point in contour.points:
        # print point.x, point.y, point.type
        if point.type == "offCurve":
            point.x -= random.randint(randomRange, randomRange)
            point.y -= random.randint(randomRange, randomRange)

g.update()
g.performUndo()
