How to make attributes un-inheritable in Python using descriptors
#################################################################
:date: 2013-04-06 02:49
:author: asmeurer
:category: Uncategorized
:slug: how-to-make-attributes-un-inheritable-in-python-using-descriptors

For https://github.com/sympy/sympy/pull/1969, and previous work at
https://github.com/sympy/sympy/pull/1901, we added the ability for the
SymPy doctester to run or not run doctests conditionally depending on
whether or not required external dependencies are installed. This means
that for example we can doctest all the plotting examples without them
failing when matplotlib is not installed.

For functions, this is as easy as decorating the function with
``@doctest_depends``, which adds the attribute ``_doctest_depends_on``
to the function with a list of what dependencies the doctest depends on.
The doctest will then not run the doctest unless those dependencies are
installed.

For classes, this is not so easy. Ideally, one could just define
``_doctest_depends_on`` as an attribute of the class. However, the issue
is that with classes, we have inheritance. But if class ``A`` has a
docstring with a doctest that depends on some modules, it doesn't mean
that a subclass ``B`` of ``A`` will have a doctest that does.

Really, what we need to do is to decorate the docstring itself, not the
class. Unfortunately, Python does not allow adding attributes to strings

| [code language="py"]
|  >>> a = ""
|  >>> a.x = 1
|  Traceback (most recent call last):
|  File "<stdin>", line 1, in <module>
|  AttributeError: 'str' object has no attribute 'x'
|  [/code]

So what we have to do is to create a attribute that doesn't inherit.

I had for some time wanted to give `descriptors`_ in Python a try, since
they are a cool feature, but also the second most complicated feature in
Python (the first is metaclasses). If you don't know what a descriptor
is, I recommend reading `this blog post`_ by Guido van Rossum, the
creator of Python. It's the best explanation of the feature there is.

Basically, Python lets attributes define what happens when they are
accessed (like ``a.x``). You may already know that objects can define
how their attributes are accessed via ``__getattr__``. This is
different. With descriptors, the *attributes themselves* define what
happens. This may sound less useful, but in fact, it's a very core
feature of the language.

If you've ever wondered how ``property``, ``classmethod``, or
``staticmethod`` work in Python, the answer is descriptors. Basically,
if you have something like

| [code language="py"]
|  class A(object):
|  def f(self):
|  return 1
|  f = property(f)
|  [/code]

Then ``A().f`` magically calls what would normally be ``A().f()``. The
way it works is that ``property`` defines the ``__get__`` method, which
returns ``f(obj)``, where ``obj`` is the calling object, here ``A()``
(remember in Python that the first argument of a method, usually called
``self`` is the object that calls the method).

Descriptors can allow method to define arbitrary behavior when called,
set, or deleted. To make an attribute inaccessible to subclasses, then,
you just need to define a descriptor that prevents the attribute from
being accessed if the class of the calling object is not the original
class. Here is some code:

| [code language="py"]
|  class nosubclasses(object):
|  def \_\_init\_\_(self, f, cls):
|  self.f = f
|  self.cls = cls
|  def \_\_get\_\_(self, obj, type=None):
|  if type == self.cls:
|  if hasattr(self.f, '\_\_get\_\_'):
|  return self.f.\_\_get\_\_(obj, type)
|  return self.f
|  raise AttributeError
|  [/code]

it works like this

| [code language="py"]
|  In [2]: class MyClass(object):
|  ...: x = 1
|  ...:

In [3]: MyClass.x = nosubclasses(MyClass.x, MyClass)

| In [4]: class MySubclass(MyClass):
|  ...: pass
|  ...:

| In [5]: MyClass.x
|  Out[5]: 1

| In [6]: MyClass().x
|  Out[6]: 1

| In [80]: MySubclass.x
| 
---------------------------------------------------------------------------
|  AttributeError Traceback (most recent call last)
|  <ipython-input-80-2b2f456dd101> in <module>()
|  ----> 1 MySubclass.x

| <ipython-input-51-7fe1b5063367> in \_\_get\_\_(self, obj, type)
|  8 return self.f.\_\_get\_\_(obj, type)
|  9 return self.f
|  ---> 10 raise AttributeError

AttributeError:

| In [81]: MySubclass().x
| 
---------------------------------------------------------------------------
|  AttributeError Traceback (most recent call last)
|  <ipython-input-81-93764eeb9948> in <module>()
|  ----> 1 MySubclass().x

| <ipython-input-51-7fe1b5063367> in \_\_get\_\_(self, obj, type)
|  8 return self.f.\_\_get\_\_(obj, type)
|  9 return self.f
|  ---> 10 raise AttributeError

| AttributeError:
|  [/code]

Note that by using the third argument to ``__get__``, this works
regardless if the attribute is accessed from the class or the object. I
have to call ``__get__`` on ``self.f`` again if it has it to ensure that
the right thing happens if the attribute has other descriptor logic
defined (and note that regular methods have descriptor logic
defined---that's how they convert the first argument ``self`` to
implicitly be the calling object).

One could easily make class decorator that automatically adds the
attribute to the class in a non-inheritable way:

| [code language="py"]
|  def nosubclass\_x(args):
|  def \_wrapper(cls):
|  cls.x = nosubclasses(args, cls)
|  return cls
|  return \_wrapper
|  [/code]

This automatically adds the property ``x`` to the decorated class with
the value given in the decorator, and it won't be accessible to
subclasses:

| [code language="py"]
|  In [87]: @nosubclass\_x(1)
|  ....: class MyClass(object):
|  ....: pass
|  ....:

| In [88]: MyClass().x
|  Out[88]: 1

| In [89]: MySubclass().x
| 
---------------------------------------------------------------------------
|  AttributeError Traceback (most recent call last)
|  <ipython-input-89-93764eeb9948> in <module>()
|  ----> 1 MySubclass().x

| <ipython-input-51-7fe1b5063367> in \_\_get\_\_(self, obj, type)
|  8 return self.f.\_\_get\_\_(obj, type)
|  9 return self.f
|  ---> 10 raise AttributeError

| AttributeError:
|  [/code]

For SymPy, we can't use class decorators because we still support Python
2.5, and they were introduced in Python 2.6. The best work around is to
just call ``Class.attribute = nosubclasses(Class.attribute, Class)``
after the class definition. Unfortunately, you can't access a class
inside its definition like you can with functions, so this has to go at
the end.

**Name Mangling**

After coming up with all this, I remembered that Python already has a
pretty standard way to define attributes in such a way that subclasses
won't have access to them. All you have to do is use two underscores
before the name, like ``__x``, and it will be `name mangled`_. This
means that the name will be renamed to ``_classname__x`` outside the
class definition. The name will not be inherited by subclasses. There
are some subtleties with this, particularly for strange class names
(names that are too long, or names that begin with an underscore). I
`asked about this on StackOverflow`_. The best answer is that there was
a function in the standard library, but it was removed in Python 3. My
tests reveal that the behavior is different in CPYthon than in PyPy, so
getting it right for every possible class is nontrivial. The descriptor
thing should work everywhere, though. On the other hand,
``getattr(obj, '_' + obj.__class__.__name__ + attributename)`` will work
99% of the time, and is much easier both to write and to understand than
the descriptor.

.. _descriptors: http://docs.python.org/2/howto/descriptor.html
.. _this blog post: http://python-history.blogspot.com/2010/06/inside-story-on-new-style-classes.html?m=1
.. _name mangled: http://docs.python.org/2/reference/expressions.html#atom-identifiers
.. _asked about this on StackOverflow: http://stackoverflow.com/q/15845931/161801
