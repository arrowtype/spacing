"""
    A simple way to make some kerning strings, for kerning and/or proofing your kerning.
    Adjusted for open/close pairs, like brackets and quotes.

    Run anywhere you can run Python, then copy and paste the output into e.g. GlyphsApp.
"""

# dict of open/close glyph pairs
open_close_pairs = {
    "‘": "’",
    "’": "‘",
    "“": "”",
    "'": "'",
    "\"": "\"",
    "«": "»",
    "‹": "›",
    "{": "}",
    "[": "]",
    "(": ")",
}

# characters you want to check in the middle
middleChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,:;“”‘’"

# Configure the kerning string pattern, if you want to adjust it.
pattern = "nn{open}{middleChar}{close}nono{open}{middleChar}{close}oo"

# If you want to change the way each pattern is separated, change this. It adds a basic newline (`\n`) by default.
# Change to a space (`" "`) if you want to only use spaces, e.g. as one option for an easy InDesign proof (newlines & columns might be better, though).
# Change to "\\n " at the end of your pattern if you want your output to include newlines in the RoboFont space center.
separator = "\n"

for open, close in open_close_pairs.items():
    for middleChar in [c for c in middleChars]:
        # use pattern as formatted string
        print(pattern.format(open=open, close=close, middleChar=middleChar), end=separator)
