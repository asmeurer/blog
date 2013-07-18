Update for the Beginning of the Summer
######################################
:date: 2011-05-26 05:41
:author: asmeurer
:category: Uncategorized
:slug: update-for-the-beginning-of-the-summer

So the Google Summer of Code coding period officially started on Monday,
and in solidarity with the students, I will be blogging once a week
about various things. Some of the posts will just be about what I have
done that week. Others will be continuations of my Risch Algorithm
series of blog posts (see parts `0`_, `1`_, `2`_, and `3`_).

This week, I will do the former. I have spend the past several weeks
preparing for the release. The main thing right now is to clear out `the
issues that are blocking the release`_. I merged in a branch that
included all of my polys related fixes from my integration3 branch.
Along with similar branch from earlier that had some non-polys related
fixes (like some fixes to the integrals), all of my fixes from
integration3 not directly related to my implementation of the Risch
Algorithm should no be in master.

Once those issues are fixed, I should be ready to make a release
candidate for the release. The last release was over a year ago (March
2010), and we've racked up `quite a few changes`_ since then. A few big
ones are:

-  **The new polys**. This is (in my opinion) the biggest change.
   Because of the new polys, everything is faster, and simplification is
   far more powerful than it was before. This is for a few reasons. The
   biggest reason is that the new polys allow polynomials in any kind of
   expression, not just Symbols. This means that you can do things like
   factor the expression $latex \\cos^2{x} + 2\\cos{x} + 1$. As you can
   imagine, many simplifications of complex expressions are nothing more
   than polynomial simplifications, where the polynomial is in some
   function.

   .. raw:: html

      <p>

   In addition to this, the new polys have a much faster implementation,
   and if you have gmpy installed, it will use that and be even faster.
   There are also several faster algorithms, like a faster algorithm for
   multivariate factorization, that have been implemented. These all
   lead to blazing fast simplification and polynomial minipulation in
   SymPy.
-  **The Quantum Module**. Unfortunatly, I can't say much about this,
   since I don't know anything about quantum physics. Furthermore, at
   the time of the writing of this blog post, that part of the release
   notes hasn't been written yet. Suffice it say that thanks to two GSoC
   projects from last summer (see `this`_ and
   `this <http://code.google.com/p/sympy/wiki/Quantum_Computation_Report>`__
   page), we now have a quantum physics module. A lot of the stuff in
   that module, from my understanding, is unique to SymPy, which is very
   exciting. (By the way, if you're interested in this, Brian Granger
   can tell you more about it).
-  **Various backwards incompatible changes**. We've taken advantage of
   the fact that this will be a point release (0.7.0) to clean up some
   old cruft.

   -  We've renamed the functions ``abs()`` and ``sum()`` to ``Abs()``
      and ``summation()``, respectively, because they conflicted with
      built-in names (although thanks to ``__abs__`` magic,
      ``abs(expr)`` will still work with the built-in ``abs()``
      function).
   -  This will be the last release to support Python 2.4. This will be
      a big benefit to not have to support Python 2.4 anymore after this
      release. There were `a ton of features`_ added in Python 2.5 that
      we have had to either manually re-implement (like any() and
      all()), or have had to do without (like the with statement). Also,
      this will make porting to Python 3 much easier (this is one of our
      GSoC projects).
   -  We split the class Basic, which is the base class of all SymPy
      types, into Basic and a subclass Expr. Mathematical objects like
      ``cos(x)`` or ``x*y*z**2`` are instances of Expr. Objects that do
      not make sense in mathematical expressions, but still want to have
      some of the standard SymPy methods like .args and .subs() are
      Basic. For example, a Set object is Basic, but not Expr.

-  **Lots of little bug fixes and new features**. See the `release
   notes`_.

Once we have the release out, I plan to go back to work on the Risch
Algorithm. I am very close to finishing the exponential case, which
means that once I do, any transcendental elementary function built up of
only exponential extensions could be integrated or proven not to have an
elementary integral by my algorithm. I also want to start getting the
code ready to merge with the main code base, so that it can go in the
next release (0.7.1).

Finally, I want to announce that I have been selected for a `student
sponsorship`_ to the SciPy 2011 conference in Austin, TX in the week of
July 11. Mateusz and I will be presenting a tutorial on SymPy. This will
be the first time I have ever attended a conference, and I am very
excited.

.. _0: http://asmeurersympy.wordpress.com/2010/06/11/integration-of-rational-functions/
.. _1: http://asmeurersympy.wordpress.com/2010/06/30/the-risch-algorithm-part-1/
.. _2: http://asmeurersympy.wordpress.com/2010/07/24/the-risch-algorithm-part-2-elementary-functions/
.. _3: http://asmeurersympy.wordpress.com/2010/08/14/the-risch-algorithm-part-3-liouvilles-theorem/
.. _the issues that are blocking the release: http://code.google.com/p/sympy/issues/list?can=2&q=Milestone%3DRelease0.7.0+&colspec=ID+Type+Status+Priority+Milestone+Owner+Summary+Stars&cells=tiles
.. _quite a few changes: https://github.com/sympy/sympy/wiki/Release-Notes-for-0.7.0
.. _this: http://code.google.com/p/sympy/wiki/SymbolicQMReport
.. _a ton of features: http://docs.python.org/whatsnew/2.5.html
.. _release notes: https://github.com/sympy/sympy/wiki/Release-Notes-for-0.7.0
.. _student sponsorship: http://conference.scipy.org/scipy2011/student.php
