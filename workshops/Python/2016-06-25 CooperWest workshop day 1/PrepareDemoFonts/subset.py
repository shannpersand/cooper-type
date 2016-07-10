# Remove all glyphs from the current font that have a unicde higher than 255 (U+00FF),
# but do keep any glyphs that are used as components within that range.

f = CurrentFont()

cmap = f.getCharacterMapping()

glyphsToKeep = set([".notdef"])  # also, don't throw away the .notdef glyph

for i in range(256):
    if i in cmap:
        gn = cmap[i][0]
        glyphsToKeep.add(gn)
        g = f[gn]
        for compo in g.components:
            glyphsToKeep.add(compo.baseGlyph)

for gn in f.keys():
    if gn not in glyphsToKeep:
        del f[gn]

# TODO: do something smarter here :)
f.groups.clear()
f.kerning.clear()

f.update()
