import random

g = CurrentGlyph()

for contour in g:
    print "----- new contour"
    for point in contour.points:
        print point.x, point.y, point.type
