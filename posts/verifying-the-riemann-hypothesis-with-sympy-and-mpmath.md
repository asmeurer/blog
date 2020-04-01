I've recently spent some of my free time watching various YouTube videos about
the [Riemann Hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis).
I've collected the videos I've watched into [YouTube
playlist](https://www.youtube.com/playlist?list=PLrFrByaoJbcqKjzgJvLs2-spSmzP7jolT).
The playlist is sorted with the most mathematically approachable videos first,
so even if you haven't studied complex analysis before, you can watch the
first few. If you have studied complex analysis, all the videos will be within
your reach (none of them are highly technical with proofs). Each video
contains parts that aren't in any of the other videos, so you will get
something out of watching each of them.

The [last video in the
playlist](https://www.youtube.com/watch?v=lyf9W2PWm40&list=PLrFrByaoJbcqKjzgJvLs2-spSmzP7jolT&index=8)
is a lecture by Keith Conrad. In it, he mentioned a method by which one could
go about verifying the Riemann Hypothesis with a computer. I wanted to see if
I could do this with SymPy and mpmath. It turns out you can.

# Background Mathematics

## Euler's Product Formula

Before we get to the computations, let's go over some mathematical background.
As you may know, the Riemann Hypothesis is one of the 7 [Millennium Prize
Problems](https://en.wikipedia.org/wiki/Millennium_Prize_Problems) outlined by
the Clay Mathematics Institute in 2000. The problems have gained some fame
because each problem comes with a $1,000,000 prize if solved. One problem, the
[Poincaré conjecture](https://en.wikipedia.org/wiki/Poincar%C3%A9_conjecture),
has already been solved (Grigori Perelman who solved it turned down the 1
million dollar prize). The remainder remain unsolved.

The Riemann Hypothesis is one of the most famous of these. The reason for this
is that the problem is central many open questions in number theory. There are
hundreds of theorems which are only known to be true contingent on the Riemann
Hypothesis, meaning that if the Riemann Hypothesis were proven, immediately
hundreds of theorems would be proven as well. Also, unlike some other
Millennium Prize problems like P=NP, the Riemann Hypothesis is almost
universally believed to be true by mathematicians.

To understand the statement of the hypothesis, we must first define the zeta
function. Let

$$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$$

(that squiggle
$\zeta$ is the lowercase Greek letter zeta). This expression makes sense if
$s$ is an integer greater than 1, $s=2, 3, \ldots$, since we know from simple
arguments from calculus that the summation converges in those cases (it isn't
important for us what those values are, only that the summation converges).
The story begins with Euler, who in 1740 considered the following infinite
product: $$\prod_{p\ \mathrm{prime}}\frac{1}{1 - \frac{1}{p^s}}.$$ The product
ranges over all prime numbers, i.e., it is $$\left(\frac{1}{1 -
\frac{1}{2^s}}\right)\cdot\left(\frac{1}{1 -
\frac{1}{3^s}}\right)\cdot\left(\frac{1}{1 - \frac{1}{5^s}}\right)\cdots.$$ The
fraction $\frac{1}{1 - \frac{1}{p}}$ may seem odd at first, but consider the
famous geometric series formula, $$\sum_{k=0}^\infty r^k = \frac{1}{1 - r},$$
which is true for $|r| < 1$. Our fraction is exactly of this form, with $r =
\frac{1}{p^s}$. So substituting, we have

$$\prod_{p\,\mathrm{prime}}\frac{1}{1 - \frac{1}{p^s}} =
\prod_{p\,\mathrm{prime}}\sum_{k=0}^\infty \left(\frac{1}{p^s}\right)^k =
\prod_{p\,\mathrm{prime}}\sum_{k=0}^\infty \left(\frac{1}{p^k}\right)^s.$$

If we take a closer look at what this is, it is

$$\left(\frac{1}{p_1^s} + \frac{1}{p_1^{2s}} + \frac{1}{p_1^{3s}} +
\cdots\right)\cdot\left(\frac{1}{p_2^s} + \frac{1}{p_2^{2s}} +
\frac{1}{p_2^{3s}} + \cdots\right)\cdots.$$

Now think about how to expand finite products of finite sums, for instance,
$$(x_1 + x_2 + x_3)(y_1 + y_2 + y_3)(z_1 + z_2 + z_3).$$ To expand the above,
you would take a sum of every combination where you pick one $x$ term, one $y$
term, and one $z$ term, giving

$$x_1y_1z_1 + x_1y_1z_2 + \cdots + x_2y_1z_3 + \cdots + x_3y_2z_1 + \cdots x_3y_3z_3.$$

So to expand the infinite product, we do the same thing. We take
every combination of picking every combination of $1/p_i^{ks}$, with
one $k$ for each $i$. If we pick infinitely many non-$1$ powers, the product
will be zero, so we only need to consider terms where there are finitely many
primes. The resulting sum will be something like

$$\frac{1}{1^s} + \frac{1}{p_1^s} + \frac{1}{p_2^s} + \frac{1}{p_1^{2s}} +
\frac{1}{p_3^s} + \frac{1}{\left(p_1p_2\right)^s} + \cdots,$$

where each prime power combination is picked exactly once. However, we know by
the [Fundamental Theorem of
Arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic)
that when you take all combinations of products primes that you get each
positive integer exactly once. So the above sum is just

$$\frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + \cdots,$$ which is just
$\zeta(s)$ as we defined it above.

Euler's product formula gives us our first clue as to why the zeta function can give
us insights into prime numbers.

## Analytic Continuation

In 1859, Bernhard Riemann wrote a [short 9 page paper on number theory and the
zeta
function](https://en.wikipedia.org/wiki/On_the_Number_of_Primes_Less_Than_a_Given_Magnitude).
It was the only paper Riemann ever wrote on the subject of number theory, but
it is undoubtedly one of the most important papers every written on the
subject.

In the paper, Riemann considered the zeta function summation

$$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$$

the summation makes sense not just for integers $s = 2, 3, \ldots$, but for
any real number $s > 1$ (if $s = 1$, the summation is the [harmonic
series](https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)), which
famously diverges). In fact, it is not hard to see that for complex $s$, the
summation makes sense so long as $\mathrm{Re}(s) > 1$ (for more about this,
and the basic ideas of analytic continuation, I recommend [3Blue1Brown's
video](https://www.youtube.com/watch?v=sD0NjbwqlYw&list=PLrFrByaoJbcqKjzgJvLs2-spSmzP7jolT&index=3)
from my YouTube playlist).

Riemann wanted to extend this function to the entire complex plane, not just
$\mathrm{Re}(s) > 1$. The process of doing this is called [analytic
continuation](https://en.wikipedia.org/wiki/Analytic_continuation). The theory
of complex analysis tells us that if we can find an extension of $\zeta(s)$ to
the whole complex plan that remains differentiable, then that extension is
unique, and we can reasonably say that that *is* the definition of the
function everywhere.

Riemann used the following approach. Consider what we might call the
"completed zeta function"

$$Z(s) = \pi^{-\frac{s}{2}}\Gamma\left(\frac{s}{2}\right)\zeta(s).$$

Using Fourier analysis, Riemann gave a formula for $Z(s)$ that is defined
everywhere, allowing us to use it to define $\zeta(s)$ to the left of 1. From
the formula for $Z(s)$ one can also see

1. $Z(s)$ is defined everywhere in the complex plane, except for simple poles at 0
   and 1.

2. $Z(s) = Z(1 - s).$ This means if we have a value for $s$ that is right of
   the line $\mathrm{Re}(z) = \frac{1}{2},$ we can get a value to the left of
   it by reflecting it over the real-axis and the line at $\frac{1}{2}$ (to
   see this, note that if we connect a line between $s$ and $1 - s$, the
   midpoint will be $1/2$, which should in fact be the case since $1/2$ is the
   average of $s$ and $1 - s$).

<img src="../../s-and-1-s.svg" width="608">

(created with [Geogebra](https://www.geogebra.org/graphing/c9rzy9hj))

## Zeros

Looking at $Z(s)$, there are three parts. $\pi^{-\frac{s}{2}}$ is the easiest:
it has no zeros and no poles. The second part is the [gamma
function](https://en.wikipedia.org/wiki/Gamma_function). $\Gamma(z)$ has no
zeros and has simple poles at nonpositive integers $z=0, -1, -2, \ldots$.

So taking this, along with the fact that $Z(s)$ is entire except for simple
poles at 0 and 1 we get from $$\zeta(s) =
\frac{Z(s)}{\pi^{-\frac{s}{2}}\Gamma\left(\frac{s}{2}\right)}$$

1. $Z(s)$ has a pole at 1, which means that $\zeta(s)$ does as well. This is not
   surprising, since we already know the summation formula from above diverges
   as $s$ approaches 1.
2. $Z(s)$ has a pole at 0. Since $\Gamma\left(\frac{s}{2}\right)$ also has a
   pole at 0, zeta must have neither a zero nor a pole at 0 (in fact,
   $\zeta(0) = -1/2$).
3. Since $\Gamma\left(\frac{s}{2}\right)$ has no zeros, there are no further
   poles of $\zeta(s)$. This $\zeta(s)$ is entire everywhere except for a
   simple pole at $s=1$.
4. $\Gamma\left(\frac{s}{2}\right)$ has poles at the remaining negative even
   integers. Since $Z(s)$ has no poles there, these must correspond to zeros
   of $\zeta(s)$. These are the so-called "trivial" zeros of the zeta
   function, at $s=-2, -4, -6, \ldots$. The term "trivial" here is a relative one.
   They are trivial to see from the above formula, whereas other zeros of zeta
   are much harder to see.
5. $\zeta(s) \neq 0$ if $\mathrm{Re}(s) > 1$. One way to see this is from the
   Euler product formula. Since each term in the product is not zero, the
   function itself cannot be zero (this is a bit hand-wavy, but it can be made
   rigorous). If we reflect $\mathrm{Re}(s)$ over the line at $\frac{1}{2}$
   using $1 - s$, using the above formula with $Z(s)$, we see that $\zeta(s)$
   cannot be zero for $\mathrm{Re}(s) < 0$ as well, with the exception of the
   aforementioned trivial zeros at $s=-2, -4, -6, \ldots$.

Thus, any non-trivial zeros of $\zeta(s)$ must have real part between 0 and 1.
This is called the "critical strip." Riemann hypothesized that in fact all the
zeros are not only between 0 and 1, but on the line dividing the strip at real
part equal to $1/2$. This line is called the "critical line."

## Computational Verification

Whenever you have a mathematical hypothesis, it is good to check if it is true
numerically. If we verified that all the zeros in the critical strip from,
say, $\mathrm{Im}(s) = 0$ to $\mathrm{Im}(s) = N$ are in fact on the critical
line for some large $N$, then it would give evidence that the Riemann
Hypothesis is true. This would not constitute a proof.
[Hardy](https://en.wikipedia.org/wiki/G._H._Hardy) showed in 1914 that
$\zeta(s)$ has infinitely many zeros on the critical strip, so only finding
finitely many of them would not suffice as a proof. (Although if we were to
find a counter-example, a zero *not* on the critical line, that WOULD
constitute a proof that the Hypothesis is false. However, there are strong
reasons to believe that the hypothesis is not false, so this would be unlikely
to happen.)

How would we verify that the zeros are all on the line $1/2$. We can find
zeros of $\zeta(s)$ numerically, but how would we know if the real part is
really exactly 0.5 and not 0.500000000000000000000000000000000001. And more
importantly, just because we find some zeros, it doesn't mean that we have all
of them. Maybe we can find a bunch of zeros on the critical line, but how
would we be sure that there aren't other zeros lurking around elsewhere on the
critical strip?

We want to find rigorous answers to two questions

1. How can we count the number of zeros between $\mathrm{Im}(s) = 0$ and
$\mathrm{Im}(s) = N$ of $Z(s)$?

2. How can we verify that all those zeros lie on the critical line, that is,
   they have real part equal to exactly $1/2$?

### Counting Zeros Part 1

To answer the first question, we can make use of a powerful theorem from
complex analysis called the [argument
principle](https://en.wikipedia.org/wiki/Argument_principle#Generalized_argument_principle).
The argument principle says that if $f$ is a meromorphic function on some
closed contour $C$, and does not have any zeros or poles on $C$ itself, then

$$\frac{1}{2\pi i}\oint_C \frac{f'(z)}{f(z)}\\,dx = \\#\left\\{\text{zeros of $f$
inside of C}\right\\} - \\#\left\\{\text{poles of $f$
inside of C}\right\\},$$ where all roots and poles are counted with
multiplicity.

In other words, the integral on the left-hand side counts the number of zeros
of $f$ in a region. The argument principle is quite easy to show given the
Cauchy residue theorem (see the above linked Wikipedia article for a proof).
The expression $f'(z)/f(z)$ is called the "[logarithmic
derivative](https://en.wikipedia.org/wiki/Logarithmic_derivative) of $f$",
because it equals $d/dz \log(f(z))$ (although it makes sense even without
defining what "$\log$" means).

One should take a moment to appreciate the beauty of this
result. The left-hand side is an integral, something we generally think of as
being a continuous quantity. But it is always exactly equal to an integer.
Results such as these give us a further glimpse at how analytic functions and
analytic functions can provide results in number theory, a field which one
would naively think can only be studied via discrete means.

Practically speaking, this fact means that if the above integral computes to
something like 0.9999999, we know that it must in fact equal exactly 1. So as
long as we get a result that is near an integer, we can round it to the exact
answer.

We can integrate a contour along the critical strip up to some $\mathrm{Im}(s)
= N$ to count the number of zeros up to $N$ (we have to make sure to account
for the poles. I go into more details about this when I actually compute the
integral below).

### Counting Zeros Part 2

So using the argument principle, we can count the number of roots in a region.
Now how can we verify that they all lie on the critical line? The answer lies
in the $Z(s)$ function defined above. By the points outlined in the previous
section, we can see that $Z(s)$ is zero exactly where $\zeta(s)$ is zero on
the critical strip, and it is not zero anywhere else. In other words,

<div style="text-align:center"> <b>the zeros of $Z(s)$ are exactly the non-trivial zeros of $\zeta(s)$.</b></div>

This helps us because $Z(s)$ has a nice property on the critical line. First
we note that $Z(s)$ commutes with conjugation, that is $\overline{Z(s)} =
Z(\overline{s})$ (this isn't obvious from what I have shown, but it is true).
On the critical line $\frac{1}{2} + it$, we have

$$\overline{Z\left(\frac{1}{2} + it\right)} = Z\left(\overline{\frac{1}{2} +
it}\right) = Z\left(\frac{1}{2} - it\right).$$

However, $Z(s) = Z(1 - s)$, and $1 - \left(\frac{1}{2} - it\right) =
\frac{1}{2} + it$, so

$$\overline{Z\left(\frac{1}{2} + it\right)} = Z\left(\frac{1}{2} +
it\right),$$

which means that $Z\left(\frac{1}{2} + it\right)$ is real valued for real $t$.

This simplifies things a lot, because it is much easier to find zeros of a real
function. In fact, we don't even care about finding the zeros, only counting
them. Since $Z(s)$ is continuous, we can use a simple method: counting sign
changes. If a continuous real function changes signs from negative to positive or from
positive to negative n times in an interval, then it must have at least n
roots in that interval. It may have more, for instance, if some roots are
clustered close together, or if a root has a multiplicity greater than 1, but
we know that there must be at least n.

So our approach to verifying the Riemann Hypothesis is as such

1. Integrate $\frac{1}{2\pi i}\oint_C Z'(s)/Z(s)\\,dx$ along contour $C$ that
   runs along the critical strip up to some $\mathrm{Im}(s)
   = N$. The integral will tell us there are exactly $n$ roots in the contour,
   counting multiplicity.

2. Try to find $n$ sign changes of $Z(1/2 + it)$ from $t=0\ldots N$. If we can
   find $n$ of them, we are done. We have confirmed all the roots are on the
   critical line.

Step 2 could fail if the Riemann Hypothesis is false, in which case a root
wouldn't be on the critical line, but it would also fail if a root has a
multiplicity greater than 1. Fortunately, as it turns out, no one has found a
root of zeta function yet that has a multiplicity greater than 1, so we should
not expect that to happen (no one has found a counterexample to the Riemann
Hypothesis either).

# Verification with SymPy and mpmath

We can either integrate right above them, or expand the contour to include
them. I chose to do the former, since it is already known that there are no
zeros near the real axis. It has also been shown that there are no zeros on
the lines $\mathrm{Re}(s) = 0$ or $\mathrm{Re}(s) = 1$, so we do not need to
worry about that. If the upper point of our contour happens to have zeros on
it, we would be very unlucky, but if it happens we can just adjust it a little
bit.

<img src="../../contour-c.svg" width="608">

(created with [Geogebra](https://www.geogebra.org/graphing/nmnsaywd))
