import colorsys

def interpolate(a, b, t):
    return a + t * (b - a)

nSteps = 13

for i in range(nSteps):
    t = i / (nSteps - 1)

    hue = interpolate(0, 1, t)
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    print r, g, b
    x = interpolate(0, 900, t)

    fill(r, g, b)
    rect(x, 0, 100, 1000)
