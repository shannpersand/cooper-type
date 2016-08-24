f = CurrentFont()

# print f.selection
# f.selection = ["a", "b", "c"]

wideGlyphs = []
for g in f:
    if g.width > 800:
        wideGlyphs.append(g.name)

f.selection = wideGlyphs
