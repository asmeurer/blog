*Note: No Starch Press has sent me a copy of this book for review purposes.*

**SHORT VERSION: *Doing Math with Python* is well written and introduces
topics in a nice, mathematical way. I would recommend it for new users of
SymPy.**

[*Doing Math with Python*](https://www.nostarch.com/doingmathwithpython) by
Amit Saha is a new book published by No Starch Press. The book shows how to
use Python to do high school-level mathematics. It makes heavy use of SymPy in
most chapters, and this review will focus mainly on those parts, as that is
the area I have expertise in.

The book assumes a basic understanding of programming in Python 3, as well as
the the mathematics (although advanced topics are explained). No prior
background in the libraries used, SymPy and matplotlib, is assumed. For this
reason, this book can serve as an introduction to SymPy. Each chapter ends
with some programming exercises, which range from easy exercises to more
advanced ones.

The book has seven chapters. In the first chapter, "Working with numbers",
basic mathematics using pure Python is introduced (no SymPy yet). It should be
noted that Python 3 (not Python 2) is required for this book. One of the
earliest examples in the book (`3/2 == 1.5`) will not work correctly without
it. I applaud this choice, although I might have added a warning to wary
users. (As a side note, in the Appendix, it is recommended to install Python
via [Anaconda](https://www.continuum.io/downloads), which I also
applaud). This chapter also introduces the `fractions` module, which seems odd
since `sympy.Rational` will be used for rational numbers later in the text (to
little harm, however, since SymPy automatically converts `fractions.Fraction`
instances to `sympy.Rational`).

In all, this chapter is a good introduction to the basics of the mathematics
of Python. There is also an introduction to variables and strings. However, as
I noted above, one should really have some background with basic Python before
reading this book, as concepts like flow control and function definition are
assumed.

Chapters 2 and 3 cover plotting with matplotlib and basic statistics,
respectively. I will not say much about the matplotlib chapter, since I know
only basic matplotlib myself. I will note that the chapter covers matplotlib
from a (high school) mathematics point of view, starting with a definition of
the Cartesian plane, which seems a fitting choice for the book.

Chapter 3 shows how to do basic statistics (mean, median, standard deviation,
etc.) using pure Python. This chapter is clearly meant for pedagogical
purposes for basic statistics, since the basic functions `mean`, `median`,
etc. are implemented from scratch (as opposed to using `numpy.mean` or the
standard library `statistics.mean`). This serves as a good introduction to
more Python concepts (like `collections.Counter`) and statistics.

Note that the functions in this chapter assume that the data is the entire
population, not a sample. This is mentioned at the beginning of the chapter,
but not elaborated on. For example, this leads to a different definition of
variance than what might be seen elsewhere (the `calculate_variance` used in
this chapter is `pvariance` in the standard library `statistics` module).

It is good to see that a numerically stable definition of variance is used
here (see [PEP 450](https://www.python.org/dev/peps/pep-0450/) for more
discussion on this). These numerical issues show why it is important to use a
real statistics library rather than a home grown one. In other words, use this
chapter to learn more about statistics and Python, but if you ever need to do
statistics on real data, use a statistics library like `statistics` or
`numpy`. Finally, I should note that this book appears to be written against
Python 3.3, whereas `statistics` was added to the Python standard library in
Python 3.4. Perhaps it will get a mention in future editions.

Chapter 4, "Algebra and Symbolic Math with SymPy" starts the introduction to
SymPy. The chapter starts similar to the
[official SymPy tutorial](http://docs.sympy.org/latest/tutorial/index.html) in
describing what symbolics is, and guiding the reader away from common
misconceptions and gotchas. The chapter does a good job of explaining common
gotchas and avoiding antipatterns.

This chapter may serve as an alternative to the official tutorial. Unlike the
official tutorial, which jumps into
[higher-level mathematics](http://docs.sympy.org/latest/tutorial/simplification.html#powers)
and [broader use-cases](http://docs.sympy.org/latest/tutorial/matrices.html),
this chapter may be better suited to those wishing to use SymPy from the
standpoint of high school mathematics.

My only gripes with this chapter, which, in total, are minor, relate to printing.

1. The typesetting of the pretty printing is inconsistent and in some cases,
   incorrect. Powers are printed in the book using superscript numbers, like

       x²

   However, SymPy prints powers like

        2
       x

   even when Unicode pretty printing is enabled. This is a minor point, but it
   may confuse users. Also, the output appears to use ASCII pretty printing
   (mixed with superscript powers), for example

           x²   x³   x⁴   x⁵
       x + -- + -- + -- + --
           2    3    4    5

   Most users will either get MathJax printing (if they are using the Jupyter
   notebook), or Unicode printing, like

            2    3    4    5
           x    x    x    x
       x + ── + ── + ── + ──
           2    3    4    5

    Again, this is a minor point, but at the very least the correct printing
    looks better than the fake printing used here.

2. Inline with the previous point, I would recommend telling the user to start
   with `init_printing()`. The function is used once to change the order of
   printing to rev-lex (for series printing). There is a link to the
   [tutorial page on printing](http://docs.sympy.org/latest/tutorial/printing.html). That
   page goes into more depth than is necessary for the book, but I would
   recommend at least mentioning to always call `init_printing()`, as 2D
   printing can make a huge difference over the default `str` printing, and it
   obviates the need to call `pprint`.

Chapter 5, "Playing with Sets and Probability" covers SymPy's set objects
(particularly `FiniteSet`) to do some basic set theory and probability. I'm
excited to see this in the book. The sets module in SymPy is relatively new,
but quite powerful. We do not yet have an introduction to the sets module in
the SymPy tutorial. This chapter serves as a good introduction to it (albeit
only with finite sets, but the SymPy functions that operate on infinite sets
are exactly the same as the ones that operate on finite sets). In all, I don't
have much to say about this chapter other than that I was presently surprised
to see it included.

Chapter 6 shows how to draw geometric shapes and fractals with matplotlib. I
again won't say much on this, as I am no matplotlib expert. The ability to
draw leaf fractals and Sierpiński triangles with Python does look
entertaining, and should keep readers enthralled.

Chapter 7, "Solving Calculus Problems" goes into more depth with SymPy. In
particular, assumptions, limits, derivatives, and integrals.  The chapter
alternates between symbolic formulations using SymPy and numeric
calculations (using `evalf`). The numeric calculations are done both for
simple examples and more advanced things (like implementing gradient descent).


I like Saha's approach of first showing unevaluated forms (`Limit`,
`Derivative`, `Integral`), and then evaluating them with `doit()`. This puts
users in the mindset of a mathematical expression being a formula which may or
may not later be "calculated". The opposite approach, using the function
forms, `limit`, `diff`, and `integrate`, which evaluate if they can and return
an unevaluated object if they can't, can be confusing to new users in my
experience. A common new SymPy user question is (some form of) "how do I
evaluate an expression?" (the answer is `doit()`).

I also like that this chapter explains the gotcha of `math.sin(Symbol('x'))`,
although I personally would have included this earlier in the text.

(Side note: now that I look, these are both areas in which the official
tutorial could be improved).


## Summary

This book is a good introduction to doing math with Python, and, for the
chapters that use it, a good basic introduction to SymPy. I would recommend it
to anyone wishing to learn SymPy, but especially to anyone whose knowledge of
mathematics may preclude them from getting the most out of the official SymPy
tutorial.

I imagine this book would work well as a pedagogical tool, either for math
teachers or for self-learners. The exercises in this book should push the
motivated to learn more.

I have a few minor gripes, but no major issues.

You can purchase this book from the
[No Starch Press](https://www.nostarch.com/doingmathwithpython) website, both
as a print book an an ebook. The website also includes a sample chapter
([chapter 1](https://www.nostarch.com/download/Doing%20Math%20with%20Python_sample_Chapter1.pdf)),
code samples from the book, and exercise solutions.
