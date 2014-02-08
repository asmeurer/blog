Nondeterminism
##############
:date: 2011-06-05 06:08
:author: asmeurer
:category: Uncategorized
:slug: nondeterminism

So from Saturday to Wednesday of this week, I was on vacation to the
Grand Canyon without my computer. Therefore, I did not do a whole lot
with respect to SymPy this week. The vacation was very fun, though. My
family and I hiked to the bottom of the Grand Canyon and stayed a day at
the bottom in a lodge at Phantom Ranch, then hiked back up. I would
highly recommend it to anyone who does not mind doing a little hiking.

Regarding what I did do, other than catching up on the email from when I
was gone, I did some more work finishing patches for the release. We are
now *very* close to having a release. All the remaining `blocking
issues`_ either have patches that need to be reviewed, or decisions that
need to be made.

I also did some work on the Risch Algorithm, though it wasn't very much.
One of my favorite ways to "do work" on the code is to stress test
``risch_integrate()`` and if I find a bug or find that it runs too slow,
see what needs to be done to fix it. This week, I discovered that
``risch_integrate()`` has a bit of nondeterminism built into it.
Actually, I already knew this, but I recently found an example that
demonstrates it very nicely. The problem is that when it builds the
extension to integrate the function, ``risch_integrate()`` uses
``.atoms()`` to get the parts of the expression (for example,
``expr.atoms(log)`` gets all the logarithms in ``expr``). But
``.atoms()`` returns a set (I believe this is for performance reasons,
though I'm not certain). So we get things like

| **Hover over the code and click on the left-most, "view source" icon
(a paper icon with ``< >`` over it) to view without breaks. Opens in a
new window.**
|  [code language="py"]
|  In [1]: a = Add(\*(log(x\*\*i) for i in range(10)))

| In [2]: a
|  Out[2]:
|  ⎛ 2⎞ ⎛ 3⎞ ⎛ 4⎞ ⎛ 5⎞ ⎛ 6⎞ ⎛ 7⎞ ⎛ 8⎞ ⎛ 9⎞
|  log(x) + log⎝x ⎠ + log⎝x ⎠ + log⎝x ⎠ + log⎝x ⎠ + log⎝x ⎠ + log⎝x ⎠ +
log⎝x ⎠ + log⎝x ⎠

In [3]: b = risch\_integrate(a, x)

| In [4]: b
|  Out[4]:
|  ⎛ 4⎞
|  45⋅x⋅log⎝x ⎠
|  -45⋅x + ────────────
|  4
|  [/code]

This is correct, since we have

| [code language="py"]
|  In [5]: expand(b.diff(x) - a)
|  Out[5]: 0
|  [/code]

(remember that $latex \\log{(x^n)}=n\\log{(x)}$). The integral can be
expressed in terms of any of the logarithms in the expression. It
happens to be expressed in terms of $latex \\log{(x^4)}$ because that
happened to be the first one that came out of ``a.atoms(log)`` during
iteration. This is problematic. First, it's not exactly what is
expected. The ideal solution would be if the answer was written in terms
of $latex \\log{(x)}$.

But it's actually worse than that. Like I mentioned, this is
nondeterministic. It depends on the order of iteration through a set,
which is not guaranteed to be in any particular order. Indeed, if I run
the following in 32-bit Python 2.7 and again in 64-bit Python 2.7), the
output is exactly the same except for ``i`` = 64 to ``i`` = 77.

| [code language="py"]
|  for i in range(100):
|  print risch\_integrate(Add(\*(log(x\*\*j) for j in range(i))), x)
|  [/code]

The actual output seems to follow a pattern, though it's had to discern
exactly what it is. The output for 32-bit is
https://gist.github.com/1008685 and the output for 64-bit is
https://gist.github.com/1008684 (sorry, I forgot to print ``i``; just
subtract 4 from the line number).

So this has gotten me thinking about how to reduce nondeterminism.
Clearly, I need to sort the result of ``.atoms()``, or else
``risch_integrate()`` might return a different (though equivalent)
result on different platforms. Actually, I've seen ``list(set)`` return
a different result in the *same* Python session. That means that you
could potentially get something like
``risch_integrate(expr, x) == risch_integrate(expr, x) => False``!

The problem is how to sort the atoms. We recently added a ``sort_key()``
function that can be passed as a key to ``sorted()``, which is
completely deterministic and platform independent. That would solve the
determinism problem, but actually, I think this requires more thought.
The order that the differential extension is built in can affect not
only the form of the resulting antiderivative (though it will always be
equivalent, up to a constant), but also the speed with which it is
computed. To take an example from `issue 2010`_, the issue about
``risch_integrate()`` (you may also `recognize`_ this example if you are
a regular reader of this blog), the ``handle_first`` keyword argument to
``risch_integrate()`` affects if it builds the extension tower looking
for logarithms first or exponentials first. Whichever comes last is what
is integrated first (the tower is integrated from the top to the
bottom). If the last extension was an exponential, then it uses the
exponential algorithm. If it was a logarithm, then it uses the logarithm
algorithm. These are completely different algorithms, and indeed the
results can appear in different forms (and sometimes, one will raise
NotImplementedError while the other will work because I have implemented
the exponential algorithm more completely than the logarithmic one). It
also affects the speed because the integrand might be of a different
"type" in the different extensions. In the example below, the answers
are different because it tries to make the argument of the logarithmic
part monic with respect to the exponential or the logarithm,
respectively. Also notice the speed difference. This can be exasperated
more for integrands of different forms than this one.

| [code language="py"]
|  In [1]: f = (x\*(x + 1)\*((x\*\*2\*exp(2\*x\*\*2) - log(x +
1)\*\*2)\*\*2 +
|  ...: 2\*x\*exp(3\*x\*\*2)\*(x - (2\*x\*\*3 + 2\*x\*\*2 + x +
1)\*log(x + 1))))/((x +
|  ...: 1)\*log(x + 1)\*\*2 - (x\*\*3 + x\*\*2)\*exp(2\*x\*\*2))\*\*2

| In [2]: f
|  Out[2]:
|  ⎛ 2 ⎞
|  ⎜⎛ 2⎞ 2⎟
|  ⎜⎜ 2 2 2⋅x ⎟ ⎛ ⎛ 2 3⎞ ⎞ 3⋅x ⎟
|  x⋅(1 + x)⋅⎝⎝- log (1 + x) + x ⋅ℯ ⎠ + 2⋅x⋅⎝x - ⎝1 + x + 2⋅x + 2⋅x
⎠⋅log(1 + x)⎠⋅ℯ ⎠
| 
──────────────────────────────────────────────────────────────────────────────────────────
|  2
|  ⎛ 2⎞
|  ⎜ 2 ⎛ 2 3⎞ 2⋅x ⎟
|  ⎝log (1 + x)⋅(1 + x) - ⎝x + x ⎠⋅ℯ ⎠

| In [3]: risch\_integrate(f, x, handle\_first='log')
|  Out[3]:
|  ⎛ ⎛ 2⎞⎞ ⎛ ⎛ 2⎞⎞
|  ⎜log(1 + x) ⎝x ⎠⎟ ⎜ log(1 + x) ⎝x ⎠⎟ ⎛ 2⎞
|  log⎜────────── + ℯ ⎟ log⎜- ────────── + ℯ ⎟ 2 ⎝x ⎠
|  ⎝ x ⎠ ⎝ x ⎠ x ⋅ℯ ⋅log(1 + x)
|  x + ─────────────────────── - log(1 + x) - ─────────────────────────
+ ──────────────────────────
|  2 2 2
|  2 3 2⋅x
|  - x⋅log (1 + x) + x ⋅ℯ

| In [4]: risch\_integrate(f, x, handle\_first='exp')
|  Out[4]:
|  ⎛ ⎛ 2⎞⎞ ⎛ ⎛ 2⎞⎞ ⎛ 2⎞
|  ⎜ ⎝x ⎠⎟ ⎜ ⎝x ⎠⎟ ⎝x ⎠
|  log⎝log(1 + x) + x⋅ℯ ⎠ log⎝log(1 + x) - x⋅ℯ ⎠ x⋅ℯ ⋅log(1 + x)
|  x + ───────────────────────── - log(1 + x) -
───────────────────────── - ──────────────────────
|  2 2 2
|  2 2 2⋅x
|  log (1 + x) - x ⋅ℯ

| In [5]: %timeit risch\_integrate(f, x, handle\_first='log')
|  1 loops, best of 3: 1.49 s per loop

| In [6]: %timeit risch\_integrate(f, x, handle\_first='exp')
|  1 loops, best of 3: 1.21 s per loop

| In [7]: cancel(risch\_integrate(f, x, handle\_first='log').diff(x) -
f)
|  Out[7]: 0

| In [8]: cancel(risch\_integrate(f, x, handle\_first='exp').diff(x) -
f)
|  Out[8]: 0
|  [/code]

So what I think I really need to do is to do some research on what order
of building the tower makes it the most efficient. Also,
``handle_first`` needs to be modified to be more dynamic than just
looking at exponentials or logarithms first, but also considering which
exponentials or logarithms to look at first, and the others might be
rewritten in terms of those (this needed to be done anyway to make it
work for three types of extensions: exponentials, logarithms, and
tangents).

There can also be more heuristics for this. Currently, there are
heuristics for exponentials to prefer rewriting $latex e^{2x}$ as $latex
\\left({e^{x}}\\right)^2$ instead of rewriting $latex e^{x}$ as $latex
\\sqrt{e^{2x}}$ (this is necessary not only for keeping things in terms
of the nicer looking gcds but also because ``risch_integrate()`` doesn't
know how to handle algebraic extensions like square roots). I didn't
realize it at the time, but the corollary heuristic for logarithms
should try to rewrite $latex \\log{(x^2)}$ in terms of $latex
\\log{(x)}$ and not the other way around. We can use the exact same gcd
algorithm (called ```integer_powers()```_ in ``risch.py``, and I now
realize that it should actually be called ``integer_multiples()``) as we
do for the exponential, only use the powers of the arguments instead of
coefficients. This might require some factorization to do completely
correctly, so it certainly requires some thought.

| **Update**
|  I discovered that there's an easier way to show the nondeterminism of
the above than running it on different architectures. You just have to
change the variable of integration:

| [code language="py"]
|  In [1]: a = Add(\*(log(x\*\*i) for i in range(10)))

| In [2]: risch\_integrate(a, x)
|  Out[2]:
|  ⎛ 4⎞
|  45⋅x⋅log⎝x ⎠
|  -45⋅x + ────────────
|  4

In [3]: b = Add(\*(log(y\*\*i) for i in range(10)))

| In [4]: risch\_integrate(b, y)
|  Out[4]: -45⋅y + 45⋅y⋅log(y)

In [5]: c = Add(\*(log(z\*\*i) for i in range(10)))

| In [6]: risch\_integrate(c, z)
|  Out[6]:
|  ⎛ 2⎞
|  45⋅z⋅log⎝z ⎠
|  -45⋅z + ────────────
|  2
|  [/code]

Clearly the code for this needs to be doing some canonicalization.

.. _blocking issues: http://code.google.com/p/sympy/issues/list?q=label:Milestone-Release0.7.0
.. _issue 2010: http://code.google.com/p/sympy/issues/detail?id=2010#c1
.. _recognize: http://asmeurersympy.wordpress.com/2010/08/05/prototype-risch_integrate-function-ready-for-testing/
.. _``integer_powers()``: https://github.com/asmeurer/sympy/blob/integration3/sympy/integrals/risch.py#L44
