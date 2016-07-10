import colorsys

# help(colorsys)

r, g, b = colorsys.hsv_to_rgb(0.41, 1.0, 1.0)

print r, g, b
fill(r, g, b)
rect(0, 0, 1000, 1000)