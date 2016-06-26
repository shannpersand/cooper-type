light = OpenFont("DemoFonts/SourceSansPro_0_subset.ufo")
bold = OpenFont("DemoFonts/SourceSansPro_1_subset.ufo")

result = NewFont()

for boldGlyph in bold:
    # set variable for the glyph name
    glyphName = boldGlyph.name
    lightGlyph = light[glyphName]
    
    xCenter = lightGlyph.width / 2
    yCenter = lightGlyph.height / 2
    # decompose the component characters
    boldGlyph.decompose()
    lightGlyph.decompose()
    lightGlyph.scale(.75, center=(xCenter, yCenter))
    # create a variable for the amount to center by
    offset = (boldGlyph.width - lightGlyph.width) / 2
    # move the glyph by the offset amount horizontally
    lightGlyph.move((offset, 0))
    # get the result of the difference between the two glyphs
    result[glyphName] = boldGlyph % lightGlyph
    
light.close()
bold.close()