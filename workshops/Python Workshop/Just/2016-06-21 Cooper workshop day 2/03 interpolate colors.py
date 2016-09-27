def interpolate(a, b, t):
    return a + t * (b - a)

r1 = 0.0
g1 = 1.0
b1 = 1.0

r2 = 1.0
g2 = 0.0
b2 = 0.0

nSteps = 5

for i in range(nSteps):
    t = i / (nSteps - 1)

    r = interpolate(r1, r2, t)
    g = interpolate(g1, g2, t)
    b = interpolate(b1, b2, t)
    x = interpolate(0, 900, t)

    fill(r, g, b)
    rect(x, 0, 100, 1000)
