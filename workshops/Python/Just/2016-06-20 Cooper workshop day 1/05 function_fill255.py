def fill255(red, green, blue, alpha=255):
    fill(red/255, green/255, blue/255, alpha/255)

# print fill255

fill(0.9)
rect(30, 40, 500, 600)

# fill(0, 0.3, 0.6, 0.5)
fill(None)
stroke(1, 0, 0)
strokeWidth(30)
oval(180, 160, 500, 600)

r = 61
g = 169
b = 168

##3da9a8
# print hex(r), hex(g), hex(b)

# fill(r/255, g/255, b/255)
stroke(None)
fill255(r, g, b, 243)
# fill255(61, 169, 168, 243)

rect(100, 100, 276, 284)
