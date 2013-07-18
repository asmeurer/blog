More information on my Google Summer of Code project this year
##############################################################
:date: 2010-05-26 17:33
:author: asmeurer
:category: Uncategorized
:slug: more-information-on-my-google-summer-of-code-project-this-year

So, as I noted `here`_, I have been accepted into the Google Summer of
Code program again this year. I mentioned that my project involved
improving the integrator, but I didn't say much other than that. So here
I plan on saying a bit more. If you want more details, you can read my
application `on the SymPy wiki`_.

My goal is to improve the integrator in SymPy, in other words, the back
end to the ``integrate()`` function. This is no easy task. Currently,
SymPy has a pretty decnet integration engine. It is even able to solve
some integrals that no other system is known to be able to solve (the
second integral
`here <http://en.wikipedia.org/wiki/Risch_algorithm#Implementation>`__).
But, as I discovered often many times throughout my work on ODEs last
year, the integrator can often leave something to be desired. There are
two problems that I hope to address.

First, the integrator often fails on elementary integrals. This is
because all of the integration in SymPy is based on a heuristic called
the Risch-Norman algorithm. Symbolic integration has been completely
solved in the form of the Risch algorithm, meaning that there exists an
algorithm to determine if an elementary function has an elementary
antiderivative or not, and to find it if it does. This algorithm, called
the Risch algorithm, is extremely complicated, to the extent that no
computer algebra system has ever completely implemented all the parts of
it. My plan is to begin implementing the full algorithm in SymPy. I
don't expect to finish the whole thing -- as I said no one ever has.
Rather, I hope to make a good headway into what is known as the
transcendental part. The Risch algorithm is broken up into four parts:
rational part, the transcendental part, the algebraic part, and the
mixed part.

The rational part is involves integrating rational functions (functions
of the form $latex \\frac{a\_nx^n + a\_{n-1}x^{n-1} + \\cdots + a\_2x^2
+ a\_1x + a\_0}{b\_nx^n + b\_{n-1}x^{n-1} + \\cdots + b\_2x^2 + a\_1x +
a\_0}$). The rational part is the easiest part in the sense that the
algorithm is the simplest, and also that all rational function integrals
are elementary (a term that I will define later). Rational function
integration is already implemented in sympy in full, though I may give a
brief outline of how it works in a later post.

The transcendental part is the part that I will be implementing this
summer. My guide will be `*Symbolic Integration I: Transcendental
Functions* by Manuel Bronstein`_, which describes and proves the
transcendental part of the algorithm in some 300+ pages. I will try to
explain a little of how the algorithm works in some blog posts, but
understand that it is very complex. Therefore, I will probably explain
it without proving things. If you are interested in buying the book and
learning the algorithm rigorously, the only prerequisites that I can
tell are calculus (so you know what an integral and a derivative are),
and a semester of abstract algebra (you need to know about rings,
fields, ideals, homomorphisms, etc., as well as the various theorems
relating them).

In the book, I am still in the part that develops the theory called
differential algebra necessary to prove the integration algorithm
correct. So to begin the GSoC program, I am working on learning the
polys module in sympy. My method of doing this is to write doctests for
all the functions in the module. It's a daunting task, but it's been
probably the best way of learning how a computer module works that I
have ever tried. You really have to understand all aspects of a function
to write a doctest for it, the types of the parameters and return value,
as well as what the algorithm is actually doing. It's especially helpful
that the code for the functions is right below the docstring for each
function, so I can see how it really works on the inside, removing the
mystery of the module. Furthermore, it will serve as a reference for me
for the remainder of the summer, as well for anyone else who wants to
learn the polys module, or just needs to debug it. I've also ran into
several bugs and inefficiencies in the module that I have taken the
liberty of fixing.

Well that's it for this post. If you want to follow my progress on the
doctests, my branch is
http://github.com/asmeurer/sympy/tree/polydocs-polys9. Note that the
branch will be very unstable until I finish at some point at the end of
this week or the beginning of the next.

.. _here: http://asmeurersympy.wordpress.com/2010/04/26/gsoc-2010/trackback/
.. _on the SymPy wiki: http://wiki.sympy.org/wiki/User:Asmeurer/GSoC2010_Application
.. _`*Symbolic Integration I: Transcendental Functions* by Manuel Bronstein`: http://www.amazon.com/Symbolic-Integration-Transcendental-Computation-Mathematics/dp/3540214933/ref=sr_1_fkmr0_2?ie=UTF8&qid=1274894380&sr=8-2-fkmr0
