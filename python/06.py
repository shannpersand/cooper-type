# a = 13

# if a > 10:
#     print "a is greater than 10!"
#     print "(another line)"
# else:
#     print 'nope'
    
# if a == 13:
#     print "lucky!"

# if a > 10 and a < 20:
#     print "tween"
    
# if 10 < a < 20:
#     print "tween"
    
f = CurrentFont()

# f.selection = ["a", "b", "c"]

wideGlyphs = []
for g in f:
    if g.width > 600:
        wideGlyphs.append(g.name)

f.selection = wideGlyphs

print f.selection