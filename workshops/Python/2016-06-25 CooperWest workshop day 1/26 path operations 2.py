light = OpenFont("DemoFonts/SourceSansPro_0_subset.ufo")
bold = OpenFont("DemoFonts/SourceSansPro_1_subset.ufo")

result = NewFont()


for boldGlyph in bold:
    glyphName = boldGlyph.name
    lightGlyph = light[glyphName].copy()
    boldGlyph.decompose()
    lightGlyph.decompose()
    offset = (boldGlyph.width - lightGlyph.width) / 2
    lightGlyph.move((offset, 0))
    result[glyphName] = boldGlyph % lightGlyph
    result[glyphName].width = boldGlyph.width
    # result[glyphName] = boldGlyph
    # result[glyphName].appendGlyph(lightGlyph)

# light.close()
# bold.close()
