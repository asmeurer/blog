Title: Major API Change for the Risch Algorithm Functions
Date: 2010-12-27 07:34
Author: asmeurer
Category: Uncategorized
Slug: major-api-change-for-the-risch-algorithm-functions

I have been able to get to work again on the Risch Algorithm now that I
have a month winter break from classes. So the first thing I did was
commit a bunch of bug fixes that had been sitting there since the end of
the summer. Then, I set out to make a major internal API change to the
entire Risch Algorithm.

Let me give some background. When I first started programming the Risch
Algorithm at the beginning of the summer, I didn't have a very good idea
of how differential extensions worked yet (remember that I programmed
the algorithm as I learned it from Bronstein's book). Let me use the
function `derivation()` to demonstrate how the API has changed.
`derivation()` takes the Poly `p` in `t` and computes the derivative
(`t` is some transcendental extension, like \$latex e\^x\$). Also, the
integration variable is `x`. The first internal API that I used was

`derivation(p, D, x, t)`

where `D` is a Poly of the derivative of `t`, and `x` and `t` are
Symbols (see [this commit][]). The problem here is that `p` might not be
in just one symbol, `t`, but in many. This would happen whenever the
function had more than one transcendental function, or extension, in it.
So, for example, \$latex e\^x\\log{x}\$ would have this problem.
Surprisingly, according to the git log, it took me until July 4 to
figure this out (that above linked commit, which is the first occurrence
of this function and when I started the full algorithm, dates from June
7, so it took me almost a month!), after which I had already written a
good portion of the Risch Algorithm. I changed the API to

`derivation(p, D, x, T)`

where `T` is a list of the extension variables and `D` is a list of the
derivations of the respective elements of `T` with respect to the lower
elements and x (see [this commit][1]). Now, the derivation of `x` is
always `Poly(1, x)`, so I didn't think it was necessary to include it.
But it turns out that it is easier to just always include this in `D`
rather than try to special case it in the code. Also, the lowest
extension variable, `x`, isn't used very often in the code, so it also
doesn't make much sense to keep it separate from the rest of the
variables in `T`. Now this didn't take me as long to figure out (July
11). Therefore, I changed the API to just

`derivation(p, D, T)`

where the first element of `T` is always `x` and the first element of
`D` is always `Poly(1, x)` (see [this commit][2]).

Now this API worked quite well for the remainder of the summer. However,
at the very end, I discovered that a function required to handle some
special cases in certain parts of the algorithm needed four more lists
(the elements of the extension that are logarithms, the elements of the
extension that are exponentials, the arguments of those logarithms, and
the arguments of those exponentials). I had previously thought that
these lists would only be needed when creating the extension at the
beginning of integration, but it turned out that this was not the case
and that they could be needed in several rather deep places in the
algorithm. The only way to get them there would be to pass them through
to every single function in the algorithm.

So I was faced with a dilemma. I didn't want to pass six arguments
through each function just because a few might need them all. I knew
that the answer was to create an object to store all the data for a
differential extension and to just pass this object around.
Unfortunately, this happened at the very end of the summer, so I hadn't
been able to do that until now.

This brings us to now. Over the past couple of weeks, I created an
object called `DifferentialExtension`, and replaced the API in the Risch
Algorithm to use it. See [this commit][3] and [this commit][4] and some
of the ones in between to see what I did. More or less, the object is
like a C struct---it does little more than hold a lot of information as
attributes. However, at the suggestion of Ronan Lamy on the [mailing
list][], I have moved all the relevant code for building the extension
from the `build_extension()` function into
`DifferentialExtension.__init__()`. I have also created some "magic" to
handle the recursive nature of the algorithm. A DifferentialExtension
object has an attribute `level`, which represents the level of the
extension that the algorithm is working in. So you can store all the
derivations of the extension in `DifferentialExtension.D`, but only have
`DifferentialExtension.d` point to the "current" outermost derivation.
This replaces things like

`D = D[:-1] T = T[:-1]`

from the old API to just

`DE.decrement_level()`

(and then later on, `DE.increment_level()`). The entire API is now just

`derivation(p, DE)`

where `DE` is a `DifferentialExtension` object. Changing the API of the
entire code base at this point was a bit of work, but I have finally
finished it, and I must say, this is much cleaner. True, you now have to
use `DE.t` everywhere instead of `t` (with `t = T[-1]` at the top of the
function), which is three characters more space for every use, but I
think in the end it is cleaner. For example, the function that used to
be

`is_log_deriv_k_t_radical(fa, fd, L_K, E_K, L_args, E_args, D, T)`

is now just

`is_log_deriv_k_t_radical(fa, fd, DE)`.

Also, because it is an object, I can do cool things like override
`DifferentialExtension.__str__()` to print out a tuple of the most
important attributes of the object, making debugging much easier (now
there is just one print statement instead of five).

Another thing I had to do was to allow the creation of these objects
manually, because what is now `DifferentialExtension.__init__()` cannot
yet handle, for example, tangent extensions, but some of the tests
involve those. So I created an `extension` flag to `__init__()` to which
you could pass a dictionary, and it would create a skeleton extension
from that (see [this commit][5]). I made it smart enough to create some
attributes automatically, so I only have to pass the list `D` in most
tests---it creates attributes like `T` from that automatically. Thus,
this in some ways made the tests a little simpler, because I didn't have
to worry about `T` any more.

We'll see how things go, but this fourth API change should hopefully be
the last. This should also make it much easier whenever I add
trigonometric function support, where I will have to add even more
attributes to the object. I won't have to change the code in any
existing function (unless it specifically needs to be able to know about
trig extensions), because, to them, the information in `DE` will not
change.

So the good news behind all of this, as I mentioned at the beginning of
this post, is that I can now write some algorithm that requires those
`L_K`, `E_K`, `L_args`, `E_args` variables from arbitrary places within
the algorithm. This should allow me to completely finish the exponential
case. So look forward soon to a `risch_integrate()` that can handle
completely any transcendental function of exponentials (either produce
an integral or prove that no elementary integral exists).

And just to be clear, this doesn't change anything with
`risch_integrate()`---this is only an internal change. And at the
moment, it doesn't add any features, though that should soon change. So
keep on testing it for me! If you see any errors along the lines of
"Variable t not defined," it probably means that I missed that one when
I was switching the API due to poor test coverage in that area of the
code. I would love to know about any errors you find, or, indeed, any
testing you do with `risch_integrate`. Remember that you can obtain my
branch at [my GitHub account (branch integration3)][].

  [this commit]: https://github.com/asmeurer/sympy/commit/0f6a3d90f724118fadc5fdaf290a0cb3e3963efd
  [1]: https://github.com/asmeurer/sympy/commit/20b7a5f8ca8dec579065f85583f11cc0955b96f0
  [2]: https://github.com/asmeurer/sympy/commit/bca2b19844ae71aa1ef8e27a9f77eabb70b4aa5f
  [3]: https://github.com/asmeurer/sympy/commit/d9d9548625513188aaa663621bfe4e097aebf741
  [4]: https://github.com/asmeurer/sympy/commit/1935b6d6e1fdf8eae4deb5a4f56ea53c5d6989fa
  [mailing list]: http://groups.google.com/group/sympy/browse_thread/thread/a051b5ba1fb5cb4d
  [5]: https://github.com/asmeurer/sympy/commit/7121b06eab3f1e0f8464c287438fb7175f07762b
  [my GitHub account (branch integration3)]: https://github.com/asmeurer/sympy/tree/integration3
