*This post is based off a Jupyter notebook I made in 2013. You can download
the original [here](https://gist.github.com/asmeurer/6046766).*

This post is based off a
[wiki page](https://github.com/sympy/sympy/wiki/What-happens-when-you-mess-with-hashing)
on the SymPy wiki, which in turn was based on
[a message](https://groups.google.com/forum/#!msg/sympy/pJ2jg2csKgU/0nn21xqZEmwJ)
to the SymPy mailing list.

# What is hashing?

Before we start, let's have a brief introduction to hashing. A
[*hash function*](http://en.wikipedia.org/wiki/Hash_function) is a function
that maps a set of objects to a set of integers. There are many kinds of hash
functions, which satisfy many different properties, but the most important
property that must be satisfied by any hash function is that it be a function
(in the mathematical sense), that is, if two objects are equal, then their
hash should also be equal.

Usually, the set of integers that the hash function maps to is much smaller
than the set of objects, so that there will be multiple objects that hash to
the same value. However, generally for a hash function to be useful, the set
of integers should be large enough, and the hash function well distributed
enough that if two objects hash to the same value, then they are very likely
to be equal.

To summarize, a hash function *must* satisfy the property:

- **If two objects are equal, then their hashes should be equal.**

Additionally, a *good* hash function should satisfy the property:

- **If two objects have the same hash, then they are not likely to be the same
  object.**

Note that, as noted, since there are generally more possible objects than hash
values, two objects may hash to the same value. This is called a
[hash collision](http://en.wikipedia.org/wiki/Hash_collision), and anything
that deals with hashes should be able to deal with them.

This won't be discussed here, but an additional property that a good hash
function should satisfy to be useful is this:

- **The hash of an object should be cheap to compute.**

# What is it used for?

If we have a hash function that satisfies the above properties, then we can
use it to create from a set of object something called a *hash table*.
Suppose we have a collection of objects, and given any object, we want to be
able to compute very quickly if that object belongs to our set. We could store
these objects in an ordered array, but then to determine if it is in the set,
we would have to search potentially through every element of the array (in
other words, an \\(O(n)\\)) algorithm.

With hashing, we can do better. We create what is known as a
[*hash table*](http://en.wikipedia.org/wiki/Hash_table). Instead of storing
the objects in an ordered array, we create an array of buckets, each
corresponding to some hash values. We then hash each object, and store it into
the array corresponding to its hash value (if there are more hash values than
buckets, we distribute them using a second hash function, which can be as
simple as taking the modulus with respect to the number of buckets, `% n`).

This image from
[Wikipedia](http://en.wikipedia.org/wiki/File:Hash_table_3_1_1_0_1_0_0_SP.svg)
shows an example

![img](http://upload.wikimedia.org/wikipedia/commons/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg)

To determine if an object is in a hash table, we only have to hash the object,
and look in the bucket corresponding to that hash. This is an $O(1)$
algorithm, assuming we have a good hash function, because each bucket will
generally hold very few objects, possibly even none.

# Hashing in Python

Python has a built in function that performs a hash called `hash()`.  For many
objects, the hash is not very surprising.  Note, the hashes you see below may
not be the same ones you see if you run the examples, because Python hashing
depends on the architecture of the machine you are running on, and, in newer
versions of Python, hashes are randomized for security purposes.


```py
>>> hash(10)
10
>>> hash(()) # An empty tuple
3527539
>>> hash('a')
12416037344
```


In Python, not all objects are hashable. For example


```py
>>> hash([]) # An empty list
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

This is because Python has an additional restriction on hashing:

- **In order for an object to be hashable, it must be immutable.**

This is important basically because we want the hash of an object to remain
the same across the object's lifetime. But if we have a mutable object, then
that object itself can change over its lifetime. But then according to our
first bullet point above, that object's hash has to change too.

This restriction simplifies hash tables. If we allowed an object's hash to
change while it is in a hash table, we would have to move it to a different
bucket. Not only is this costly, but the hash table would have to *notice*
that this happened; the object itself doesn't know that it is sitting in a
hash table, at least not in the Python implementation.

In Python, there are two objects that correspond to hash tables, `dict` and
`set`. A `dict` is a special kind of hash table called an
[*associative array*](http://en.wikipedia.org/wiki/Associative_array). An
associative array is a hash table where each element of the hash table points
to another object. The other object itself is not hashed.

Think of an associative array as a generalization of a regular array (like a
`list`). In a `list`, the objects are associated to nonnegative integer
indices, like


```py
>>> l = ['a', 'b', 7]
>> l[0]
'a'
>>> l[2]
7
```


In an associative array (i.e., a `dict`) we can index objects by anything, so
long as the key is hashable.


```py
>>> d = {0: 'a', 'hello': ['world']}
>>> d[0]
'a'
>>> d['hello']
['world']
```


Note that only the keys need to be hashable. The values can be anything, even
unhashable objects like `list`.

The uses for associative arrays are boundless. `dict` is one of the most
useful data types in the Python language. Some example uses are

- Extension of `list` with "missing values". For example, `{0: 'a', 2: 7}`
  would correspond to the above list `l` with the value `'b'` corresponding to
  the key `1` removed.

- Representation of a mathematical function with a finite domain.

- A poor-man's database.

- Implementing a [Pythonic version](http://stackoverflow.com/q/60208/161801)
  of the switch-case statement.

The other type of hash table, `set`, more closely matches the definition I
gave above for a hash table. A `set` is just a container of hashable
objects. `set`s are unordered, and can only contain one of each object (this
is why they are called "sets," because this matches the mathematical
definition of a [set](http://en.wikipedia.org/wiki/Set_(mathematics))).

In Python 2.7 or later, you can create a set with `{` and `}`, like `{a, b,
c}`. Otherwise, use `set([a, b, c])`.


```py
>>> s = {0, (), '2'}
>>> s
{0, '2', ()}
>>> s.add(1)
>>> s
{0, 1, '2', ()}
>>> s.add(0)
>>> s
{0, 1, '2', ()}
```


A final note: `set` and `dict` are themselves mutable, and hence not hashable!
There is an immutable version of set called `frozenset`. There are no
immutable dictionaries.


```py
>>> f = frozenset([0, (), '2'])
>>> f
frozenset({0, '2', ()})
>>> hash(f)
-7776452922777075760
>>> # A frozenset, unlike a set, can be used as a dictionary key
>>> d[f] = 'a set'
>>> d
{0: 'a', frozenset({0, '2', ()}): 'a set', 'hello': ['world']}
```


# Creating your own hashable objects

Before we move on, there is one final thing we need to know about hashing in
Python, which is how to create hashes for custom objects. By default, if we
create an object, it will be hashable.


```py
>>> class Nothing(object):
...     pass
...
>>> N = Nothing()
>>> hash(N)
270498113
```


Implementation-wise, the hash is just the object's `id`, which corresponds to
its position in memory. This satisfies the above conditions: it is (extremely)
cheap to compute, and since by default objects in Python compare unequal to
one another, objects with different hashes will be unequal.


```py
>>> M = Nothing()
>>> M == N
False
>>> hash(M)
270498117
>>> hash(M) == hash(N)
False
```

To define a hash function for an object, define the `__hash__` method.


```py
>>> class HashToOne(object):
...     def __hash__(self):
...         return 1
...
>>> HTO = HashToOne()
>>> hash(HTO)
1
```

To set an object as not hashable, set `__hash__` to `None`.


```py
>>> class NotHashable(object):
...     __hash__ = None
...
>>> NH = NotHashable()
>>> hash(NH)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'NotHashable'
```

Finally, to override the equality operator `==`, define `__eq__`.


```py
>>> class AlwaysEqual(object):
...     def __eq__(self, other):
...         if isinstance(other, AlwaysEqual):
...             return True
...        return False
...
>>> AE1 = AlwaysEqual()
>>> AE2 = AlwaysEqual()
>>> AE1 == AE2
True
```

One of the key points that I hope you will take away from this notebook is
that if you override `__eq__`, you **must** also override `__hash__` to
agree. Note that Python 3 will actually require this: in Python 3, you cannot
override `__eq__` and not override `__hash__`. But that's as far as Python
goes in enforcing these rules, as we will see below. In particular, Python
will never actually check that your `__hash__` actually agrees with your
`__eq__`.

# Messing with hashing

Now to the fun stuff. What happens if we break some of the invariants that
Python expects of hashing. Python expects two key invariants to hold

1. **The hash of an object does not change across the object's lifetime (in
   other words, a hashable object should be immutable).**

2. **`a == b` implies `hash(a) == hash(b)` (note that the reverse might not
   hold in the case of a hash collision).**

As we shall see, Python expects, but does not enforce either of these.

## Example 1: Mutating a hash

Let's break rule 1 first. Let's create an object with a hash, and then change
that object's hash over its lifetime, and see what sorts of things can happen.


```py
>>> class Bad(object):
...     def __init__(self, hash): # The object's hash will be hash
...         self.hash = hash
...     def __hash__(self):
...         return self.hash
...
>>> b = Bad(1)
>>> hash(b)
1
>>> d = {b:42}
>>> d[b]
42
>>> b.hash = 2
>>> hash(b)
2
>>> d[b]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: <__main__.Bad object at 0x1047e7438>
```

Here, we implicitly changed the hash of `b` by mutating the attribute of `b`
that is used to compute the hash. As a result, the object is no longer found
in a dictionary, which uses the hash to find the object.

The object is still there, I just can't access it any more.

```py
>>> d
{<__main__.Bad object at 0x1047e7438>: 42}
```

Note that Python doesn't prevent me from doing this. I could make it if I
want, by making `__setattr__` raise `AttributeError`, but even then I could
forcibly change it by modifying the object's `__dict__`. I could try some more
fancy things using descriptors, metaclasses, and/or `__getattribute__`, but
even then, if I knew what was happening, I could probably find a way to change
it. This is what is meant when we say that Python is a "consenting adults"
language.

## Example 2: More mutation

Let's try something even more crazy. Let's make an object that hashes to a
different value each time we look at the hash.


```py
>>> class DifferentHash(object):
...     def __init__(self):
...         self.hashcounter = 0
...     def __hash__(self):
...         self.hashcounter += 1
...         return self.hashcounter
...
>>> DH = DifferentHash()
>>> hash(DH)
1
>>> hash(DH)
2
>>> hash(DH)
3
```


Obviously, if we use `DH` as a key to a dictionary, then it will not work,
because we will run into the same issue we had with `Bad`. But what about
putting `DH` in a `set`.


```py
>>> DHset = {DH, DH, DH}
>>> DHset
{<__main__.DifferentHash at 0x101f79f50>,
 <__main__.DifferentHash at 0x101f79f50>,
 <__main__.DifferentHash at 0x101f79f50>}
```

Woah! We put the exact same object in a `set` three times, and it appeared all
three times. This is not what is supposed to happen with a set.

```py
>>> {1, 1, 1}
{1}
```

What happens when we do stuff with `DHset`?

```py
>>> DHset.remove(DH)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: <__main__.DifferentHash object at 0x1047e75f8>
```

That didn't work, because `set.remove` searches for an object by its hash,
which is different by this point.

Now let's make a copy of `DHset`. The `set.copy` method will create a shallow
copy (meaning that the set container itself will be different, according to
`is` comparison, but the objects themselves will the same, according to `is`
comparison).


```py
>>> DHset2 = DHset.copy()
>>> DHset2 == DHset
True
```


Everything is fine so far. This object is only going to cause trouble if
something recomputes its hash. But remember that the whole reason that we had
trouble with something like `Bad` above is that Python *doesn't* recompute
that hash of an object, unless it has to. So let's do something that will
force it to do so: let's pop an object from one of the sets and add it back
in.


```py
>>> D = DHset.pop()
>>> DHset.add(D)
>>> DHset
{<__main__.DifferentHash at 0x101f79f50>,
 <__main__.DifferentHash at 0x101f79f50>,
 <__main__.DifferentHash at 0x101f79f50>}
>>> DHset2
{<__main__.DifferentHash at 0x101f79f50>,
 <__main__.DifferentHash at 0x101f79f50>,
 <__main__.DifferentHash at 0x101f79f50>}
>>> DHset == DHset2
False
```

There we go. By removing it from the set, we made the set forget about its
hash, so it had to be recomputed when we added it again. This version of
`DHset` now has a `DH` with a different hash than it had before. Thinking back
to `set` being a hash table, in this `DHset`, the three `DH` objects are in
different "buckets" than they were in before. `DHset.__eq__(DHset2)` notices
that the bucket structure is different right away and returns `False`.

By the way, what hash value are we up to these days?

```py
>>> hash(DH)
9
```

## Example 3: When `a == b` does not imply `hash(a) == hash(b)`

Now let's look at point 2. What happens if we create an object with `__eq__`
that disagrees with `__hash__`. We actually already have made a class like
this, the `AlwaysEqual` object above. Instances of `AlwaysEqual` will always
compare equal to one another, but they will not have the same hash, because
they will use `object`'s default `__hash__` of `id`. Let's take a closer look
at the `AE1` and `AE2` objects we created above.


```py
>>> hash(AE1)
270498221
>>> hash(AE2)
270498197
>>> hash(AE1) == hash(AE2)
False
>>> {AE1, AE2}
{<__main__.AlwaysEqual at 0x101f79950>,
 <__main__.AlwaysEqual at 0x101f79ad0>}
 ```

We can already see that we have broken one of the key properties of a `set`,
which is that it does not contain the same object twice.  This can lead to
subtle issues. For example, suppose we had a list and we wanted to remove all
the duplicate items from it. An easy way to do this is to convert the list to
a set and then convert it back to a list.

```py
>>> l = ['a', 'a', 'c', 'a', 'c', 'b']
>>> list(set(l))
['a', 'c', 'b']
```

Now, this method is obviously not going to work for a list of `AlwaysEqual` objects.

```py
>>> AE3 = AlwaysEqual()
>>> l = [AE1, AE1, AE3, AE2, AE3]
>>> list(set(l))
[<__main__.AlwaysEqual at 0x102c1d590>,
 <__main__.AlwaysEqual at 0x101f79ad0>,
 <__main__.AlwaysEqual at 0x101f79950>]
```

Actually, what happened here is that the equality that we defined on
`AlwaysEqual` was essentially ignored. We got a list of unique items by `id`,
instead of by `__eq__`. You can imagine that if `__eq__` were something a
little less trivial, where some, but not all, objects are considered equal,
that this could lead to very subtle issues.

But there is an issue with the above algorithm. It isn't stable, that is, it
removes the ordering that we had on the list. We could do this better by
making a new list, and looping through the old one, adding elements to the new
list if they aren't already there.


```py
>>> def uniq(l):
...     newl = []
...     for i in l:
...         if i not in newl:
...             newl.append(i)
...     return newl
...
>>> uniq(['a', 'a', 'c', 'a', 'c', 'b'])
['a', 'c', 'b']
>>> uniq([AE1, AE1, AE3, AE2, AE3])
[<__main__.AlwaysEqual at 0x101f79ad0>]
```

This time, we used `in`, which uses `==`, so we got only one unique element of
the list of `AlwaysEqual` objects.

But there is an issue with this algorithm. Checking if something is in a list
is \\(O(n)\\), but we have an object that allows checking in \\(O(1)\\) time,
namely, a set. So a more efficient version might be:


```py
>>> def uniq2(l):
...     newl = []
...     newlset = set()
...     for i in l:
...         if i not in newlset:
...             newl.append(i)
...             newlset.add(i)
...     return newl
...
>>> uniq2(['a', 'a', 'c', 'a', 'c', 'b'])
['a', 'c', 'b']
>>> uniq2([AE1, AE1, AE3, AE2, AE3])
[<__main__.AlwaysEqual at 0x101f79ad0>,
 <__main__.AlwaysEqual at 0x102c1d590>,
 <__main__.AlwaysEqual at 0x101f79950>]
```

Bah! But now, since we used a set, we compared by hashing, not equality, so we
are left with three objects again. Notice the extremely subtle difference
here. Basically, it is this:

```py
>>> AE1 in {AE2}
False
>>> AE1 in [AE2]
True
```

Set containment uses hashing; list containment uses equality. If the two don't
agree, then the result of your algorithm will depend on which one you use!

By the way, as you might expect, dictionary containment also uses hashing, and
tuple containment uses equality:

```py
>>> AE1 in {AE2: 42}
False
>>> AE1 in (AE2,)
True
```

## Example 4: Caching hashing

If you ever want to add subtle bizarreness to a system, add some sort of
caching, and then do it wrong.

As we noted in the beginning, one important property of a hash function is
that it is quick to compute. A nice way to achieve this for heavily cached
objects is to cache the value of the cache on the object, so that it only
needs to be computed once. The pattern (which is modeled after SymPy's
`Basic`) is something like this:


```py
>>> class HashCache(object):
...     def __init__(self, arg):
...         self.arg = arg
...         self.hash_cache = None
...     def __hash__(self):
...         if self.hash_cache is None:
...             self.hash_cache = hash(self.arg)
...         return self.hash_cache
...     def __eq__(self, other):
...         if not isinstance(other, HashCache):
...             return False
...         return self.arg == other.arg
...
```

`HashCache` is nothing more than a small wrapper around a hashable argument,
which caches its hash.


```py
>>> hash('a')
12416037344
>>> a = HashCache('a')
>>> hash(a)
12416037344
```

For ordinary Python builtins, simply recomputing the hash will be faster than
the attribute lookup used by `HashCache`. *Note: This uses the `%timeit` magic
from IPython. `%timeit` only works when run in IPython or Jupyter.*

```py
>>> %timeit hash('a')
10000000 loops, best of 3: 69.9 ns per loop
>>> %timeit hash(a)
1000000 loops, best of 3: 328 ns per loop
```

But for a custom object, computing the hash may be more computationally
expensive. As hashing is supposed to agree with equality (as I hope you've
realized by now!), if computing equality is expensive, computing a hash
function that agrees with it might be expensive as well.

As a simple example of where this might be useful, consider a highly nested
tuple, an object whose hash that is relatively expensive to compute.


```py
>>> a = ()
>>> for i in xrange(1000):
...     a = (a,)
...
>>> A = HashCache(a)
```


```py
>>> %timeit hash(a)
100000 loops, best of 3: 9.61 µs per loop
>>> %timeit hash(A)
1000000 loops, best of 3: 325 ns per loop
```

So far, we haven't done anything wrong. `HashCache`, as you may have noticed,
has `__eq__` defined correctly:


```py
>>> HashCache(1) == HashCache(2)
False
>>> HashCache(1) == HashCache(1)
True
```

But what happens if we mutate HashCache. This is different from examples 1 and
2 above, because we will be mutating what happens with equality testing, but
not the hash (because of the cache).

(In the below example, recall that small integers hash to themselves, so
`hash(1) == 1` and `hash(2) == 2`.)


```py
>>> a = HashCache(1)
>>> d = {a: 42}
>>> a.arg = 2
>>> hash(a)
1
>>> d[a]
42
```

Because we cached the hash of `a`, which was computed as soon as we created
the dictionary `d`, it remained unchanged when modified the arg to be
`2`. Thus, we can still find the key of the dictionary. But since we have
mutated `a`, the equality testing on it has changed. This means that, as with
the previous example, we are going to have issues with dicts and sets keeping
unique keys and entries (respectively).


```py
>>> a = HashCache(1)
>>> b = HashCache(2)
>>> hash(a)
1
>>> hash(b)
2
>>> b.arg = 1
>>> a == b
True
>>> hash(a) == hash(b)
False
>>> {a, b}
{<__main__.HashCache at 0x102c32050>, <__main__.HashCache at 0x102c32450>}
>>> uniq([a, b])
[<__main__.HashCache at 0x102c32050>]
>>> uniq2([a, b])
[<__main__.HashCache at 0x102c32050>, <__main__.HashCache at 0x102c32450>]
```

Once we mutate `b` so that it compares equal to `a`, we start to have the same sort of issues that we had in example 3 with `AlwaysEqual`. Let's look at an instant replay.


```py
>>> a = HashCache(1)
>>> b = HashCache(2)
>>> b.arg = 1
>>> print a == b
True
>>> print hash(a) == hash(b)
True
>>> print {a, b}
set([<__main__.HashCache object at 0x102c32a10>])
>>> print uniq([a, b])
[<__main__.HashCache object at 0x102c32a50>]
>>> print uniq2([a, b])
[<__main__.HashCache object at 0x102c32a50>]
```


Wait a minute, this time it's different! Comparing it to above, it's pretty
easy to see what was different this time. I left out the part where I showed
the hash of `a` and `b`. When I did that the first time, it cached the hash of
`b`, making it forever be `2`, but when I didn't do it the second time, the
hash had not been cached yet, so the first time it is computed (in the `print
hash(a) == hash(b)` line), `b.arg` has already been changed to `1`.

And herein lies the extreme subtlety: if you mutate an object with that hashes
its cache like this, you will run into issues **only if** you had already
called some function that hashed the object somewhere. Now just about anything
might compute the hash of an object. Or it might not. For example, our `uniq2`
function computes the hash of the objects in its input list, because it stores
them in a set, but `uniq` does not:


```py
>>> a = HashCache(1)
>>> b = HashCache(2)
>>> uniq2([a, b])
>>> b.arg = 1
>>> print a == b
True
>>> print hash(a) == hash(b)
False
>>> print {a, b}
set([<__main__.HashCache object at 0x102c32c50>, <__main__.HashCache object at 0x102c32c10>])
>>> print uniq([a, b])
[<__main__.HashCache object at 0x102c32c50>]
>>> print uniq2([a, b])
[<__main__.HashCache object at 0x102c32c50>, <__main__.HashCache object at 0x102c32c10>]
```

```py
>>> a = HashCache(1)
>>> b = HashCache(2)
>>> uniq([a, b])
>>> b.arg = 1
>>> print a == b
True
>>> print hash(a) == hash(b)
True
>>> print {a, b}
set([<__main__.HashCache object at 0x102c32c90>])
>>> print uniq([a, b])
[<__main__.HashCache object at 0x102c32bd0>]
>>> print uniq2([a, b])
[<__main__.HashCache object at 0x102c32bd0>]
```

The moral of this final example is that if you are going to cache something,
that something had better be immutable.

# Conclusion

The conclusion is this: don't mess with hashing. The two invariants above are
important. Let's restate them here,

1. **The hash of an object must not change across the object's lifetime (in
   other words, a hashable object should be immutable).**

2. **`a == b` implies `hash(a) == hash(b)` (note that the reverse might not
   hold in the case of a hash collision).**

If you don't follow these rules, you will run into very subtle issues, because
very basic Python operations expect these invariants.

If you want to be able to mutate an object's properties, you have two
options. First, make the object unhashable (set `__hash__ = None`). You won't
be able to use it in sets or as keys to a dictionary, but you will be free to
change the object in-place however you want.

A second option is to make all mutable properties non-dependent on hashing or
equality testing. This option works well if you just want to cache some
internal state that doesn't inherently change the object. Both `__eq__` and
`__hash__` should remain unchanged by changes to this state. You may also want
to make sure you use proper getters and setters to prevent modification of
internal state that equality testing and hashing does depend on.

Finally, to keep invariant 2, here are some tips:

- Make sure that the parts of the object that you use to compare equality are
  not themselves mutable. If they are, then your object cannot itself be
  immutable. This means that if `a == b` depends on `a.attr == b.attr`, and
  `a.attr` is a list, then you will need to use a tuple instead (if you want
  `a` to be hashable).

- You don't have to invent a hash function. If you find yourself doing
  bitshifts and XORs, you're doing it wrong. Reuse Python's builtin hashable
  objects. If the hash of your object should depend on the hash of `a` and
  `b`, define `__hash__` to return `hash((a, b))`. If the order of `a` and `b`
  does not matter, use `hash(frozenset([a, b]))`.

- Don't cache something unless you know that the entire cached state will not
  be changed over the lifetime of the cache. Hashable objects are actually
  great for caches. If they properly satisfy invariant 1, and all the state
  that should be cached is part of the hash, then you will not need to
  worry. And the best part is that you can just use `dict` for your cache.

- Unless you really need the performance or memory gains, don't make your
  objects mutable. This makes programs much harder to reason about. Some
  functional programming languages take this idea so far that they don't allow
  any mutable objects.

- Don't worry about the situation where `hash(a) == hash(b)` but `a !=
  b`. This is a hash collision. Unlike the issues we looked at here, hash
  collisions are expected and checked for in Python. For example, our
  `HashToOne` object from the beginning will always hash to 1, but different
  instances will compare unequal. We can see that the right thing is done in
  every case with them.

     ```py
     >>> a = HashToOne()
     >>> b = HashToOne()
     >>> a == b
     False
     >>> hash(a) == hash(b)
     True
     >>> {a, b}
     {<__main__.HashToOne at 0x102c32a10>, <__main__.HashToOne at 0x102c32cd0>}
     >>> uniq([a, b])
     [<__main__.HashToOne at 0x102c32cd0>, <__main__.HashToOne at 0x102c32a10>]
     >>> uniq2([a, b])
     [<__main__.HashToOne at 0x102c32cd0>, <__main__.HashToOne at 0x102c32a10>]
     ```

  The only concern with hash collisions is that too many of them can remove
  the performance gains of `dict` and `set`.

- Conversely, if you are writing something that uses an object's hash, remember
  that hash collisions are possible and unavoidable.

  A classic example of a hash collision is `-1` and `-2`. Remember I
  mentioned above that small integers hash to themselves:

     ```py
     >>> hash(1)
     1
     >>> hash(-3)
     -3
     ```

  The exception to this is `-1`. The CPython interpreter uses `-1` as an error
  state, so -1 is not a valid hash value. Hence, `hash(-1)` can't be `-1`. So
  the Python developers picked the next closest thing.

     ```py
     >>> hash(-1)
     -2
     >>> hash(-2)
     -2
     ```

  If you want to check if something handles hash collisions correctly, this is
  a simple example.  I should also note that the fact that integers hash to
  themselves is an implementation detail of CPython that may not be true in
  alternate Python implementations.

- Finally, we didn't discuss this much here, but don't assume that the hash of
  your object will be the same across Python sessions. In Python 3.3 and up,
  hash values of strings are randomized from a value that is seeded when
  Python starts up. This also affects any object whose hash is computed
  from the hash of strings. In Python 2.7, you can enable hash randomization
  with the `-R` flag to the interpreter. The following are two different
  Python sessions.

     ```py
     >>> print(hash('a'))
     -7750608935454338104
     ```

     ```py
     >>> print(hash('a')
     8897161376854729812
      ```
