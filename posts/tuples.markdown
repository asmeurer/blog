Today, David Beazley wrote a pretty controversial set of tweets:

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr">At the bookstore. I&#39;ll admit I judge Python books by their tuple description. &quot;Read only list?&quot;  Back on the shelf.  Nope.</p>&mdash; David Beazley (@dabeaz) <a href="https://twitter.com/dabeaz/status/778634205395845120">September 21, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr">Usually there&#39;s a sentence nearby &quot;sometimes you need a read only list.&quot; No. No, I haven&#39;t. Not in 20 years. Not even once. Sorry.</p>&mdash; David Beazley (@dabeaz) <a href="https://twitter.com/dabeaz/status/778635637457088512">September 21, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js"
charset="utf-8"></script>
<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr">My main objection is that &quot;read only list&quot; is a lazy description lacking thought. A red flag for every other topic that might be covered.</p>&mdash; David Beazley (@dabeaz) <a href="https://twitter.com/dabeaz/status/778639979052498944">September 21, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js"
charset="utf-8"></script>

There are quite a few good responses to these tweets, both from David and from
others (and from yours truly), so I recommend reading them.

Now to start off, I want to say that I respect the hell out of David Beazley.
The guy literally [wrote the book](http://www.dabeaz.com/cookbook.html) on
Python, and he knows way more about Python than I ever well.

As you probably know, there are two "array" datatypes in Python, `list` and
`tuple`.[^list] The primary difference between the two is that lists are *mutable*,
that is you can change their entries and length after they are created, with
methods like `.append` or `+=`. Tuples, on the other hand, are *immutable*.
Once you create one, you cannot change it. This makes the implementation
simpler (and hence faster, although don't let anyone tell you you should use a
tuple just because it's faster). This, as
[Ned Batchelder](http://nedbatchelder.com/blog/201608/lists_vs_tuples.html)
points out, is the only technical difference between the two.

The the idea that particularly bugs me here is that tuples are primarily
useful as "record" datatypes.

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/AllenDowney">@AllenDowney</a> Better than &quot;read-only-list.&quot; ;-).   Mainly looking for the tuple-as-record description. That&#39;s often what&#39;s missing.</p>&mdash; David Beazley (@dabeaz) <a href="https://twitter.com/dabeaz/status/778685294593716224">September 21, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Tuples are awesome for records. This is both by design—since they have a
fixed shape, the positions in a tuple can be "fixed" values, and by convention—if a
Python programmer sees parentheses instead of square brackets, he is more
likely to see it as such. The `namedtuple` object in the standard library
takes the record idea further by letting you actually name the fields:

``` python
>>> from collections import namedtuple
>>> person = namedtuple('Person', 'name, age')
>>> person('Aaron', 26)
Person(name='Aaron', age=26)
```

But is that really the *only* place you'd want to use a tuple over a list?

Consider five places you might encounter a tuple in using Python, courtesy of
Allen Downey:

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/dabeaz">@dabeaz</a> (1) tuple assignment (2) multiple return values (3) *args (4) output from zip, enumerate, etc (5) key in dictionary</p>&mdash; Allen Downey (@AllenDowney) <a href="https://twitter.com/AllenDowney/status/778691102094176257">September 21, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js"
charset="utf-8"></script>

In code these look like:

1. **Multiple assignments:**

        >>> (a, b) = 1, 2

    (yes, the parentheses are optional here, as they are in many places where a
tuple can be used, but this is still a tuple, or at least it looks like one ;)

2. **Multiple return values:**

    For example,
    [`os.walk`](https://docs.python.org/3/library/os.html#os.walk). This is
    for the most part a special case of using tuples as records.

3. **`*args`:**

        >>> def f(*args):
        ...     print(type(args), args)
        ...
        >>> f(1, 2, 3)
        <class 'tuple'> (1, 2, 3)

4. **Return value from builtins `zip`, `enumerate`, etc.:**

        >>> for i in zip(range(3), 'abc'):
        ...     print(i)
        ...
        (0, 'a')
        (1, 'b')
        (2, 'c')
        >>> for i in enumerate('abc'):
        ...     print(i)
        ...
        (0, 'a')
        (1, 'b')
        (2, 'c')

5. **Dictionary keys:**

        >>> {
        ...     (0, 0): '.',
        ...     (0, 1): ' ',
        ...     (1, 0): '.',
        ...     (1, 1): ' ',
        ... }
        {(0, 1): ' ', (1, 0): '.', (0, 0): '.', (1, 1): ' '}

This last one I find to be very important. You could arguably use a list for
the first four above[^assign] (or Python could have, if it wanted to). But it
is
[impossible](https://asmeurer.github.io/blog/posts/what-happens-when-you-mess-with-hashing-in-python/)
to meaningfully hash a mutable data structure in Python, and hashability is a
requirement for dictionary keys.

However, be careful. Not all tuples are hashable. Tuples can contain
anything, but only tuples of immutable values are hashable. Consider

``` python
>>> t = (1, 2, [3, 4])
>>> t[2].append(5)
>>> t
(1, 2, [3, 4, 5])
```


Such tuples are not hashable, and cannot be used as dictionary keys.

```python
>>> hash(t)
Traceback (most recent call last):
  File "<ipython-input-39-36822ba665ca>", line 1, in <module>
    hash(t)
TypeError: unhashable type: 'list'
```

In fact, this another important usage of tuples, which I consider to be
important, namely tree structures. Say you wanted a simple representation of a
Python syntax tree. You might represent `1 - 2*(-3 + 4)` as

``` python
('-', 1, ('*', 2, ('+', ('-', 3), 4)))
```

This isn't really a record. The meaning of the entries in the tuples is
determined by the first value, not the position. In this example, the length
of the tuple also signifies meaning.

If this looks familiar to you, it's because this is how the language Lisp
represents all programs. This is a common pattern.
[Dask graphs](http://dask.pydata.org/en/latest/graphs.html) use tuples and
dictionaries to represent computations.
[SymPy expression trees](http://docs.sympy.org/latest/tutorial/manipulation.html)
use tuples and Python classes to represent symbolic mathematical expressions.

## Mutability is Bad

My second gripe here is this notion that your default ordered collection
object in Python should be `list`. `tuples` are only to be used as "records",
or if you suspect *might* want to use it as a dictionary key. First off, you
never know when you'll want something to be hashable. Both dictionary keys and
`sets` require hashability. Suppose you want to de-duplicate a collection of
your objects. If you used `list`, you'll either have to write a custom loop that
checks for duplicates, or manually convert them to `tuple` and throw them in a
`set`. If you start with `tuple`, you don't have to worry about it (again,
assuming the entries of the tuples are all hashable as well). And suppose you
had an object like the one above, but using lists
`['-', 1, ['*', 2, ['+', ['-', 3], 4]]]`. To convert this to a hashable
object, you need to write a function that recursively converts each list to a
tuple. See how long it takes you to write that function correctly.

Secondly, mutability is bad. I counted 12 distinct methods on
`list` that mutate it (how many can you remember off the top of your
head?[^mutate]). *Any* object that gets a list anywhere in code can mutate it,
using any one of these methods. All it takes is for someone to forget that
`+=` mutates a list and that they should copy it first for code completely
distant from the origin definition to cause issues.  The hardest bug I ever
debugged had a three character
[fix](https://github.com/inducer/pudb/commit/b979fc5909c8d731eb907fc25f4e97904fb7cbbd),
adding `[:]` to copy a global list that I was
(accidentally) mutating. It took me a several hour airplane ride and some deep
dark magic that I'll leave for another blog post to discover the source of my
problems (the problems I was having appeared to be quite distant from the
actual source).

I propose that Python code in general would be vastly improved if people used
tuple as the default unordered collection, and only switched to list if
mutation was necessary (it's less necessary than you think; you can always
copy a tuple instead of mutating it), rather than defaulting to list and only
switching to tuple when hashability is needed, or some weird "rule of thumb"
that says that you should use tuples if you have a "record" and lists
otherwise. Maybe there's a good reason that `*args` and almost all builtin and
standard library functions return tuples instead of lists. It's harder to
accidentally break someone else's code, or have someone else accidentally
break your code, when your data structures are immutable.

[^list]: I want to avoid saying "a tuple is an immutable list", since "list"
    can be interpreted in two ways, as an English word meaning "ordered
    collection" (in
    which case, the statement is true), or as the Python type `list` (in which
    case, the statement is false—`tuple` is not a subclass of `list`).

[^assign]: Yes,

        >>> [a, b] = 1, 2

    works.

[^mutate]: `__delitem__`, `__iadd__`, `__imul__`, `__setitem__`, `append`, `clear`, `extend`, `insert`,
    `pop`, `remove`, `reverse`, and `sort`.
