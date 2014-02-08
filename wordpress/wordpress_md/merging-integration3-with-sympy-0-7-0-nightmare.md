Title: Merging integration3 with sympy-0.7.0 nightmare
Date: 2011-07-25 09:25
Author: asmeurer
Category: Uncategorized
Slug: merging-integration3-with-sympy-0-7-0-nightmare

For a long time, there have been several problems in my `integration3`
branch that were fixed in `master`. I decided that as an incentive to
finish the release, I would hold off on merging `master` into my branch
until the 0.7.0 release was finished. Well, here's a little timeline:

-   **June 28, 2011:** SymPy 0.7.0 final is released.
-   **June 29, 2011:** I type `git merge sympy-0.7.0` in my
    `integration3` branch.
-   **July 24, 2011 (today; technically July 25 because it's 2 AM):** I
    finish merging `sympy-0.7.0` into `integration3`.

That's right, it took me over three weeks---almost a month---to merge
`sympy-0.7.0` into `integration3` (granted, I worked on other things at
the same time, such as the [SciPy 2011 conference][], but to me, any
merge that takes longer than a day to complete is a problem). This is
because git decided that I needed to fix as a merge conflict just about
every single change in the release branch since the base of
`integration3`. The total was over 100 files. You can see the final
merge commit [here][SciPy 2011 conference].

So I started `git mergetool`, without which this whole ordeal would have
been 10 times worse. The mergetool, which on my computer is opendiff,
i.e., File Merge, gave the correct change by default in most cases, so I
actually did not have to manually fix the majority of the conflicts. But
I did have to go through and do a lot of them. I had to manually check
each difference in the polys, as I had made several changes there in the
course of working on `integration3`. In several occisaions, I had to
research a change using `git log -S` and fancy methods. And I noticed at
least two regressions in the polys, which I fixed.

mergetool was useless against `risch.py` and `test_risch.py`, because in
my branch I had renamed these to `heurisch.py` and `test_heurisch.py`.
Fortunately, these were not really modified much by me, so I could
basically just replace them with the `sympy-0.7.0` versions.

Once I finished merging I had to deal with test failures. This was
partly expected, as my branch has always had test failures due to my
hack disabling algebraic substitution in `exp`, which is required for
`risch_integrate()` to work, but there were also several unrelated ones.

Some of these were caused by wrong merge conflict resolutions by me. So
I went through `git diff sympy-0.7.0` change by change and made sure
that nothing was different that I didn't want to be. I would recommend
doing this for any big merge.

Then, I had to fix a few bugs that caused test failures. Several
semantics were changed in the release. I think the ones that I had to
change were the renaming of `has_any_symbols` to just `has`, the
renaming of `Poly.as_basic()` to `Poly.as_expr()`, and the swapping of
the meanings of `quo` and `exquo` in the polys. There were also some
doctest failures due to the change to lexicographic ordering in the
printer.

After all that, there were two regressions that caused test failures.
The first was the following:

Before:  
[code lang="py"]  
In [1]: Integral((exp(x\*log(x))\*log(x)), x).subs(exp(x\*log(x)),
x\*\*x)  
Out[1]:  
⌠  
⎮ x  
⎮ x ⋅log(x) dx  
⌡  
[/code]

After:  
[code lang="py"]  
In [1]: Integral((exp(x\*log(x))\*log(x)), x).subs(exp(x\*log(x)),
x\*\*x)  
Out[1]:  
⌠  
⎮ x⋅log(x)  
⎮ ℯ ⋅log(x) dx  
⌡  
[/code]

This substitution is necessary because the Risch algorithm requires
expressions like \$latex x\^x\$ to be rewritten as \$latex
e\^{x\\log(x)}\$ before it can integrate them, but I try to convert them
back after integrating so that the user gets the same thing in the
result that he entered. I created [issue 2571][] for this.

The second was that I had several places in my docstrings with things
like

> Given a derivation D on k[t] and f, g in k(t) with f weakly normalized
> with respect to t, either raise NonElementaryIntegralException, in
> which case the equation Dy + f\*y == g has no solution in k(t), or the
> quadruplet (a, b, c, h) such that a, h in k[t], b, c in k, and for any
> solution y in k(t) of Dy + f\*y == g, q = y\*h in k satisfies a\*Dq +
> b\*q == c.

The problem here is the "raise NonElementaryIntegralException," part.
The code quality checker things that this is an old style exception
(like `raise Exception, message`), due to a poorly formed regular
expression. I fixed this in a [pull request][].

The good news is that now a lot of stuff works that didn't before
because of fixes that were required that only existed in `master`. For
example, the following did not work before, but now does due to
improvements to `RootSum`:

[code lang="py"]

In [1]: risch\_integrate(1/(exp(5\*x) + exp(x) + 1), x)  
Out[1]:  
⎛ 2  
x + RootSum⎝21⋅z + 6⋅z + 1, Lambda(\_i, \_i\*log(-3381\*\_i\*\*4/4 -
3381\*\_i\*\*3/4

⎞ ⎛ 3 2  
- 625\*\_i\*\*2/2 - 125\*\_i/2 + exp(x) - 5))⎠ + RootSum⎝161⋅z + 115⋅z
+ 19⋅z +

1, Lambda(\_i, \_i\*log(-3381\*\_i\*\*4/4 - 3381\*\_i\*\*3/4 -
625\*\_i\*\*2/2 - 125\*\_i/2 +

⎞  
exp(x) - 5))⎠

In [2]: cancel(risch\_integrate(1/(exp(5\*x) + exp(x) + 1), x).diff(x))  
Out[2]:  
1  
─────────────  
5⋅x x  
ℯ + ℯ + 1  
[/code]

The general definition of the logarithmic part of an integral is a sum
over the roots of a polynomial, which must be expressed as a `RootSum`
in the general case. Previously, `RootSum.diff` did not work, but thanks
to Mateusz, an algorithm for computing exactly the RootSum where the
Lambda expression is a rational function was implemented (see [this
bit][] from our SciPy tutorial for an idea on how this works), so now
the Risch Algorithm can work with RootSum objects just as well with as
an ordinary sum of logarithms.

Also, there was a bug in the square free algorithm in my branch that was
fixed in `master` that was causing wrong results (I don't remember the
expression that produced them right now), and also there was a fix by me
in `master` to make `is_rational_function()` faster, as it was
significantly slowing down the calculation of some integrals (for
example, `risch_integrate(Add(*(exp(i*x) for i in range(1000))))`, which
is still slow to calculate, but now it's because of other things).

**About big branches**

So this merge, along with the poly12 fiasco (which by the way, I think
part of the reason git made me do all these merge conflict resolutions
was because `polys12` was rebased from the `polys11` I had merged into
integration3), has shown me very clearly that it is very bad to go off
with your own branch and do a lot of work and wait a long time before
merging it back into the main repo.

This is what was done with `polys12`. Mateusz had a lot of new
polynomials code that he developed in one big branch, and when it
finally came to merging it back in, it was a mess. This was for several
reasons, which I do not want to discuss too much here, but it became
clear to everyone I think that doing this was bad, and that it would
have been better to have submitted many changes as pull requests as they
were made than keeping them all together in one big branch for a long
time.

This model also affected my work, as I had to work off of latest the
polys branch, not `master`, as my work relied heavily on the latest and
greatest in the polys.

Well, with this merge of the main repo into my branch, I see that my
branch is starting to become the same way. I originally thought that I
should finish the Risch algorithm before submitting it to be merged into
`master`. I know know that this is the wrong approach. Development in
`master` is too fast to keep code away from it for too long. The
divergence makes it more and more difficult to merge back with every
time. Furthermore, there are regressions that were never noticed to be
regressions because the code that would have shown them existed only in
my branch. Now I have to fix these, whereas if the code were in
`master`, the regression would have never happened in the first place,
because the author would have seen it immediately from the test
failures.

I also thought that I should wait to merge because there were so many
bugs in my code. But I see now that this is also wrong. Merging with
`master` will help me find these bugs, as people will actually use my
code. Sure, I've asked people to try out `risch_integrate()`, and some
people have (and I thank you), but having it in the default
`integrate()` in `master` will result in finding more bugs in the code
than I ever would alone, which is basically the way it is right now with
the code living only in my own branch.

I would prepare my code for merging with `master` today, if it weren't
for this `exp.subs` hack, which causes test failures and is technically
a regression, but is required for the preparsing code to the Risch
algorithm to work. This is why I [wrote to the list][] two weeks ago
asking for advice on how to structure the substitution code so that we
can nicely have various kinds of substitutions (e.g., exact like I need
and algebraic like currently exists in `exp`) living together without
cluttering up the code.

Therefore, I am going to focus my energies on fixing this subs problem
so I can get my code merged with `master`. Then, when this is done, I
will continue my work on implementing the remaining cases of the Risch
algorithm.

So let this tale be a warning to people working on a lot of code in a
big branch. This especially applies to our GSoC students, as it's
extremely easy to let your code accumulate when you're a GSoC student
(technically this branch of mine is a GSoC branch). I see that some of
our students are doing a better job of this than others. To those who
have your code all in one big branch that hasn't been merged, I
recommend you ready your branch for merge now. And in the future, try to
break your code up into small but still meaningful chunks and submit
those as pull requests. With git, it's easy to base the code you are
currently working on on code that hasn't been merged yet, while still
keeping things in small chunks for the pull requests.

On the other hand, git will only take you so far if you keep everything
in a big branch, because there are going to be changes in `master` that
will affect your work, no matter how isolated you think it is, and these
are the sorts of things that it is impossible for git to fix for you.
But if your code is in `master`, it will be supported by everyone, and
any major change that affects it will have to fix it. For example, if
someone changes a printer and the doctests change, then he will have to
change your doctest too if it's in `master`, but if it's in your branch,
then you will have to fix it when you next merge/rebase with/against
`master`.

  [SciPy 2011 conference]: https://github.com/asmeurer/sympy/commit/52657848516ce7f4f7119b921d6b8d64131b58d3
  [issue 2571]: http://code.google.com/p/sympy/issues/detail?id=2571
  [pull request]: https://github.com/sympy/sympy/pull/511
  [this bit]: http://mattpap.github.com/scipy-2011-tutorial/html/mathematics.html#summing-roots-of-polynomials
  [wrote to the list]: http://groups.google.com/group/sympy/browse_thread/thread/4a19d0f39f51fda6#
