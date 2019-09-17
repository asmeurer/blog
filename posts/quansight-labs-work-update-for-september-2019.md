*This post has been cross-posted on the [Quansight Blog](https://labs.quansight.org/blog/).*

As of November, 2018, I have been working at
[Quansight](https://www.quansight.com/). Quansight is a new startup founded by
the same people who started Anaconda, which aims to connect companies and open
source communities, and offers consulting, training, support and mentoring
services. I work under the heading of [Quansight
Labs](https://www.quansight.com/labs). Quansight Labs is a public-benefit
division of Quansight. It provides a home for a "PyData Core Team" which
consists of developers, community managers, designers, and documentation
writers who build open-source technology and grow open-source communities
around all aspects of the AI and Data Science workflow.

My work at Quansight is split between doing open source consulting for various
companies, and working on SymPy.
[SymPy](https://www.sympy.org/en/index.html), for those who do not know, is a
symbolic mathematics library written in pure Python. I am the lead maintainer
of SymPy.

In this post, I will detail some of the open source work that I have done
recently, both as part of my open source consulting, and as part of my work on
SymPy for Quansight Labs.

## Bounds Checking in Numba

As part of work on a client project, I have been working on contributing code
to the [numba](https://numba.pydata.org) project. Numba is a just-in-time
compiler for Python. It lets you write native Python code and with the use of
a simple `@jit` decorator, the code will be automatically sped up using LLVM.
This can result in code that is up to 1000x faster in some cases:

```

In [1]: import numba

In [2]: import numpy

In [3]: def test(x):
   ...:     A = 0
   ...:     for i in range(len(x)):
   ...:         A += i*x[i]
   ...:     return A
   ...:

In [4]: @numba.njit
   ...: def test_jit(x):
   ...:     A = 0
   ...:     for i in range(len(x)):
   ...:         A += i*x[i]
   ...:     return A
   ...:

In [5]: x = numpy.arange(1000)

In [6]: %timeit test(x)
249 µs ± 5.77 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [7]: %timeit test_jit(x)
336 ns ± 0.638 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [8]: 249/.336
Out[8]: 741.0714285714286
```

Numba only works for a subset of Python code, and primarily targets code that
uses NumPy arrays.

Numba, with the help of LLVM, achieves this level of performance through many
optimizations. One thing that it does to improve performance is to remove all
bounds checking from array indexing. This means that if an array index is out
of bounds, instead of receiving an `IndexError`, you will get garbage, or
possibly a segmentation fault.

```
>>> import numpy as np
>>> from numba import njit
>>> def outtabounds(x):
...     A = 0
...     for i in range(1000):
...         A += x[i]
...     return A
>>> x = np.arange(100)
>>> outtabounds(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in outtabounds
IndexError: index 100 is out of bounds for axis 0 with size 100
>>> njit(outtabounds)(x)
-8557904790533229732
```

In numba pull request [#4432](https://github.com/numba/numba/pull/4432), I am
working on adding a flag to njit that will enable bounds checks. This will
remain disabled by default for performance purposes, but it will be able to be
turned on so that you can detect bounds issues like the one above. It will
work like

```
>>> @njit(boundscheck=True)
... def outtabounds(x):
...     A = 0
...     for i in range(1000):
...         A += x[i]
...     return A
>>> x = np.arange(100)
>>> outtabounds(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: index is out of bounds
```

The pull request is still in progress, and many things such as the quality of
the error message reporting will need to be improved. This should make
debugging issues easier for people who write numba code once it is merged.

## removestar

[removestar](https://www.asmeurer.com/removestar/) is a new tool I wrote to
automatically replace `import *` in Python modules with explicit imports.

For those who don't know, Python's `import` statement supports so-called
"wildcard" imports, like

```py
from sympy import *
```

This will import every public name from the `sympy` module into the module
namespace. This is often useful because it saves on typing every name that is
used in the import line. This is especially useful when working interactively,
where you just want to import every name and minimize typing.

However, doing `from module import *` is generally frowned upon in Python. It is
considered acceptable when working interactively at a `python` prompt, or in
`__init__.py` files (removestar skips `__init__.py` files by default).

Some reasons why `import *` is bad:

- It hides which names are actually imported.
- It is difficult both for human readers and static analyzers such as
  pyflakes to tell where a given name comes from when `import *` is used. For
  example, pyflakes cannot detect unused names (for instance, from typos) in
  the presence of `import *`.
- If there are multiple `import *` statements, it may not be clear which names
  come from which module. In some cases, both modules may have a given name,
  but only the second import will end up being used. This can break people's
  intuition that the order of imports in a Python file generally does not
  matter.
- `import *` often imports more names than you would expect. Unless the module
  you import defines `__all__` or carefully `del`s unused names at the module
  level, `import *` will import every public (doesn't start with an
  underscore) name defined in the module file. This can often include things
  like standard library imports or loop variables defined at the top-level of
  the file. For imports from modules (from `__init__.py`), `from module import
  *` will include every submodule defined in that module. Using `__all__` in
  modules and `__init__.py` files is also good practice, as these things are
  also often confusing even for interactive use where `import *` is
  acceptable.
- In Python 3, `import *` is syntactically not allowed inside of a function.

Here are some official Python references stating not to use `import *` in
files:

- [The official Python
  FAQ](https://docs.python.org/3/faq/programming.html?highlight=faq#what-are-the-best-practices-for-using-import-in-a-module):

  > In general, don’t use `from modulename import *`. Doing so clutters the
  > importer’s namespace, and makes it much harder for linters to detect
  > undefined names.

- [PEP 8](https://www.python.org/dev/peps/pep-0008/#imports) (the official
  Python style guide):

  > Wildcard imports (`from <module> import *`) should be avoided, as they
  > make it unclear which names are present in the namespace, confusing both
  > readers and many automated tools.

Unfortunately, if you come across a file in the wild that uses `import *`, it
can be hard to fix it, because you need to find every name in the file that is
imported from the `*`. Removestar makes this easy by finding which names come
from `*` imports and replacing the import lines in the file automatically.

Suppose you have a module `mymod` like

```
mymod/
  | __init__.py
  | a.py
  | b.py
```

With

```py
# mymod/a.py
from .b import *

def func(x):
    return x + y
```

```py
# mymod/b.py
x = 1
y = 2
```

Then `removestar` works like:

```
$ removestar -i mymod/
$ cat mymod/a.py
# mymod/a.py
from .b import y

def func(x):
    return x + y
```

The `-i` flag causes it to edit `a.py` in-place. Without it, it would just
print a diff to the terminal.

For implicit star imports and explicit star imports from the same module,
`removestar` works statically, making use of
[pyflakes](https://github.com/PyCQA/pyflakes). This means none of the code is
actually executed. For external imports, it is not possible to work statically
as external imports may include C extension modules, so in that case, it
imports the names dynamically.

`removestar` can be installed with pip or conda:

```
pip install removestar
```

or if you use conda

```
conda install -c conda-forge removestar
```

## sphinx-math-dollar

