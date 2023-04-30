"""
    A simple way to make some kerning strings, for kerning and/or proofing your kerning.
"""

# space-separate list of glyph names for glyphs you want on the left side of pairs
characters = "abcdefghijklmnopqrstuvwxyz"
# characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# characters = "0123456789"

# The code part. This goes through glyph name lists and outputs a proofing list.
for char in characters:
        print(char + char.join([c for c in characters]) + char)
