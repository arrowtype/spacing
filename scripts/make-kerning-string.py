"""
    A simple way to make some kerning strings, for kerning and/or proofing your kerning.
"""

# space-separate list of glyph names for glyphs you want on the left side of pairs
side1Names = "A F J K L T V W X Y"

# space-separate list of glyph names for glyphs you want on the right side of pairs
side2Names = "A F J K T V W X Y"

# Configure the kerning string pattern, if you want to adjust it. side1 glyphs will replace $1, and side2 glyphs will replace $2.
# Remove leading slashes and trailing spaces if you instead want to proof characters (not just glyph names), especially for InDesign, etc.
pattern = "HH/$1 /$2 HOHO/$1 /$2 OO nn/$1 /$2 nono/$1 /$2 oo"

# If you want to change the way each pattern is separated, change this. It adds a basic newline (`\n`) by default.
# Change to a space (`" "`) if you want to only use spaces, e.g. as one option for an easy InDesign proof (newlines & columns might be better, though).
# Change to "\\n" at the end of your pattern if you want your output to include newlines in the RoboFont space center.
separator = "\n"

# The code part. This goes through glyph name lists and outputs a proofing list.
for glyphSide1 in side1Names.split(" "):
    for glyphSide2 in side2Names.split(" "):
        print(pattern.replace("$1",glyphSide1).replace("$2",glyphSide2), end=separator)
