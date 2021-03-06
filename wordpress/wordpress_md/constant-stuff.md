Title: Constant stuff
Date: 2009-07-16 05:06
Author: asmeurer
Category: Uncategorized
Slug: constant-stuff

So I was able to get a working version of the Constant class, but
because the code cluttered up the internal Add and Mul classes too much,
Ondrej convinced me that to make a function that does the simplification
instead, and I reluctantly agreed. After begining work on it, I realized
that it will be much easier to make it just an internal function that
handles the special cases presented by `dsolve()`. That means that it
will only handle arbitrary constants that are independent of one
variable, and it will only work with constants that are named as "C1",
"C2", and so on.

If we ever get the sympyx core that Ondrej and I worked on when I was in
Los Alamos in, it will be easy for my to use a Constant class, because
it will have handler logic that will allow for the Constant class to
exist independent of Add and Mul. It already can exist independent of
Pow with a minor code addition, but simplifying powers is easier than
simplifying addition and multiplcation because exponentiation is neither
commutative nor associative, meaning that you don't have to worry about
absorbing stuff on the other side of something, like `2 + x + C`.

See my [constant-Mu][]l branch for my working version of a Constant
class the implements in Mul and Add. See my [constant-function][] branch
for my work on the internal function.

Because I have decided to make thing simple and make the function
internal only, I should have things up and running soon. Then, it will
be simple to fix up my nth order homogeneous stuff that I already have
so that it works, and then to implement variation of parameters!

  [constant-Mu]: http://github.com/asmeurer/sympy/tree/constant-Mul
  [constant-function]: http://github.com/asmeurer/sympy/tree/constant-function
