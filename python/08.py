import random

g = CurrentGlyph()
randomRange = 20

# tell robofont to get ready to undo
g.prepareUndo("Randomize points")

for contour in g:
    for point in contour.points:
        # print point.x, point.y, point.type
        # if point.y < 150:
        if point.type == "offCurve":
            point.type = "line"
            # point.x -= random.randint(-randomRange, randomRange)
            # point.y -= random.randint(-randomRange, randomRange)
    
        
# tell robofont to update the ui 
g.update()

# tell robofont that it can undo
g.performUndo()

