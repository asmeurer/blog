Title: isympy -I:  A saner interactive environment
Date: 2012-08-31 03:30
Author: asmeurer
Category: Uncategorized
Slug: isympy-i-a-saner-interactive-environment

As [promised][], here is another post describing a new feature in the
upcoming [SymPy 0.7.2][].

Automatic Symbol Definition
---------------------------

While not as ground breaking as the feature I described in my [last
post][promised], this feature is still quite useful. As you may know,
SymPy is inherently a Python library, meaning that it lives by the rules
of Python. If you want to use any name, whether it be a Symbol or a
function (like cos), you need to define it (in the case of Symbols), or
import it (in the case of functions that come with SymPy). We provide
the script `isympy` with SymPy to assist with this. This script
automatically runs IPython (if it's installed), imports all names from
sympy (`from sympy import *`), and defines common symbol names (like
`x`, `y`, and `z`).

But if you want to use a Symbol that is not one of the ones predefined
by `isympy`, you will get something like

[code language="py"]  
In [1]: r\*x  

---------------------------------------------------------------------------  
NameError Traceback (most recent call last)  
in ()  
----\> 1 r\*x

NameError: name 'r' is not defined  
[/code]

The best solution for this has been either to type `var('r')`, which
will create the Symbol `r` and inject it into the namespace, or to wrap
your text in a string and pass it to `sympify()`, like `sympify("r*x")`.
Neither of these are very friendly in interactive mode.

In SymPy 0.7.2, `isympy` has a new command line option, `isympy -a`,
which will enable a mechanism that will automatically define all
undefined names as Symbols for you:

[code language="py"]  
In [1]: r\*x  
Out[1]: r⋅x  
[/code]

There are some caveats to be aware of when using this feature:

-   Names must be undefined for `isympy -a` to work. If you type
    something like `S*x`, you'll get:[code language="py"]  
    In [3]: S\*x  

    ---------------------------------------------------------------------------  
    TypeError Traceback (most recent call last)  
    \<ipython-input-3-6656a97ea7b0\> in \<module\>()  
    ----\> 1 S\*x

    </p>
    TypeError: unsupported operand type(s) for \*: 'SingletonRegistry'
    and 'Symbol'  
    [/code]

    <p>
    That's because `S` is already defined (it's the `SingletonRegistry`,
    and also a shortcut to `sympify()`). To use a name that's already
    defined, either create it manually with `var()` or delete it using
    `del`.

-   This only works on the top level namespace. If you define a function
    with an undefined name, it will not automatically define that symbol
    when run.
-   This works by catching NameError, defining the name, and then
    re-running the expression. If you have a multiline statement, any
    lines before the undefined name will be run before the NameError
    will be caught. This usually won't happen, but it's a potential
    side-effect to be aware of. We plan to rewrite it using either ast
    or tokenize to avoid this issue.
-   Obviously, this is intended for interactive use only. If you copy
    code and put it in a script, or in some other place where someone
    might be expected to run it, but not necessarily from `isympy -a`,
    you should include symbol definitions.

Automatic int to Integer Conversion
-----------------------------------

A second thing that is annoying with Python and SymPy is that something
like `1/2` will be interpreted completely by Python, without any SymPy.
This means that something like `1/2 + x` will give either `0 + x` or
`0.5 + x`, depending on whether or not `__future__.division` has been
imported. `isympy` has always ran `from __future__ import division`, so
that you'll get the latter, but we usually would prefer to get
`Rational(1, 2)`. Previously, the best way to do this was again to
either run it through `sympify()` as a string, or to sympify at least
one of the numbers (here the `S()` shortcut to `sympify()` is useful,
because you can type just `S(1)/2`).

With SymPy 0.7.2, you can run `isympy -i`, and it will automatically
wrap all integers literals with `Integer()`. The result is that `1/2`
produces `Rational(1, 2)`:

[code language="py"]  
In [1]: 1/2 + x  
Out[1]: x + 1/2  
[/code]

Again, there are a couple of caveats:

-   If you want to get Python style division, you just need to wrap both
    arguments in `int()`:[code language="py"]  
    In [2]: int(1)/int(2)  
    Out[2]: 0.5  
    [/code]
    </p>
    <p>
    Of course, if you just want a floating point number, you can just
    use `N()` or `.evalf()`
-   This works by parsing the text and wrapping all integer literals
    with `Integer()`. This means that if you have a variable set to a
    Python int, it will still act like a Python int:[code
    language="py"]  
    In [6]: a = int(1)

    </p>
    In [7]: b = int(2)

    In [8]: a/b  
    Out[8]: 0.5  
    [/code]

    <p>
    Note that to even do that example, I had to manually make `a` and
    `b` Python ints by wrapping them in `int()`. If I had just done
    `a = 1`, it would have been parsed as `a = Integer(1)`, and I would
    have gotten a SymPy Integer. But this can be an issue if you use the
    result of some function that returns an int (again, note that most
    functions in SymPy that return integers return Integer, not int).

-   The same as before: this will only work interactively. If you want
    to reuse your code outside of `isympy -i`, you should take care of
    any int/int by rewriting it as S(int)/int.

Since these are both useful features, we've added a way that you can get
them both at once: by doing `isympy -I` (the "I" stands for
"Interactive"). If we add similar features in the future, we will also
add them to the `-I` shortcut (for example, we may add an option to
allow `^` to automatically be replaced with `**`).

  [promised]: http://asmeurersympy.wordpress.com/2012/08/21/sympy-live-sphinx-extension/
  [SymPy 0.7.2]: https://github.com/sympy/sympy/wiki/Release-Notes-for-0.7.2
