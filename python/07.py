# if the glyph in the current font is wider than 600, mark with orangey color
# for g in CurrentFont():
#     if g.width > 600:
#         g.mark = (1, 0.5, 0.2, 1)
#     else:
#         g.mark = None

# if the glyph in the current font is made with components, mark with some blue
for g in CurrentFont():
    if g.components:
        g.mark = (0, .5, .7, 1)
    else:
        g.mark = None