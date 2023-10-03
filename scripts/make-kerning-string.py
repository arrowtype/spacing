"""
    A simple way to make some kerning strings, for kerning and/or proofing your kerning.
    
    Use glyph names to generate a kerning proof for e.g. RoboFont Space Center.
    
    You can also edit this to use characters: exclude the spaces, leave out the .split(" "), 
    and remove the slashes and spaces from the pattern.
"""

# space-separate list of glyph names for glyphs you want on the left side of pairs
side1Names = "A V Y L W S".split(" ")

# space-separate list of glyph names for glyphs you want on the right side of pairs
side2Names = "quotesingle quotedbl quoteleft quoteright quotedblleft quotedblright".split(" ")

# Configure the kerning string pattern, if you want to adjust it. side1 glyphs will replace $1, and side2 glyphs will replace $2.
# Add/remove leading slashes and trailing spaces depending whether you want to proof characters or glyph names, especially for InDesign vs RoboFont, etc.
pattern = "HH/$1 /$2 HO/$1 /$2 OO"
# pattern = "nn$1$2no$1$2oo"

# If you want to change the way each pattern is separated, change this. It adds a basic newline (`\n`) by default.
# Change to a space (`" "`) if you want to only use spaces, e.g. as one option for an easy InDesign proof (newlines & columns might be better, though).
# Change to "\\n" at the end of your pattern if you want your output to include newlines in the RoboFont space center.
separator = "\n"

# Set to False if you don’t want to also see each permutation flipped
flip = True

# The code part. This goes through glyph name lists and outputs a proofing list.
for glyphSide1 in side1Names:
    for glyphSide2 in side2Names:
        print(pattern.replace("$1",glyphSide1).replace("$2",glyphSide2), end=separator)
        
        if flip:
            print(pattern.replace("$2",glyphSide1).replace("$1",glyphSide2), end=separator)
