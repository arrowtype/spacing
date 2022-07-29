# Spacing and Kerning Scripts

These are two scripts that are intended to be as simple as possible if you’re new to Python, but also flexible and useful for proofing spacing and kerning in a variety of contexts.

I found myself writing similar little scripts fairly often, so I figured they might be worth saving & sharing in an easy-to-find location.

## General instructions for use:

1. Read the scripts. 
    - Everything at the top between `"""` and `"""` is just documentation.
    - Lines starting with `#` are comments that explain the code.
2. Copy a space-separated list of glyph names from a font editor, then paste these in the place of the glyph name lists of these scripts.
    - In GlyphsApp, select the glyphs you want, right-click (or control-click) and select Copy Glyph Names > Space Separated
    - In RoboFont,  select the glyphs you want, then press OPTION + COMMAND + C
3. Run the script.
    - You could copy & paste it into the Glyphs Macro Panel or the RoboFont Script Window, then run it.
    - You could alternatively run this anywhere else on your system that runs Python.
4. Copy the output text, then paste that into wherever you are working.
5. Space / kern / proof!

### Extra suggestions for `make-spacing-string.py`

The default pattern is `nn/$1 nono/$1 oo`, so it will place each glyph name between `n` and `o` for spacing. This is best for lowercase spacing.
- If you instead want to space uppercase glyphs, try `HH/$1 HOHO/$1 OO`. 
- For numerals, try `0/$1 0808/$1 88`.
- For punctuation, maybe do `nn/$1 nono/$1 oo HH/$1 HOHO/$1 OO`

Or, adjust to suit your current need!

### Extra suggestions for `make-kerning-string.py`

By default, this makes a permutation list of non-flat sided uppercase glyphs, A–Z. This is just an example of something you may wish to kern in most fonts.

Other permutation ideas:
- Basic letters and basic trailing punctuation:
    - `side1Names = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z"`
    - `side2Names = "period comma question quotesingle quoteright colon semicolon"`
- Basic letters and basic leading punctuation:
    - `side1Names = "period questiondown quotesingle quoteleft quoteright"`
    - `side2Names = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z"`
- Uppercase diagonals (and glyphs with irregular sides):
    - `side1Names = "A F J K L T V W X Y"`
    - `side2Names = "A F J K T V W X Y"`
- Uppercase against lowercase:
    - `side1Names = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"`
    - `side2Names = "a b c d e f g h i j k l m n o p q r s t u v w x y z"`
- Uppercase "overhanging glyphs" against lowercase diacritics:
    - `side1Names = "F T V W Y"`
    - `side2Names = "a aacute abreve acircumflex adieresis agrave amacron aogonek aring atilde ae b c cacute ccaron ccedilla d eth dcaron dcroat e eacute ecaron ecircumflex edieresis edotaccent egrave emacron eogonek f g gcommaaccent h i idotless iacute icircumflex idieresis igrave ij imacron iogonek j jdotless k kcommaaccent l lacute lcaron lcommaaccent lslash m n nacute ncaron ncommaaccent ntilde o oacute ocircumflex odieresis ograve ohungarumlaut omacron oslash otilde oe p thorn q r racute rcaron rcommaaccent s sacute scaron scedilla germandbls t tcaron tcedilla u uacute ucircumflex udieresis ugrave uhungarumlaut umacron uogonek uring v w wacute wcircumflex wdieresis wgrave x y yacute ycircumflex ydieresis ygrave z zacute zcaron zdotaccent"` 
      - etc ... or maybe be logical and only use pairs that exist in the real world (requires research)!
- Non-flat sided uppercase glyphs, A–Z.
    - `side1Names = "A B C D E F G I J K L O P Q R S T U V W X Y Z"`
    - `side2Names = "A C G I J O Q S T U V W X Y Z"`

And so on! This is basically just a (very) simplified version of something like the [MetricsMachine](https://extensionstore.robofont.com/extensions/metricsMachine/) pair list builder (without several of its useful options, like compressing groups or adding open/closing punctuation). But, this approach can be still be handy for proofing, working in GlyphsApp, and more!
