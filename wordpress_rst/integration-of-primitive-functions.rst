Integration of primitive functions
##################################
:date: 2010-07-31 06:44
:author: asmeurer
:category: Uncategorized
:slug: integration-of-primitive-functions

**Integration of Primitive Functions**

So this past week, I had another break through in my project. The `first
break through`_, as you may recall, was the completion of the
``integrate_hyperexponential()`` function, which allowed for the
integration in hyperexponential extensions, including proving the
nonexistence of elementary integrals. Now I have worked my way up to
this level on the other major half of the integration algorithm
(actually, major third; more on that later): integration of primitive
elements.

This time, I can refer you to my `previous blog post`_ for definitions.
The chief thing here is that there is now a function in my
``integration3`` branch called ``integrate_primitive()``, and it is used
primarily for integrating functions with logarithms.

So, how about some examples? The first one comes from `Algorithms for
computer algebra By Keith O. Geddes, Stephen R. Czapor, George Labahn`_
(example 12.8). I like it because it contains both exponentials and
logarithms, in a way that they do not depend on each other, so it can be
integrated with either ``integrate_primitive()`` or
``integrate_hyperexponential()``. In either case, the polynomial part is
$latex \\frac{x}{x + 1}$, so recursively calling the other function is
not required. (for those of you who have been following my
``integration3`` branch, you may notice that this is blatantly taken
from the commit history).

| **Hover over the code and click on the left-most, "view source" icon
(a paper icon with ``< >`` over it) to view without breaks. Opens in a
new window.**
|  [code language="py"]
|  In [1]: from sympy.integrals.risch import integrate\_primitive,
|  integrate\_hyperexponential

| In [2]: f = (x\*(x + 1)\*((x\*\*2\*exp(2\*x\*\*2) - log(x +
1)\*\*2)\*\*2 +
|  2\*x\*exp(3\*x\*\*2)\*(x - (2\*x\*\*3 + 2\*x\*\*2 + x + 1)\*log(x +
1))))/((x +
|  1)\*log(x + 1)\*\*2 - (x\*\*3 + x\*\*2)\*exp(2\*x\*\*2))\*\*2

| In [3]: f
|  Out[3]:
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

| In [4]: var('t0, t1')
|  Out[4]: (t₀, t₁)

| In [5]: a, d = map(lambda i: Poly(i, t1), f.subs(exp(x\*\*2),
|  t0).subs(log(x + 1), t1).as\_numer\_denom())

| In [6]: a
|  Out[6]:
|  Poly((x + x\*\*2)\*t1\*\*4 + (-2\*t0\*\*2\*x\*\*3 -
2\*t0\*\*2\*x\*\*4)\*t1\*\*2 +
|  (-2\*t0\*\*3\*x\*\*2 - 4\*t0\*\*3\*x\*\*3 - 6\*t0\*\*3\*x\*\*4 -
8\*t0\*\*3\*x\*\*5 -
|  4\*t0\*\*3\*x\*\*6)\*t1 + 2\*t0\*\*3\*x\*\*3 + 2\*t0\*\*3\*x\*\*4 +
t0\* \*4\*x\*\*5 +
|  t0\*\*4\*x\*\*6, t1, domain='ZZ[x,t0]')

| In [7]: d
|  Out[7]: Poly((1 + 2\*x + x\*\*2)\*t1\*\*4 + (-2\*t0\*\*2\*x\*\*2 -
4\*t0\*\*2\*x\*\*3 -
|  2\*t0\*\*2\*x\*\*4)\*t1\*\*2 + t0\*\*4\*x\*\*4 + 2\*t0\*\*4\*x\*\*5 +
t0\*\*4\*x\*\*6, t1,
|  domain='ZZ[x,t0]')

In [8]: D = [Poly(1, x), Poly(2\*x\*t0, t0), Poly(1/(x + 1), t1)]

| In [9]: r = integrate\_primitive(a, d, D, [x, t0, t1], [lambda x:
log(x +
|  1), lambda x: exp(x\*\*2)])

| In [10]: r
|  Out[10]:
|  ⎛ ⎛ ⎛ 2⎞⎞ ⎛ ⎛ 2⎞⎞ ⎛ 2⎞ ⎞
|  ⎜ ⎜ ⎝x ⎠⎟ ⎜ ⎝x ⎠⎟ ⎝x ⎠ ⌠ ⎟
|  ⎜log⎝log(1 + x) + x⋅ℯ ⎠ log⎝log(1 + x) - x⋅ℯ ⎠ x⋅ℯ ⋅log(1 + x) ⎮ x ⎟
|  ⎜───────────────────────── - ───────────────────────── -
────────────────────── + ⎮ ───── dx, True⎟
|  ⎜ 2 2 2 ⎮ 1 + x ⎟
|  ⎜ 2 2 2⋅x ⌡ ⎟
|  ⎝ log (1 + x) - x ⋅ℯ ⎠
|  [/code]
|  An explanation: ``f`` is the function we are integrating. Preparsing
is not implemented yet, so we have to do it manually in ``[5]``. ``[8]``
is the list of derivations of the monomials we are working with,
``[x, t0, t1]``, which represent $latex x$, $latex e^{x^2}$, and $latex
\\log{(x + 1)}$, respectively. Because the outermost monomial is a
logarithm (primitive), we call ``integrate_primitive()`` on it. The last
argument of the function is the back substitution list, in reverse order
because that is the order we have to back substitute in. We can see the
result contains an unevaluated Integral. This is because the recursive
calls to integrate over the smaller extensions have not yet been
implemented. In the final version, ``integrate()`` will automatically
call ``ratint()`` in this case on it to give the complete answer. The
second argument of the result, True, indicates that the integral was
elementary and that this is the complete integral.

Because the extensions did not depend on each other, we could have also
integrated in $latex \\mathbb{Q}(x, \\log{(x + 1)}, e^{x^2})$ instead of
$latex \\mathbb{Q}(x, e^{x^2}, \\log{(x + 1)})$:

| [code language="py"]
|  In [11]: a1, d1 = map(lambda i: Poly(i, t0), f.subs(exp(x\*\*2),
t0).subs(log(x + 1), t1).as\_numer\_denom())

In [12]: D1 = [Poly(1, x), Poly(1/(x + 1), t1), Poly(2\*x\*t0, t0)]

In [13]: r1 = integrate\_hyperexponential(a1, d1, D1, [x, t1, t0],
[lambda x: exp(x\*\*2), lambda x: log(x + 1)])

| In [14]: r1
|  Out[14]:
|  ⎛ ⎛ ⎛ 2⎞⎞ ⎛ ⎛ 2⎞⎞ ⎞
|  ⎜ ⎜log(1 + x) ⎝x ⎠⎟ ⎜ log(1 + x) ⎝x ⎠⎟ ⎛ 2⎞ ⎟
|  ⎜log⎜────────── + ℯ ⎟ log⎜- ────────── + ℯ ⎟ 2 ⎝x ⎠ ⌠ ⎟
|  ⎜ ⎝ x ⎠ ⎝ x ⎠ x ⋅ℯ ⋅log(1 + x) ⎮ x ⎟
|  ⎜─────────────────────── - ───────────────────────── +
────────────────────────── + ⎮ ───── dx, True⎟
|  ⎜ 2 2 2 ⎮ 1 + x ⎟
|  ⎜ 2 3 2⋅x ⌡ ⎟
|  ⎝ - x⋅log (1 + x) + x ⋅ℯ ⎠
|  [/code]
|  We can verify by taking the derivative that the results in each case
are antiderivatives of the original function, ``f``, even though they
appear different.

| [code language="py"]
|  In [15]: cancel(r[0].diff(x) - f)
|  Out[15]: 0

| In [16]: cancel(r1[0].diff(x) - f)
|  Out[16]: 0
|  [/code]

We can see in each case, the remaining unevaluated ``Integral`` was in
$latex \\mathbb{Q}(x)$ only, meaning that the recursive call to
``integrate_hyperexponential()`` or ``integrate_primitive()``,
respectively, would not have been necessary. Finally, we can see that
choosing the correct extension to integrate over can make a difference,
time wise:

| [code language="py"]
|  In [17]: %timeit integrate\_primitive(a, d, D, [x, t0, t1], [lambda
x: log(x + 1), lambda x: exp(x\*\*2)])
|  1 loops, best of 3: 1.91 s per loop

| In [18]: %timeit integrate\_hyperexponential(a1, d1, D1, [x, t1, t0],
[lambda x: exp(x\*\*2), lambda x: log(x + 1)])
|  1 loops, best of 3: 2.63 s per loop
|  [/code]

Just as with the exponential case, the function can prove the integrals
are non-elementary. This is the so-called `logarithmic integral`_:

| [code language="py"]
|  In [19]: f1 = 1/log(x)

In [20]: a, d = map(lambda i: Poly(i, t1), f1.subs(log(x),
t1).as\_numer\_denom())

| In [21]: a
|  Out[21]: Poly(1, t1, domain='ZZ')

| In [22]: d
|  Out[22]: Poly(t1, t1, domain='ZZ')

| In [23]: integrate\_primitive(a, d, [Poly(1, x), Poly(1/x, t1)], [x,
t1], [log])
|  Out[23]: (0, False)
|  [/code]

The second argument, ``False``, indicates that the integral was
non-elementary. Namely, the function has proven that the function $latex
f - D(0) = \\frac{1}{\\log{(x)}}$ does not have an elementary
anti-derivative over $latex \\mathbb{Q}(x, \\log{(x)})$ (see the
`previous post`_ for more information).

Finally, be aware that, just as with ``integrate_hyperexponential()``
many integrals will raise ``NotImplementedError``, because the
subroutines necessary to solve them have not yet been finished.

| [code language="py"]
|  In [25]: f = log(log(x))\*\*2

| In [26]: f.diff(x)
|  Out[26]:
|  2⋅log(log(x))
|  ─────────────
|  x⋅log(x)

| In [27]: a, d = map(lambda i: Poly(i, t1),
|  cancel(f.diff(x)).subs(log(x), t0).subs(log(t0),
t1).as\_numer\_denom())

| In [28]: a
|  Out[28]: Poly(2\*t1, t1, domain='ZZ')

| In [29]: d
|  Out[29]: Poly(t0\*x, t1, domain='ZZ[x,t0]')

In [30]: D = [Poly(1, x), Poly(1/x, t0), Poly(1/(x\*t0), t1)]

| In [31]: integrate\_primitive(a, d, D, [x, t0, t1], [lambda x:
log(log(x)), log])
| 
---------------------------------------------------------------------------
|  NotImplementedError: Remaining cases for Poly RDE not yet
implemented.
|  [/code]

Now one thing that I want to add from the above examples taken from the
commit message is that logarithms are not the only function that are
primitive. The Li function (the logarithmic integral, as above),
considered as an elementary extension of $latex \\mathbb{Q}(x,
\\log{(x)})$ is also primitive. But even among the commonly defined
elementary functions, there is one other, acrtangents.

| [code language="py"]
|  In [32]: diff(atan(x)\*\*2, x)
|  Out[32]:
|  2⋅atan(x)
|  ─────────
|  2
|  1 + x

In [33]: integrate\_primitive(Poly(2\*t, t), Poly(1 + x\*\*2, t),
[Poly(1, x), Poly(1/(1 + x\*\*2), t)], [x, t], [atan])

| Out[33]:
|  ⎛ 2 ⎞
|  ⎝atan (x), True⎠

In [34]: integrate\_primitive(Poly(t, t), Poly(x, t), [Poly(1, x),
Poly(1/(1 + x\*\*2), t)], [x, t], [atan])

| Out[34]:
|  ⎛⌠ ⎞
|  ⎜⎮ atan(x) ⎟
|  ⎜⎮ ─────── dx, False⎟
|  ⎜⎮ x ⎟
|  ⎝⌡ ⎠
|  [/code]

Due to a bug in the code right now, the final version returns the
non-elementary integral in the final result. Suffice it to say that it
has proven that $latex \\int {\\frac{\\arctan{(x)}}{x} dx}$ is
non-elementary. As far as I know, this isn't any special function.
Actually, it's just a random function containing arctan that looked
non-elementary to me that I plugged in and found out that I was correct.
It's very similar in form to the `exponential integral`_ (Ei) or the
`Sine/Cosine Integral`_ (Si/Ci), which is how I guessed that it would be
non-elementary. Maybe it should be called ATi().

**Status Update**

So it has come to my attention that the suggested "pencils down" date is
one week from Monday, and the hard "pencils down" date is two weeks from
Monday (see the `Google Summer of Code Timeline`_). Now, no matter how
fast I work, my work cannot be pushed in until Mateusz's latest polys
branch gets pushed in, because my work is based on top of it. I plan on
continuing work on the integration algorithm beyond the summer until I
finish the transcendental part of the algorithm, and even after that, I
want to look into implementing other integration related things, like
definite integration using `Meijer G-functions,`_ and the algebraic part
of the algorithm. But for now, these are the things that I need to do
for the transcendental part, which is this summer's work:

*1. Implement the preparsing algorithms.* This part is two-fold. First,
I need to implement algorithms based on the Risch Structure Theorems,
which allow me to determine if an extension is algebraic or not (if it
is algebraic, we cannot integrate it because only the transcendental
part is implemented). The other part will be the function that actually
goes through an expression and tries to build up a differential
extension from it so it can be integrated. This can be a tricky part.
For example, if we want to integrate $latex f = e^x + e^{\\frac{x}{2}}$,
we want to first choose $latex t\_1=e^{\\frac{x}{2}}$ so that $latex f =
t\_1^2 + t\_1$, because if we choose $latex t\_1=e^x$, then $latex
t\_2=e^{\\frac{x}{2}}=\\sqrt{t\_1}$ will be algebraic over $latex
\\mathbb{Q}(x, t\_1)$. This is one case where we might try adding an
algebraic extensions but where it can be avoided. The solution will have
to be to go through and find the common denominators of the
exponentials. I'm also considering that this might happen in more
advanced ways, so it could be necessary for the function to backtrack in
the extension tree to see if it can do it in an entirely transcendental
way. Fortunately, the Risch Structure Theorems give us a decision
procedure for determining if an extension can be written in terms of the
previous extensions (is algebraic over it), but this will still be a
very hard function to get right.

*2. Finish the remaining cases for ``integrate_hyperexponential()`` and
``integrate_primitive()``.* As you could see in this post, as well as in
the `previous one`_, there are many integrals that cannot yet be
integrated because the special cases for them have not been implemented
yet. Most of these actually rely on implementing the structure theorem
algorithms from **1**, and implementing them once that is finished will
not take long, because they will just be straight copying of the
pseudocode from Bronstein's book. But some of them, particularly ones
from the primitive case, are not spelt out so well in Bronstein's book,
and will require more thinking (and thus time) on my part. I should note
that the Structure Theorem algorithms are also this way.

*3. Implement the hypertangent case.* The ability to integrate in
tangent extensions is the other *third* I mentioned above. Since
tangents require more special casing, I plan on doing this only after I
have finished **1** and **2**. This is actually not much work, because
most of the algorithms for solving the particular subproblem for
tangents (called the *Coupled Risch Differential Equation*) are exactly
the same as those for solving the subproblem for hyperexponentials (the
*Risch Differential Equation*), which are already (mostly) implemented
in the hyperexponential part. There are only a few extra functions that
need to be written for it. Also, you will still be able to integrate
functions that contain tangents, such as $latex e^{\\tan{(x)}}$ (recall
`last time`_ that we showed that ``integrate_hyperexponential()`` can
prove that this does not have an elementary integral). It just won't be
able to integrate when the top-most extension is a tangent.

So here is what I plan on doing. Right now, I am going to focus my work
on **1**, since most of **2** can't be done until it is anyway. But more
importantly, I want to have a prototype user-level function for the
Risch Algorithm. The reason I want this is so that people can try it
out, without having to do the preparsing like I did above, but rather
they can just call ``risch_integrate(f, x)``, and it will return the
integral of ``f``, prove that it is non-elementary and reduce it into
the elementary and non-elementary parts, or explain why it cannot do it
(either because the function is not transcendental or because something
is not implemented yet). My chief desire for doing this is so that
people can try out my code and find the bugs in it for me. I have
already found many critical errors in the code (returns a wrong result),
and I want to iron these out before anything goes in. The best way to do
this will be to release a working user-level function and hope that
people try it out for me.

Also, even if **2** and **3** are not finished, if I have **1**, I can
integrate it with ``integrate()`` (no pun intended) and just have it
bail if it raises ``NotImplementedError`` I will need to come up with a
way to differentiate between this and the case where it returns an
unevaluated ``Integral`` because it has proven that an elementary
antiderivative does not exist. Any suggestions?

I plan on continuing work after the summer until I finish **1** through
**3**, though I won't pretend that my work won't slow down considerably
when I start classes in August. I also promise to finish the `Risch
Algorithm posts`_ that I promised.

And for what it's worth, I plan on working my ass off this next two
weeks.

.. _first break through: http://asmeurersympy.wordpress.com/2010/07/12/integration-of-exponential-functions/
.. _previous blog post: http://asmeurersympy.wordpress.com/2010/07/24/the-risch-algorithm-part-2-elementary-functions/
.. _Algorithms for computer algebra By Keith O. Geddes, Stephen R. Czapor, George Labahn: http://
.. _logarithmic integral: http://en.wikipedia.org/wiki/Logarithmic_integral
.. _previous post: http://asmeurersympy.wordpress.com/2010/07/12/integration-of-exponential-functions/
.. _exponential integral: http://en.wikipedia.org/wiki/Exponential_integral
.. _Sine/Cosine Integral: http://en.wikipedia.org/wiki/Sine_integral#Sine_integral
.. _Google Summer of Code Timeline: http://socghop.appspot.com/document/show/gsoc_program/google/gsoc2010/timeline
.. _Meijer G-functions,: http://en.wikipedia.org/wiki/Meijer-G
.. _previous one: http://asmeurersympy.wordpress.com/2010/07/12/integration-of-exponential-functions/
.. _last time: http://asmeurersympy.wordpress.com/2010/07/12/integration-of-exponential-functions/
.. _Risch Algorithm posts: http://asmeurersympy.wordpress.com/2010/07/12/integration-of-exponential-functions/
