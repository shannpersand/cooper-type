light = OpenFont("DemoFonts/SourceSansPro_0_subset.ufo")
bold = OpenFont("DemoFonts/SourceSansPro_1_subset.ufo")
# intermediate = OpenFont("DemoFonts/SourceSansPro_intermediate.ufo")

# print CurrentFont().selection

glyphNames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print light.info.capHeight
print light.info.xHeight
largerThanXHeight = 1.1
wider = 1.2

# scale the y acces slightly taller than the x height
scaleFactorY = (light.info.xHeight * largerThanXHeight) / light.info.capHeight
# scale the x by slightly wider
scaleFactorX = scaleFactorY * wider

# set t for the interpolation formula
# t = ( x , y )
t = (0.03, 0.08)
# loop over the glyphs

# for apples/items/things/i in appleBasket
for gn in glyphNames:
    # make new glyphs that are named __.sc
    gnsc = gn.lower() + ".sc"
    
    #variables for interpolation
    lightGlyph = light[gn]
    boldGlyph = bold[gn]
    # interpolation formula C = A + t * (B - A)
    gsc = lightGlyph + t * (boldGlyph - lightGlyph)
    # then scale by defined scale factors
    gsc = gsc * (scaleFactorX, scaleFactorY)
    # reassigning the new glyph onto the created small caps glyphs within the light font
    light[gnsc] = gsc
    
    # access that set within the light font
   # light[gnsc] = light[gn]
    # make variable for that set
  #  gsc = light[gnsc]
    # scaled them by factors defined earlier
    # gsc.scale((scaleFactorX, scaleFactorY))
    
    
print "feature c2sc {"
for gn in glyphNames:
    gnsc = gn.lower() + ".sc"
    print "    sub", gn, "by", gnsc, ";"
print "} c2sc;"

print "feature smcp {"
for gn in glyphNames:
    gn = gn.lower()
    gnsc = gn + ".sc"
    print "    sub", gn, "by", gnsc, ";"
print "} smcp;"