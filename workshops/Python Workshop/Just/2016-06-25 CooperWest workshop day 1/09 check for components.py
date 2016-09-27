for g in CurrentFont():
    # if there are components in the glyph
    if g.components:
        # set the color
        g.mark = (1, 0, 1, 1)
    else:
        # if not, reset the color to None
        g.mark = None
