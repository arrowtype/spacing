"""
    A simple way to make some kerning strings, for kerning and/or proofing your kerning.

    Adjusted for open/close pairs, like brackets and quotes.
"""

# # space-separate list of glyph names for glyphs you want on the left side of pairs
# openGlyphs = "braceleft parenleft"

# # space-separate list of glyph names for glyphs you want on the right side of pairs
# # Order must match the openGlyphs list
# closeGlyphs = "braceright parenright"

# dict of open/close glyph pairs
openCloseGlyphs = {
    "braceleft": "braceright",
    "parenleft": "parenright",
}

# space-separate list of glyph names for glyphs you want to check in the middle
middleGlyphs = "zero one two three four five six seven eight nine"

# Configure the kerning string pattern, if you want to adjust it. middleGlyphs will replace $1.
# Remove leading slashes and trailing spaces if you instead want to proof characters (not just glyph names), especially for InDesign, etc.
pattern = "HH/$OPEN /$1 /$CLOSE HOHO/$OPEN /$1 /$CLOSE OO"

# If you want to change the way each pattern is separated, change this. It adds a basic newline (`\n`) by default.
# Change to a space (`" "`) if you want to only use spaces, e.g. as one option for an easy InDesign proof (newlines & columns might be better, though).
# Change to "\\n " at the end of your pattern if you want your output to include newlines in the RoboFont space center.
separator = "\\n "

# The code part. This goes through glyph name lists and outputs a proofing list.
for middleGlyph in middleGlyphs.split(" "):
    for openGlyph, closeGlyph in openCloseGlyphs.items():
        print(pattern.replace("$1",middleGlyph).replace("$OPEN",openGlyph).replace("$CLOSE",closeGlyph), end=str(separator))
