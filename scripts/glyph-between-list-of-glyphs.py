"""
    A simple script to generate a list of characters separated by a glyph.

    For example, characters "abcde" separated by "T" should look like: "TaTbcTdTeT"
"""

# charsToTest = "abcdefghijklmnopqrstuvwxyz"
# charsToTest = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charsToTest = "0123456789"

separator = "|"

string = separator + separator.join([c for c in charsToTest]) + separator

print(string)