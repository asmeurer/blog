True is True is False is True is False
######################################
:date: 2011-03-15 22:29
:author: asmeurer
:category: Uncategorized
:slug: true-is-true-is-false-is-true-is-false

Time for `another`_ `one`_ of my WTF Python blog posts. Yesterday, I
randomly typed this in a Python session (it was late at night):

| [code language="py"]
|  >>> True is True is False is True is False
|  False
|  [/code]

First a little background, in case you don't know. The ``is`` operator
in Python does exact object comparison in memory. Unlike ``==``, which
only compares it two objects are equal, ``is`` only returns True if both
arguments have the same memory address. So you can have something like:

| [code language="py"]
|  >>> a = 12345
|  >>> b = 12345
|  >>> a == b
|  True
|  >>> a is b
|  False
|  [/code]

Now, there are a handful of Python built-ins that are always equal one
another with the ``is`` operator. ``True`` and ``False`` are two such
constants:

| [code language="py"]
|  >>> a = True
|  >>> b = True
|  >>> a == b
|  True
|  >>> a is b
|  True
|  >>> c = False
|  >>> d = False
|  >>> c == d
|  True
|  >>> c is d
|  True
|  [/code]

Now, going back to the above, we see that each ``is`` returns ``True``
or ``False``, which is then evaluated with the next one. Or at least
that is what you would think is happening. But go back and look at it
again, and see if you can figure out what it should evaluate to. You
could probably guess that something was amiss from the fact that I was
blogging about it. If you haven't figured it out already, look at the
following:

| [code language="py"]
|  >>> True is True is False is True is False
|  False
|  >>> (((True is True) is False) is True) is False
|  True
|  >>> True is (True is (False is (True is False)))
|  True
|  [/code]

So it seems that ``is`` does not associate to the left or to the right.
Let's see if we can figure out what is going on. First off,
``True is True``, etc. do behave as you expect them to:

| [code language="py"]
|  >>> True is True
|  True
|  >>> False is False
|  True
|  >>> True is False
|  False
|  >>> False is True
|  False
|  [/code]

It is when we start using multiple ``is``\ s in the same statement that
we start seeing problems:

| [code language="py"]
|  >>> False is False is False
|  True
|  >>> (False is False) is False
|  False
|  [/code]

So what's going on here? ``False is False`` is True, so maybe it is
short-circuiting somehow.

| [code language="py"]
|  >>> True is False is False
|  False
|  >>> False is False is True
|  False
|  [/code]

No, that is not it. Those reduce to ``False is False`` and
``True is True`` when associating to the left, respectively, and
``True is True`` and ``True is True`` when associating to the right.

Finally, at this point, it occurs to me what is really going on. Have
you figured it out too (or maybe you already knew all along)? Maybe you
can guess it from this statement, which uses ``None``, another built-in
object that always compares equal to itself with the ``is`` operator:

| [code language="py"]
|  >>> None is None is None
|  True
|  [/code]

So you see what is happening? ``is`` doesn't associate at all. Rather,
using multiple ``is``\ s in one statement does multiple comparisons at
once. Any ``a is b is … x`` will return ``True`` if ``a``, ``b``, …, and
``x`` are all equal by the ``is`` operator (they share the same identity
or memory address), and ``False`` otherwise. Actually, this isn't
surprising, since ``==`` works the same way:

| [code language="py"]
|  >>> False == False == False
|  True
|  >>> (False == False) == False
|  False
|  [/code]

This syntax can actually be useful to test equality of three or more
items at once efficiently (Python will not evaluate the same operand
more than once, and it short circuits). But it can be confusing when
comparing with ``True`` or ``False``, since ``a is b`` and ``a == b``
themselves evaluate to one of those values. So remember that it is NOT
associative in any way. Rather, it acts as an n-way comparison.

Finally, as `this table`_ of operator precedence in Python shows, ``is``
and ``==`` have the same precedence in Python. Therefore, it should be
possible to combine the two in these same statement. Indeed, you can:

| [code language="py"]
|  >>> a = 12345
|  >>> b = 12345
|  >>> c = b
|  >>> a == b == c
|  True
|  >>> a is b is c
|  False
|  >>> # Because this is False
|  ...
|  >>> a is b
|  False
|  >>> # But this is True
|  ...
|  >>> b is c
|  True
|  >>> # So we get
|  ...
|  >>> a == b is c
|  True
|  [/code]

.. _another: http://asmeurersympy.wordpress.com/2009/07/20/modifying-a-list-while-looping-through-it-in-python/
.. _one: http://asmeurersympy.wordpress.com/2010/06/16/strange-python-behavior-can-someone-please-explain-to-me-what-is-going-on-here/
.. _this table: http://docs.python.org/reference/expressions.html#summary
