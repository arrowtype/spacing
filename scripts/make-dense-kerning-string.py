"""
    This script generates a dense kerning string for use in a kerning feature in a font.

    Especially useful for proofing kerning, or for kerning in GlyphsApp.
"""

# adjust the order to your liking
roughOrderOfKernConcern = "AYTJFVWKXEFODCGQPRBDSLUZIMNH"

kernString = ""

for c in roughOrderOfKernConcern:
    for c2 in roughOrderOfKernConcern:
        kernString += f"H{c}{c2}{c}H "
    kernString += "\n\n"

print(kernString)

# copy kernString to clipboard using pbcopy (works on mac only, sorry)
import subprocess

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

write_to_clipboard(kernString)