SymPy 0.7.0 released
####################
:date: 2011-06-29 08:00
:author: asmeurer
:category: Uncategorized
:slug: sympy-0-7-0-released

*Cross posted on the `official SymPy blog`_*

| SymPy 0.7.0 has been released on June 28, 2011. It is available at
| `
http://sympy.org`_

| The source distribution can be downloaded from:
| `http://sympy.googlecode.com/files/sympy-0.6.7.tar.gz`_

| You can get the Windows installer here:
| `http://sympy.googlecode.com/files/sympy-0.6.7.win32.exe`_

| And the html documentation here:
| `http://sympy.googlecode.com/files/sympy-0.6.7-docs-html.zip`_\ 

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

About SymPy

.. raw:: html

   </p>

.. raw:: html

   <p>

| SymPy is a Python library for symbolic mathematics. It aims to become
a full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.
SymPy is written entirely in Python.
| 
| 

.. raw:: html

   </div>

.. raw:: html

   <div>

| Changes since last stable release
| 

.. raw:: html

   </div>

.. raw:: html

   <div>

\ **
**\ 

.. raw:: html

   </div>

.. raw:: html

   <div>

\ **(from
https://github.com/sympy/sympy/wiki/Release-Notes-for-0.7.0)**\ 

.. raw:: html

   </div>

.. raw:: html

   <div>

\ **
**

.. raw:: html

   <p>

.. raw:: html

   </div>

.. raw:: html

   <div>

\ **
**

Backwards compatibility breaks
------------------------------

.. raw:: html

   <p>

.. raw:: html

   </div>

.. raw:: html

   <div>

\ ****

-  This will be the last release of SymPy to support Python 2.4.
   Dropping support for Python 2.4 will let us move forward with things
   like supporting Python 3, and will let us use things that were
   introduced in Python 2.5, like with-statement context managers.
-  no longer support creating matrices without brackets (see: issue 930)
-  Renamed ``sum()`` to ``summation()`` (see: 3e763a8, issues 1376,
   1727). This was changed so that it no longer overrides the built-in
   ``sum()``. The unevaluated summation is still called ``Sum()``.
-  Renamed ``abs()`` to ``Abs()`` (see: 64a12a4, issue 1727). This was
   also changed so that it no longer overrides the built-in ``abs()``.
   Note that because of ``__abs__`` magic, you can still do
   ``abs(expr)`` with the built-in ``abs()``, and it will return
   ``Abs(expr)``.
-  Renamed ``max_()`` and ``min_()`` to now ``Max()`` and ``Min()``
   (see: 99a271e, issue 2153)
-  Changed behaviour of ``symbols()``. ``symbols('xyz')`` gives now a
   single symbol (``'xyz'``), not three (``'x'``, ``'y'`` and ``'z'``)
   (see: f6452a8). Use\ ``symbols('x,y,z')`` or ``symbols('x y z')`` to
   get three symbols. The 'each\_char' option will still work but is
   being deprecated.
-  Split class ``Basic`` into new classes ``Expr``, ``Boolean`` (see:
   a0ab479, 635d89c). Classes that are designed to be part of standard
   symbolic expressions (like ``x**2*sin(x)``) should subclass from
   ``Expr``. More generic objects that do not work in symbolic
   expressions but still want the basic SymPy structure like ``.args``
   and basic methods like ``.subs()`` should only subclass from
   ``Basic``.
-  ``as_basic()`` method was renamed to ``as_expr()`` to reflect changes
   in the core (see: e61819d, 80dfe91)
-  Methods ``as_coeff_terms`` and ``as_coeff_factors`` were renamed to
   ``as_coeff_mul`` and ``as_coeff_add``, respectively.
-  Removed the ``trim()`` function. The function is redundant with the
   new polys (see below). Use the ``cancel()`` function instead.

Major Changes
-------------

Polys
~~~~~

-  New internal representations of dense and sparse polynomials (see:
   6aecdb7, 31c9aa4)
-  Implemented algorithms for real and complex root isolation and
   counting (see: 3acac67, 4b75dae, fa1206e, 103b928, 45c9b22, 8870c8b,
   b348b30)
-  Improved Gröbner bases algorithm (see: ff65e9f, 891e4de, 310a585)
-  Field isomorphism algorithm (see: b097b01, 08482bf)
-  Implemented efficient orthogonal polynomials (see: b8fbd59)
-  Added configuration framework for polys (see: 33d8cdb, 7eb81c9)
-  Function for computing minimal polynomials (see: 88bf187, f800f95)
-  Function for generating Viete's formulas (see: 1027408)
-  ``roots()`` supports more classes of polynomials (e.g. cyclotomic)
   (see: d8c8768, 75c8d2d)
-  Added a function for recognizing cyclotomic polynomials (see:
   b9c2a9a)
-  Added a function for computing Horner form of polynomials (see:
   8d235c7)
-  Added a function for computing symmetric reductions of polynomials
   (see: 6d560f3)
-  Added generators of Swinnerton-Dyer, cyclotomic, symmetric, random
   and interpolating polynomials (see: dad03dd, 6ccf20c, dc728d6,
   2f17684, 3004db8)
-  Added a function computing isolation intervals of algebraic numbers
   (see: 37a58f1)
-  Polynomial division (``div()``, ``rem()``, ``quo()``) now defaults to
   a field (see: a72d188)
-  Added wrappers for numerical root finding algorithms (see: 0d98945,
   f638fcf)
-  Added symbolic capabilities to ``factor()``, ``sqf()`` and related
   functions (see: d521c7f, 548120b, f6f74e6, b1c49cd, 3527b64)
-  ``together()`` was significantly improved (see: dc327fe)
-  Added support for iterable containers to ``gcd()`` and ``lcm()``
   (see: e920870)
-  Added a function for constructing domains from coefficient containers
   (see: a8f20e6)
-  Implemented greatest factorial factorization (see: d4dbbb5)
-  Added partial fraction decomposition algorithm based on undetermined
   coefficient approach (see: 9769d49, 496f08f)
-  ``RootOf`` and ``RootSum`` were significantly improved (see: f3e432,
   4c88be6, 41502d7)
-  Added support for gmpy (GNU Multiple Precision Arithmetic Library)
   (see: 38e1683)
-  Allow to compile ``sympy.polys`` with Cython (see: afb3886)
-  Improved configuration of variables in ``Poly`` (see: 22c4061)
-  Added documentation based on Wester's examples (see: 1c23792)
-  Irreducibility testing over finite fields (see: 17e8f1f)
-  Allow symmetric and non-symmetric representations over finite fields
   (see: 60fbff4)
-  More consistent factorization forms from ``factor()`` and ``sqf()``
   (see: 5df77f5)
-  Added support for automatic recognition algebraic extensions (see:
   7de602c)
-  Implemented Collins' modular algorithm for computing resultants (see:
   950969b)
-  Implemented Berlekamp's algorithm for factorization over finite
   fields (see: 70353e9)
-  Implemented Trager's algorithm for factorization over algebraic
   number fields (see: bd0be06)
-  Improved Wang's algorithm for efficient factorization of multivariate
   polynomials (see: 425e225)

Quantum
~~~~~~~

-  Symbolic, abstract dirac notation in ``sympy.physics.quantum``. This
   includes operators, states (bras and kets), commutators,
   anticommutators, dagger, inner products, outer products, tensor
   products and Hilbert spaces
-  Symbolic quantum computing framework that is based on the general
   capabilities in ``sympy.physics.quantum``. This includes qubits
   (``sympy.physics.quantum.qubit``), gates
   (``sympy.physics.quantum.gate``), Grover's algorithm
   (``sympy.physics.quantum.grover``), the quantum Fourier transform
   (``sympy.physics.quantum.qft``), Shor's algorithm
   (``sympy.physics.quantum.shor``) and circuit plotting
   (``sympy.physics.quantum.circuitplot``)
-  Second quantization framework that inclues creation/anihilation
   operators for both Fermions and Bosons and Wick's theorem for
   Fermions (``sympy.physics.secondquant``).
-  Symbolic quantum angular momentum (spin) algebra
   (``sympy.physics.quantum.spin``)
-  Hydrogen wave functions (Schroedinger) and energies (both
   Schroedinger and Dirac)
-  Wave functions and energies for 1D harmonic oscillator
-  Wave functions and energies for 3D spherically symmetric harmonic
   oscillator
-  Wigner and Clebsch Gordan coefficients

Everything else
---------------

-  Implement symarray, providing numpy nd-arrays of symbols.
-  update mpmath to 0.16
-  Add a tensor module (see:
   http://code.google.com/p/sympy/wiki/CodeGenerationReport)
-  A lot of stuff was being imported with ``from sympy import *`` that
   shouldn't have been (like ``sys``). This has been fixed.

Assumptions:
~~~~~~~~~~~~

-  Refine
-  Added predicates (see: 7c0b857, 53f0e1a, d1dd6a3..)
-  Added query handlers for algebraic numbers (see: f3bee7a)
-  Implement a SAT solver (see:
   http://code.google.com/p/sympy/wiki/SuperchargingAssumptionsReport,
   2d96329, acfbe75, etc.)

Concrete
~~~~~~~~

-  Finalized implementation of Gosper's algorithm (see: 0f187e5,
   5888024)
-  Removed redundant ``Sum2`` and related classes (see: ef1f6a7)

Core:
~~~~~

-  Split ``Atom`` into ``Atom`` and ``AtomicExpr`` (see: 965aa91)
-  Various ``sympify()`` improvements
-  Added functionality for action verbs (many functions can be called
   both as global functions and as methods e.g.
   ``a.simplify() == simplify(a)``)
-  Improve handling of rational strings (see: 053a045, issue 1778)
-  Major changes to factoring of integers (see: 273f450, issue 2003)
-  Optimized ``.has()`` (see: c83c9b0, issue 1980; d86d08f)
-  Improvements to power (see: c8661ef, issue 1963)
-  Added range and lexicographic syntax to ``symbols()`` and ``var()``
   (see: f6452a8, 9aeb220, 957745a)
-  Added ``modulus`` argument to ``expand()`` (see: 1ea5be8)
-  Allow to convert ``Interval`` to relational form (see: 4c269fe)
-  SymPy won't manipulate minus sign of expressions any more (see:
   6a26941, 9c6bf0f, e9f4a0a)
-  ``Real`` and ``.is_Real`` were renamed to ``Float`` and
   ``.is_Float``. ``Real`` and ``.is_Real`` still remain as deprecated
   shortcuts to ``Float`` and\ ``is_Float`` for backwards compatibility.
   (see: abe1c49)
-  Methods coeff and as\_coefficient are now non-commutative aware. (see
   a4ea170)

Geometry:
~~~~~~~~~

-  Various improvements to Ellipse
-  Updated documentation to numpy standard
-  Polygon and Line improvements
-  Allow all geometry objects to accept a tuple as ``Point`` args

Integrals:
~~~~~~~~~~

-  Various improvements (see eg. issues 1772, 1999, 1992, 1987.. etc)

isympy
~~~~~~

-  Fixed the ``-p`` switch (see: e8cb04a)
-  Caching can be disabled using ``-C`` switch (see: 0d8d748)
-  Ground types can be set using ``-t`` switch (see: 75734f8)
-  Printing ordering can be set using ``-o`` switch (see: fcc6b13,
   4ec9dc5)

Logic
~~~~~

-  implies object adheres to negative normal form
-  Create new boolean class, ``logic.boolalg.Boolean``
-  Added XOR operator (^) support
-  Added If-then-else (ITE) support
-  Added the dpll algorithm

Functions:
~~~~~~~~~~

-  Added Piecewise, B-splines
-  Spherical Bessel function of the second kind implemented
-  Add series expansions of multivariate functions (see: d4d351d)

Matrices:
~~~~~~~~~

-  Add elementwise product (Hadamard product)
-  Extended QR factorization for general full ranked mxn matrices
-  Remove deprecated functions ``zero()``, ``zeronm()``, ``one()`` (see:
   5da0884)
-  Added cholesky and LDL factorizations, and respective solves.
-  Added functions for efficient triangular and diagonal solves.
-  ``SMatrix`` was renamed to ``SparseMatrix`` (see: acd1685)

Physics
~~~~~~~

-  See the Quantum section

Printing:
~~~~~~~~~

-  Implemented pretty printing of binomials (see: 58c1dad)
-  Implemented pretty printing of Sum() (see: 84f2c22, 95b4321)
-  ``sympy.printing`` now supports ordering of terms and factors (see:
   859bb33)
-  Lexicographic order is now the default. Now finally things will print
   as ``x**2 + x + 1`` instead of ``1 + x + x**2``, however series still
   print using reversed ordering, e.g. ``x - x**3/6 + O(x**5)``. You can
   get the old order (and other orderings) by setting the ``-o`` option
   to isympy (see: 08b4932, a30c5a3)

Series:
~~~~~~~

-  Implement a function to calculate residues, ``residue()``
-  Implement nseries and lseries to handle ``x0 != 0``, series should be
   more robust now (see: 2c99999, issues 2122-2124)
-  Improvements to Gruntz algorithm

Simplify:
~~~~~~~~~

-  Added ``use()`` (see: 147c142)
-  ``ratsimp()`` now uses ``cancel()`` and ``reduced()`` (see: 108fb41)
-  Implemented EPath (see: 696139d, bf90689)
-  a new keyword ``rational`` was added to nsimplify which will replace
   Floats with Rational approximations. (see: 053a045)

Solvers:
~~~~~~~~

-  ODE improvements (see: d12a2aa, 3542041; 73fb9ac)
-  Added support for solving inequalities (see: 328eaba, 8455147,
   f8fcaa7)

Utilities:
~~~~~~~~~~

-  Improve cartes, for generating the Cartesian product (see: b1b10ed)
-  Added a function computing topological sort of graphs (see: b2ce27b)
-  Allow to setup a customized printer in ``lambdify()`` (see: c1ad905)
-  ``flatten()`` was significantly improved (see: 31ed8d7)
-  Major improvements to the Fortran code generator (see:
   http://code.google.com/p/sympy/wiki/CodeGenerationReport, 3383aa3,
   7ab2da2, etc.)

In addition to the more noticeable changes listed above, there have been
numerous other smaller additions, improvements and bug fixes in the
~2000 commits in this release. See the git log for a full list of all
changes. The command ``git log sympy-0.6.7..sympy-0.7.0`` will show all
commits made between this release and the last. You can also see the
issues closed since the last release `here`_.

Authors
-------

The following people contributed at least one patch to this release
(names are given in alphabetical order by last name). A total of 64
people contributed to this release. People with a \* by their names
contributed a patch for the first time for this release. Thirty-seven
people contributed for the first time for this release. Over half of the
people who contributed to this release contributed for the first time!

Thanks to everyone who contributed to this release!

-  Tom Bachmann\*
-  Tomas Bambas\*
-  Matthew Brett\*
-  Ondřej Čertík
-  Renato Coutinho
-  Addison Cugini\*
-  Matt Curry\*
-  Raffaele De Feo\*
-  Mark Dewing
-  Thomas Dixon\*
-  Harold Erbin
-  Pavel Fedotov\*
-  Gilbert Gede\*
-  Oleksandr Gituliar\*
-  Brian Granger
-  Alexey U. Gudchenko\*
-  Øyvind Jensen
-  Fredrik Johansson
-  Felix Kaiser
-  Yuri Karadzhov\*
-  Gary Kerr\*
-  Kibeom Kim\*
-  Nicholas J.S. Kinar\*
-  Anatolii Koval\*
-  Sebastian Krämer
-  Ryan Krauss
-  Gregory Ksionda\*
-  Priit Laes
-  Vladimir Lagunov
-  Ronan Lamy
-  Tomo Lazovich\*
-  Saptarshi Mandal\*
-  David Marek
-  Jack McCaffery\*
-  Benjamin McDonald\*
-  Aaron Meurer
-  Christian Muise\*
-  Óscar Nájera\*
-  Jezreel Ng\*
-  Sherjil Ozair\*
-  Mateusz Paprocki
-  James Pearson
-  Fernando Perez
-  Vladimir Perić\*
-  Mario Pernici\*
-  Nicolas Pourcelot
-  rayman\*
-  Matthew Rocklin\*
-  Christian Schubert
-  Andre de Fortier Smit\*
-  Chris Smith
-  Cristóvão Sousa\*
-  Akshay Srinivasan
-  Vinzent Steinberg
-  Prafullkumar P. Tale\*
-  Andy R. Terrel
-  Kazuo Thow\*
-  Toon Verstraelen
-  Sean Vig\*
-  Luca Weihs\*
-  Thomas Wiecki
-  Shai 'Deshe' Wyborski\*
-  Jeremias Yehdegho\*

.. raw:: html

   <p>

.. raw:: html

   </div>

.. _official SymPy blog: http://sympy.blogspot.com/2011/06/sympy-070-released.html
.. _`
http://sympy.org`: http://sympy.org/
.. _`http://sympy.googlecode.com/files/sympy-0.6.7.tar.gz`: http://sympy.googlecode.com/files/sympy-0.6.6.tar.gz
.. _`http://sympy.googlecode.com/files/sympy-0.6.7.win32.exe`: http://sympy.googlecode.com/files/sympy-0.6.6.win32.exe
.. _`http://sympy.googlecode.com/files/sympy-0.6.7-docs-html.zip`: http://sympy.googlecode.com/files/sympy-0.6.6-docs-html.zip
.. _here: http://code.google.com/p/sympy/issues/list?can=1&q=closed-after%3A2010%2F3%2F17+closed-before%3A2011%2F6%2F13&sort=-closed&colspec=ID+Type+Status+Priority+Milestone+Owner+Summary+Stars+Closed&cells=tiles
