# Set the unicode value for glyphs that don't have one, yet do appear in the Adobe Glyph List For New Fonts.

from fontTools.agl import AGL2UV

for g in CurrentFont():
    if not g.unicode and g.name in AGL2UV:
        g.unicode = AGL2UV[g.name]
