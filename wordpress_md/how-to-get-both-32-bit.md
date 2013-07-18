Title: How to get both 32-bit and 64-bit Python in Snow Leopard
Date: 2009-11-13 01:16
Author: asmeurer
Category: Uncategorized
Slug: how-to-get-both-32-bit

We had some discussion on one of the Python issues about whether my
Python in Snow Leopard should be 32-bit or 64-bit. I originally thought
that it was tied to what the kernel was, but I turned out to be wrong.

From what I discovered, the important thing is what the Python was
compiled as. You can tell what your Python has been compiled as by
running:  
` >>> import sys >>> from math import log >>> log(sys.maxsize, 2)`  
If this is just under 31, then it is 32 bit. If it returns 63, then it
is 64. An easier way to tell it to run:  
` >>> 2**40`  
If you get 1099511627776L, then you have 32-bit Python, if you get
1099511627776, you have 64-bit Python (notice that the number is long in
32-bit Python, because it is larger than maxint).

This test won't work in Python 3 because all integers are "long" by
default, but the first part will still work.

So why does this matter, you ask? Well, aside from the fact that much
longer numbers are not long (anything less than 2\*\*63 - 1 =
9223372036854775807), there is the issue of hashing.

In 64-bit Python:  
` >>> hash('a') 12416037344`

but in 32-bit Python  
` >>> hash('a') -468864544`

SymPy uses hash values to order arguments, so often it happens that
behavior in one architecture will not show up in the other. These
problems are often hard to track and fix, but the worst is when things
work fine on the machine you are working on. This actually happened to
me with my GSoC project. I was renumbering the arbitrary constants in
the printing order in an expression, but it turned out that the printing
order of an expression can be dependent on .args order, so I had to
modify the tests to canonize the numbering first.

So here comes the crux of the post. It turns out that on Mac OS X, if
you install the binary from python.org (Mac Installer Disk Image), this
installs a 32-bit Python (for compatibility reasons) in
/Library/Frameworks/Python.framework/Versions/2.6/bin/python2.6  
. However, if you install Python using 64-bit fink in Snow Leopard, it
will compile it from source into 64-bit, and install it into
/sw/bin/python2.6.

So now I have an easy way to test both architectures without having to
ssh into some other machine, which was what I was doing before.
