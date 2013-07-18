Infinitely nested lists in Python
#################################
:date: 2012-09-19 04:21
:author: asmeurer
:category: Uncategorized
:slug: infinitely-nested-lists-in-python

Readers of this blog know that I sometimes like to write about some
`strange`_, `unexpected`_, and `unusual`_ things in Python that I
stumble across. This post is another one of those.

First, look at this

| [code language="py"]
|  >>> a = []
|  >>> a.append(a)
|  >>> a
|  [[...]]
|  [/code]

What am I doing here? I'm creating a list, ``a``, and I'm adding it to
itself. What you end up with is an infinitely nested list. The first
interesting thing about this is that Python is smart enough to not
explode when printing this list. The following should convince you that
``a`` does indeed contain itself.

| [code language="py"]
|  >>> a[0] is a
|  True
|  >>> a[0] == a
|  True
|  [/code]

Now, if you have programmed in C, or a similar language that uses
pointers, this should not come as a surprise to you. Lists in Python,
like most things, do not actually contain the items inside them. Rather,
they contain references (in C terminology, "pointers") to the items
inside them. From this perspective, there is no issue at all with ``a``
containing a pointer to itself.

The first thing I wondered when I saw this was just how clever the
printer was at noticing that the list was infinitely nested. What if we
make the cycle a little more complex?

| [code language="py"]
|  >>> a = []
|  >>> b = []
|  >>> a.append(b)
|  >>> b.append(a)
|  >>> a
|  [[[...]]]
|  >>> b
|  [[[...]]]
|  >>> a[0] is b
|  True
|  >>> b[0] is a
|  True
|  [/code]

So it still works. I had thought that maybe repr just catches
``RuntimeError`` and falls back to printing ``...`` when the list is
nested too deeply, but it turns out that is not true:

| [code language="py"]
|  >>> a = []
|  >>> for i in range(10000):
|  ... a = [a]
|  ...
|  >>> a
|  Traceback (most recent call last):
|  File "<stdin>", line 1, in <module>
|  RuntimeError: maximum recursion depth exceeded while getting the repr
of a list
|  [/code]

And by the way, in case you were wondering, it is possible to catch a
``RuntimeError`` (using the same ``a`` as the previous code block)

| [code language="py"]
|  >>> try:
|  ... print(a)
|  ... except RuntimeError:
|  ... print("no way")
|  ...
|  no way
|  [/code]

(and you also may notice that this is Python 3. Things behave the same
way in Python 2)

Back to infinitely nested lists, we saw that printing works, but there
are some things that don't work.

| [code language="py"]
|  >>> a[0] == b
|  True
|  >>> a[0] == a
|  Traceback (most recent call last):
|  File "<stdin>", line 1, in <module>
|  RuntimeError: maximum recursion depth exceeded in comparison
|  [/code]

``a[0] is b`` holds (i.e., they are exactly the same object in memory),
so ``==`` is able to short-circuit on them. But to test ``a[0] == a`` it
has to recursively compare the elements of ``a`` and ``a[0]``. Since it
is infinitely nested, this leads to a recursion error. Now an
interesting question: why does this happen? Is it because ``==`` on
lists uses a depth first search? If it were somehow possible to compare
these two objects, would they be equal?

One is reminded of `Russel's paradox`_, and the reason why in `axiomatic
set theory`_, sets are not allowed to contain themselves.

Thinking of this brought me to my final question. Is it possible to make
a Python ``set`` that contains itself? The answer is obviously no,
because ``set`` objects can only contain hashable objects, and ``set``
is not hashable. But ``frozenset``, ``set``'s counterpart, is hashable.
So can you create a ``frozenset`` that contains itself? The same for
``tuple``. The method I used for ``a`` above won't work, because ``a``
must be mutable to append it to itself.

.. _strange: http://asmeurersympy.wordpress.com/2009/07/20/modifying-a-list-while-looping-through-it-in-python/
.. _unexpected: http://asmeurersympy.wordpress.com/2010/06/16/strange-python-behavior-can-someone-please-explain-to-me-what-is-going-on-here/
.. _unusual: http://asmeurersympy.wordpress.com/2011/03/15/true-is-true-is-false-is-true-is-false/
.. _Russel's paradox: http://en.wikipedia.org/wiki/Russel%27s_paradox
.. _axiomatic set theory: http://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory
