import_module (the (hopefully) last fix for 0.7.0)
##################################################
:date: 2011-06-24 06:59
:author: asmeurer
:category: Uncategorized
:slug: import_module-the-hopefully-last-fix-for-0-7-0

So everything seemed to be ready to go for the 0.7.0 release, when
someone `pointed out`_ a test failure in Python 2.5.

It turned out that there is a bug in numpy (see the `numpy issue page`_
for more information), that was causing the quantum module to fail
entirely when imported in Python 2.5 with numpy installed.

Because there was no easy way around the bug, the solution was to
disable numpy completely in Python 2.5 in the quantum module. But this
entailed writing the following code idiom

| [code language="python"]
|  import sys
|  import warnings

| numpy\_supported = True
|  if sys.version\_info < (2, 6):
|  warnings.warn("Cannot use numpy in Python 2.4/2.5.")
|  numpy\_supported = False
|  else:
|  try:
|  import numpy as np
|  except ImportError:
|  numpy\_supported = False
|  [/code]

in all the half dozen files that import numpy in the quantum module.

So clearly, SymPy needed a more centralized way to handle importing
optional external modules. Hence, I wrote the ``import_module()``
function. The function attempts to import a module given it's name. It
returns the module if it can be imported and None if it cannot. It
supports checking the version of Python or the version of the library
and not importing it if either are too old. It also supports emitting
warnings when the module is not available or the version is too old.
Thus, the above idiom reduces to

| [code language="python"]
|  from sympy.external import import\_module

| np = import\_module('numpy', min\_python\_version=(2, 6))
|  [/code]

And that's it. The function will automatically warn if numpy cannot be
imported because the Python version is too old.

Any kind of ``numpy_supported`` variable in the code can be replaced by
testing the ``np`` variable itself, like

| [code language="python"]
|  if np:
|  # Do some numpy stuff
|  else:
|  # np is None
|  # Do whatever you do when it is not available
|  [/code]

This method has an additional advantage, which is that the warnings can
be customized by setting variable hooks. So, for example, the test
runner can disable all warnings by doing

| [code language="python"]
|  import sympy.external
|  sympy.external.importtools.WARN\_OLD\_VERSION = False
|  sympy.external.importtools.WARN\_NOT\_INSTALLED = False
|  [/code]

I actually did make the test runner do this, and also set both to True
when the ``SYMPY_DEBUG`` environment variable is set to True (by
default, ``WARN_NOT_INSTALLED`` is False and ``WARN_OLD_VERSION`` is
True).

There are some caveats. First, note that the function does it's magic
using the built-in ``__import__()`` function. To import a submodule
(like ``sympy.quantum``), you need to pass some stuff to the
``fromlist`` argument of ``__import__()``. It's also a good idea to pass
names to this if you plan to replicate ``from module import stuff``
(instead of just ``import module``), because some modules use lazy
importing and other magic that prevent you from accessing names directly
from ``module.stuff`` without importing ``stuff`` first.

To do this, just pass the arguments to ``__import__()`` to
``import_module()`` using the ``__import__kwargs`` keyword argument,
like

| [code language="python"]
|  from sympy.external import import\_module
|  # Do this instead of "from matplotlib import pyplot" or "import
matplotlib.pyplot as pyplot"
|  matplotlib = import\_module('matplotlib',
\_\_import\_\_kwargs={'fromlist':['pyplot']})
|  pyplot = matplotlib.pyplot
|  [/code]

Second, for module version checking it looks at ``module.__version__``.
Some modules use a different method (for example, gmpy). You can use the
other method by passing the proper arguments to ``import_module()``. For
example, versions of gmpy lower than 1.03 have a bug that prevent its
use in SymPy (basically, ``int(large mpz)`` did not automatically
convert the number to a ``long``). So to import gmpy, but only if it's
version 1.03 or newer, you would use

| [code language="python"]
|  from sympy.external import import\_module
|  gmpy = import\_module('gmpy', min\_module\_version='1.03',
|  module\_version\_attr='version',
module\_version\_attr\_call\_args=())
|  [/code]

This tells it to check the version of gmpy using ``gmpy.version()``, and
to import it only if it's at least 1.03 (note that this works by the
fact that Python lexicographically compares strings and tuples, so
``'1.02' < '1.03'`` returns True).

The sympy.external module is completely independent of the rest of SymPy
(it does not call ``sympy/__init__.py``), so you can use it even outside
of sympy without the performance penalty that importing all of sympy
might bring.

So, hopefully this is the last issue to fix for the 0.7.0 release. You
can still test it at https://github.com/sympy/sympy/tree/0.7.0. If
people want, I will create another release candidate. Otherwise, I will
release 0.7.0 final on Monday (barring any further problems).

.. _pointed out: https://groups.google.com/d/topic/sympy/9FOPjxC0D6s/discussion
.. _numpy issue page: http://projects.scipy.org/numpy/ticket/1872
