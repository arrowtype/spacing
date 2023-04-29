"""
    A simple way to make an arbitrary spacing string.
"""

# Update to make different lists. Use the actual characters, not glyph names.
# characters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
characters = " . , : ; ! ¡ ? ¿ • * # / \ - – _ ( ) { } [ ] ‚ „ “ ” ‘ ’ \" ' @ &"

# Configurable pattern. By default, this will put glyphs between nn and oo
# Remove leading slashes and trailing spaces if you instead want to proof characters (not just glyph names), especially for InDesign, etc.
# Add "\\n" at the end of your pattern if you want your output to include newlines, e.g. for the RoboFont space center
pattern = "HH$1Hnn$1no$1oo$1þ"

# If you want to change the way each pattern is separated, change this. It adds a basic newline (`\n`) by default.
# Change to a space (`" "`) if you want to only use spaces, e.g. as one option for an easy InDesign proof (newlines & columns might be better, though).
# Change to "\\n" at the end of your pattern if you want your output to include newlines in the RoboFont space center.
separator = "\n"

# The code part. This goes through glyph name lists and outputs a proofing list.
for name in characters.split(" "):
    print(pattern.replace("$1",name), end=separator)
