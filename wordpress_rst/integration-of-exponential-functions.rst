Integration of exponential functions
####################################
:date: 2010-07-12 06:22
:author: asmeurer
:category: Uncategorized
:slug: integration-of-exponential-functions

So for the first time this summer, I missed my blogging deadline. I have
been on vacation for the past few weeks, and have spent a good bit of
the last week in the car, driving home. But that's not my excuse. I was
on vacation the week before, when I wrote up my `lengthy blog post on
the Risch Algorithm`_. My excuse is that I wanted to finish up my
``integrate_hyperexponential()`` function before I posted, so I could
write about it. Well, I finished it on Thursday (today is Sunday, the
post was due Friday), but I ran into unexpected bugs (imagine that) that
has postponed it actually working until now. I also ended up doing API
changes 3 different times (they are basically incrementally all one
change, from supporting only one extension to properly supporting
multiple extensions. Look for long commits in my recent commit history
in my branch if you are interested).

So here is the function. It integrates exponential functions. You still
have to manually create the differential extension, as before. Here are
some examples. You can try them in my `integration2`_ branch (I have
rebased over Mateusz's latest polys9update. The latest branch is always
integration\ ``n``, where ``n`` is the largest integer available).

| **Hover over the code and click on the left-most, "view source" icon
(a paper icon with ``< >`` over it) to view without breaks. Opens in a
new window.**
|  [code language="py"]
|  In [1]: from sympy.integrals.risch import \*

| In [2]: var('t1, t')
|  Out[2]: (t₁, t)

In [3]: r = exp(2\*tan(x))\*tan(x) + tan(x) + exp(tan(x))

| In [4]: r
|  Out[4]:
|  2⋅tan(x) tan(x)
|  ℯ ⋅tan(x) + tan(x) + ℯ

In [5]: rd = r.diff(x)

| In [6]: rd
|  Out[6]:
|  ⎛ 2 ⎞ 2⋅tan(x) 2 ⎛ 2 ⎞ 2⋅tan(x) ⎛ 2 ⎞ tan(x)
|  1 + ⎝2 + 2⋅tan (x)⎠⋅ℯ ⋅tan(x) + tan (x) + ⎝1 + tan (x)⎠⋅ℯ + ⎝1 + tan
(x)⎠⋅ℯ

In [7]: a, d = map(lambda i: Poly(i, t), rd.subs(tan(x),
t1).subs(exp(t1), t).as\_numer\_denom()) # Manually create the extension

| In [8]: a
|  Out[8]: Poly((1 + 2\*t1 + t1\*\*2 + 2\*t1\*\*3)\*t\*\*2 + (1 +
t1\*\*2)\*t + 1 + t1\*\*2, t, domain='ZZ[t1]')

| In [9]: d
|  Out[9]: Poly(1, t, domain='ZZ')

In [10]: integrate\_hyperexponential(a, d, [Poly(1, x), Poly(1 +
t1\*\*2, t1), Poly((1 + t1\*\*2)\*t, t)], [x, t1, t], [lambda x:
exp(tan(x)), tan])

| Out[10]:
|  ⎛ ⌠ ⎞
|  ⎜ 2⋅tan(x) ⎮ ⎛ 2 ⎞ tan(x) ⎟
|  ⎜ℯ ⋅tan(x) + ⎮ ⎝1 + tan (x)⎠ dx + ℯ , True⎟
|  ⎝ ⌡ ⎠
|  [/code]

We have to manually build up the differential extension (``[7]``). The
first element is $latex x$, which is already there. Next, we add $latex
t\_1 = \\tan{x}$, and finally $latex t = e^{\\tan{x}} = e^{t\_1}$. The
third argument of ``integrate_hyperexponential()`` is what gives these
variables their identities: their derivatives. The fourth argument is
the list of the extension symbols, and the last argument is a list of
the functions for which the symbols stand for, in reverse order (because
we have to back substitute in the solution in reverse order).

The unevaluated Integral in the solution is due to the recursive nature
of the Risch algorithm. Eventually, an outer function in the algorithm
will recursively integrate until it reaches the ground field, $latex
\\mathbb{Q}$. It will also do the proper preparsing automatically as
well. The second element of the solution, ``True``, indicates that the
integral is elementary, and thus the given solution is the complete
integral of the original integrand, which we can see ($latex \\int (1 +
\\tan^2{x})dx=\\tan{x}$).

Another example:

[code language="py"]

In [1]: from sympy.integrals.risch import \*

| In [2]: var('t')
|  Out[2]: (t,)

In [3]: rd = exp(-x\*\*2)

| In [4]: rd
|  Out[4]:
|  2
|  -x
|  ℯ

In [5]: a, d = map(lambda i: Poly(i, t), rd.subs(exp(x\*\*2),
t).as\_numer\_denom())

| In [6]: a
|  Out[6]: Poly(1, t, domain='ZZ')

| In [7]: d
|  Out[7]: Poly(t, t, domain='ZZ')

In [8]: integrate\_hyperexponential(a, d, [Poly(1, x), Poly(2\*x\*t,
t)], [x, t], [lambda x: exp(x\*\*2)])

Out[8]: (0, False)

[/code]

Here the second argument of the solution is ``False``, which indicates
that the algorithm has proven that the integral of $latex e^{-x^2}$ is
not elementary! The first argument 0 indicates that actually it is the
integral of $latex e^{-x^2} - \\frac{d}{dx}(0)$ that is not elementary,
i.e., the Risch algorithm will reduce an integrand into an integrated
function part and non-elementary part. For example:

| [code language="py"]
|  In [1]: from sympy.integrals.risch import \*

| In [2]: var('t1, t')
|  Out[2]: (t₁, t)

In [3]: rd = exp(x)/tan(x) + exp(x)/(1 + exp(x))

| In [4]: rd
|  Out[4]:
|  x x
|  ℯ ℯ
|  ────── + ──────
|  x tan(x)
|  1 + ℯ

In [5]: a, d = map(lambda i: Poly(i, t), rd.subs(exp(x), t).subs(tan(x),
t1).as\_numer\_denom())

| In [6]: a
|  Out[6]: Poly(t\*\*2 + (1 + t1)\*t, t, domain='ZZ[t1]')

| In [7]: d
|  Out[7]: Poly(t1\*t + t1, t, domain='ZZ[t1]')

| In [8]: integrate\_hyperexponential(a, d, [Poly(1, x), Poly(1 +
t1\*\*2, t1), Poly(t, t)], [x, t1, t], [exp, tan])
|  Out[8]:
|  ⎛ ⎛ x⎞ ⎞
|  ⎝log⎝1 + ℯ ⎠, False⎠

[/code]

This indicates that the integral of $latex (\\frac{e^x}{\\tan{x}} +
\\frac{e^x}{1 + e^x}) - \\frac{d}{dx}(\\log{(1 + e^x)}) =
\\frac{e^x}{\\tan{x}}$ is not elementary. That is one advantage that the
new algorithm will have over the present one. Currently, the present
algorithm just returns an unevaluated Integral for the above ``rd``, but
the new one will be able to return $latex \\log{(1 + e^x)} +
\\int{\\frac{e^x}{\\tan{x}}dx}$. It will be able to do this even if rd
were rewritten as $latex \\frac{e^x \\tan{x} + e^x + e^{2x}}{e^x
\\tan{x} + \\tan{x}}$ (notice that this is exactly what
``.as_numer_denom()`` is doing anyway in ``[5]``, as you can see in
``[6]`` and ``[7]``). Furthermore, it will have actually *proven* that
the remaining $latex \\int{\\frac{e^x}{\\tan{x}}dx}$ is non-elementary.
I plan on having some kind of marker in the pretty printed unevaluated
``Integral`` to indicate this. Suggestions on what this should be are
welcome.

Finally, the full algorithm appears to be faster (probably
asymptotically faster) than the current implementation:

| [code language="py"]
|  In [1]: from sympy.integrals.risch import \*

| In [2]: var('t1, t')
|  Out[2]: (t₁, t)

In [3]: rd = exp(x)\*x\*\*4

In [4]: a, d = map(lambda i: Poly(i, t), rd.subs(exp(x),
t).as\_numer\_denom())

| In [5]: integrate\_hyperexponential(a, d, [Poly(1, x), Poly(t, t)],
[x, t], [lambda x: exp(x)])
|  Out[5]:
|  ⎛ x 4 x x 3 x 2 x ⎞
|  ⎝24⋅ℯ + x ⋅ℯ - 24⋅x⋅ℯ - 4⋅x ⋅ℯ + 12⋅x ⋅ℯ , True⎠

| In [6]: %timeit integrate\_hyperexponential(a, d, [Poly(1, x), Poly(t,
t)], [x, t], [exp])
|  10 loops, best of 3: 28 ms per loop

| In [7]: integrate(rd, x)
|  Out[7]:
|  x 4 x x 3 x 2 x
|  24⋅ℯ + x ⋅ℯ - 24⋅x⋅ℯ - 4⋅x ⋅ℯ + 12⋅x ⋅ℯ

| In [8]: %timeit integrate(rd, x)
|  1 loops, best of 3: 218 ms per loop

[/code]

Of course, keep in mind that I am timing what will be an internal
function against a full function. But if you increase the exponent on x,
you find that there is no way the addition of preparsing time (which
shouldn't be affected by such a change) will cause it to become as slow
as the current ``integrate()``. Like I said, I am pretty sure that it is
asymptotic. For example:

| [code language="py"]
|  In [1]: from sympy.integrals.risch import \*

| In [2]: var('t1, t')
|  Out[2]: (t₁, t)

In [3]: rd = exp(x)\*x\*\*10

In [4]: a, d = map(lambda i: Poly(i, t), rd.subs(exp(x),
t).as\_numer\_denom())

| In [5]: integrate\_hyperexponential(a, d, [Poly(1, x), Poly(t, t)],
[x, t], [lambda x: exp(x)])
|  Out[5]:
|  ⎛ x 10 x x 3 x 5 x 7 x 9 x 8 x 6 x 4 x 2 x ⎞
|  ⎝3628800⋅ℯ + x ⋅ℯ - 3628800⋅x⋅ℯ - 604800⋅x ⋅ℯ - 30240⋅x ⋅ℯ - 720⋅x ⋅ℯ
- 10⋅x ⋅ℯ + 90⋅x ⋅ℯ + 5040⋅x ⋅ℯ + 151200⋅x ⋅ℯ + 1814400⋅x ⋅ℯ , True⎠

| In [6]: %timeit integrate\_hyperexponential(a, d, [Poly(1, x), Poly(t,
t)], [x, t], [exp])
|  10 loops, best of 3: 42 ms per loop

| In [7]: integrate(rd, x)
|  Out[7]:
|  x 10 x x 3 x 5 x 7 x 9 x 8 x 6 x 4 x 2 x
|  3628800⋅ℯ + x ⋅ℯ - 3628800⋅x⋅ℯ - 604800⋅x ⋅ℯ - 30240⋅x ⋅ℯ - 720⋅x ⋅ℯ
- 10⋅x ⋅ℯ + 90⋅x ⋅ℯ + 5040⋅x ⋅ℯ + 151200⋅x ⋅ℯ + 1814400⋅x ⋅ℯ

| In [8]: %timeit integrate(rd, x)
|  1 loops, best of 3: 2.78 s per loop
|  [/code]

There is one thing I should mention. I haven't implemented all the cases
in ``rischDE()``, which is the subproblem for exponential functions
(more on this in a future "The Risch Algorithm" post). So some integrals
will fail with a ``NotImplementedError``, indicating that there is a
function that I still need to implement to solve the integral:

| [code language="py"]
|  In [1]: from sympy.integrals.risch import \*

| In [2]: var('t1, t')
|  Out[2]: (t₁, t)

In [3]: rd = (exp(x) - x\*exp(2\*x)\*tan(x))/tan(x)

In [4]: a, d = map(lambda i: Poly(i, t), rd.subs(exp(x), t).subs(tan(x),
t1).as\_numer\_denom())

| In [5]: a
|  Out[5]: Poly(-t1\*x\*t\*\*2 + t, t, domain='ZZ[x,t1]')

| In [6]: d
|  Out[6]: Poly(t1, t, domain='ZZ[t1]')

| In [7]: integrate\_hyperexponential(a, d, [Poly(1, x), Poly(1 +
t1\*\*2, t1), Poly(t, t)], [x, t1, t], [exp, tan])
| 
---------------------------------------------------------------------------
|  ...
|  NotImplementedError: The ability to solve the parametric logarithmic
derivative problem is required to solve this RDE
|  [/code]

So feel free to give this a try and let me know what you think. You will
have to do the preparsing as I have done above, which means that you
also have to be careful that any extension that you make is not the
derivative or logarithmic derivative of an element of the field you have
already built up. You also cannot use algebraic functions, as I
mentioned before, including things like $latex e^\\frac{\\log{x}}{2}$
(functions like these are called the logarithmic derivatives of
k(t)-radicals, which I will also discuss in a future "The Risch
Algorithm" post). If you just use simple extensions like
``t1 = tan(x);t=exp(x)`` like I have above, you won't need to worry
about this. Each derivative Poly should be in the variable that it is
the derivative of (e.g., start with ``Poly(1, x)``, then add
``Poly(1 + t1**2, t1)``, ``Poly(t2*(1 + t1**2), t2)``, etc.). Everything
else should be a Poly in ``t``, the last element of the extension. And
in cause you didn't get it, the last extension must be an exponential
function.

Also, I didn't have to do it in any of the above examples, but the first
and second arguments to ``integrate_hyperexponential()`` *must* be
canceled (``a, d = a.cancel(d, include=True)`` will do this for you), or
you will get a wrong result! I spent a good day of debugging until I
figured this out. The existence of other bugs didn't help.

.. _lengthy blog post on the Risch Algorithm: http://asmeurersympy.wordpress.com/2010/06/30/the-risch-algorithm-part-1/
.. _integration2: http://github.com/asmeurer/sympy/tree/integration2
