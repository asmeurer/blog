Title: Meeting Ondrej in Los Alamos
Date: 2009-07-13 02:22
Author: asmeurer
Category: Uncategorized
Slug: meeting-ondrej-in-los-alamos

So Ondrej was kind enough to have me over to his house in Los Alamos for
Friday and Saturday. We spent a lot of time coding together. While we
worked on some other things too, we mainly worked on my constant class.
Ondrej and I came up with an idea for restructured Mul and Add classes
that would allow different objects in them to handle the other objects
in them. The way it is now, if I want my Constant object to absorb other
objects, like `2*a*C*x => C*x`, I have to hardcode it into Mul. The same
is true with Add. This makes the Mul and Add classes muddy. Right now,
there is already special handling for other such dynamic objects such as
Order classes (e.g., `O(x)`), and Infinity class. See the
`Add.flatten()` and `Mul.flatten()` methods in sympy/core/add.py and
sympy.core/mul.py to see what I mean.

We came up with a system where symbols and numbers are handled the same
way, because we need them to be fast, but if an expression has an object
that has a `handle_mul()` method, it will call that method with the
other objects in the expression in the Mul/Add and the object will take
care of the special handling. Ondrej was able to get most of it working
in his experimental core that doesn't use assumptions [here][]. We will
hopefully end up using it, but we need to wait until we merge the new
assumptions system.

So in the mean while, I have a working Constant class that modifies Mul
and Add [here][1]. Since it will take a while until the new assumptions
system is done ([Fabian Seoane][] is doing it for his Google Summer of
Code project), we may end up temporarily adding in my Constant branch.
Once I have a working Constant class, I can solve [homogeneous
differential equations][] (not to be confused with [first order
differential equations with homogeneous coefficients][]) with one case
(there are several cases depending on whether the roots of the so called
characteristic equation are real, imaginary, or complex, but we can
actually handle them in one case if we have constants that combine into
each other. More on this in a later post). Once I have that (which I
have everything already except for the arbitrary constants), I can then
implement [variation of parameters][], which, along with separable, will
probably be the most used solver of the ones that I will implement this
summer.

Once I get those, I can clean up a lot of the 2nd order differential
equation code in dsolve (currently it is just a hack with a bunch of
special cases all covered by variation of parameters). With that code
cleaned up, I can refactor dsolve to use my proposed hints engine, which
will allow the user to choose which methods they want to use to solve an
equation (more on that in a later post too).

  [here]: //github.com/certik/sympyx.git
  [1]: http://github.com/asmeurer/sympy/tree/constant-Mul
  [Fabian Seoane]: http://fseoane.net/blog/
  [homogeneous differential equations]: http://en.wikipedia.org/wiki/Linear_differential_equation#Homogeneous_linear_differential_equation_with_constant_coefficients
  [first order differential equations with homogeneous coefficients]: http://asmeurersympy.wordpress.com/2009/05/31/first-order-differential-equations-with-homogeneous-coefficients/
  [variation of parameters]: http://en.wikipedia.org/wiki/Variation_of_parameters
