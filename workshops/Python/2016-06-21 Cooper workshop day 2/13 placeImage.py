# size("LetterLandscape")

def placeImage(imagePath, position, scaleFactor):
    x, y = position
    save()
    translate(x, y)
    scale(scaleFactor)
    image(imagePath, (0, 0))
    restore()

# the path can be a path to a file or a url

p = "http://f.cl.ly/items/1T3x1y372J371p0v1F2Z/drawBot.jpg"

# w, h = imageSize(p)

placeImage(p, (200, 200), 0.5)
placeImage(p, (400, 550), 0.5)
