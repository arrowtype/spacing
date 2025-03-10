"""
    A simple way to make some kerning strings, for kerning and/or proofing your kerning.
"""

# space-separate list of glyph names for glyphs you want on the left side of pairs
# characters_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# characters_2 = "abcdefghijklmnopqrstuvwxyz"
characters_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters_1 = ".,’‘“”'\"«»()[]{}_?¿!¡*:;"


# characters = "0123456789"

# The code part. This goes through glyph name lists and outputs a proofing list.
for char_1 in characters_1:
    print("H", end="")
    print(char_1 + char_1.join([c for c in characters_2]) + char_1, end="")
    print("H")
