One problem solved
##################
:date: 2009-05-25 23:47
:author: asmeurer
:category: Uncategorized
:slug: one-problem-solved

Well, I figured out why my patch files are appearing corrupted to
everyone.  It is close to what I expected.  The files had a Macintosh
character encoding, when everyone was expecting UTF-8.  Changing the
encoding with TextWrangler was easy enough, but now the question is, how
do I make git use this encoding by default?
