light = OpenFont("DemoFonts/SourceSansPro_0_subset.ufo")
bold = OpenFont("DemoFonts/SourceSansPro_1_subset.ufo")
intermediate = OpenFont("DemoFonts/SourceSansPro_intermediate.ufo")

# create an extended version glyphOrder
for glyphName in light.glyphOrder: #or keys()

    # glyphName = "a"
    targetGlyph = intermediate.newGlyph(glyphName)

    # get the x coordinates from the light but interpolate the y values at 10% between light and bold
    targetGlyph.interpolate((0, 0.1), light[glyphName], bold[glyphName])

    
    horizontalScale = 1.5
    
    # scale horizontally
    targetGlyph.scale((horizontalScale, 1))
    # also scale the wodth
    targetGlyph.width *= horizontalScale

# intermediate ["a"].interpolate((0, 0.8), light["a"], bold["a"])