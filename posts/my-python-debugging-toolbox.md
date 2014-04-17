Python is one of the easiest programming languages to both read and write, due
to its simple syntax and high-level paradigms.  But with any programming
language, if you do anything sufficiently complicated with it, you will
eventually need to debug problems, and Python is no exception.  I've written
down here some of the tricks I've learned for debugging Python, in the hopes
that it will help others to debug their programs, and also in the hopes that
others will chime in with their own methods of debugging, so that I may
improve myself.

# What is debugging?

Before I list the tools I use, it's useful to ask what exactly debugging
is. [Wikipedia](http://en.wikipedia.org/wiki/Debugging) defines debugging as
"a methodical process of finding and reducing the number of bugs".  The
New Oxford American Dictionary defines "debug" as "identify and remove errors
from (computer hardware or software)".

Practically, both of these definitions are too broad. There is a whole process
to removing bugs:

1. Identify that there is a bug
2. Find the source of the bug in the source code
3. Implement a fix for the bug
4. Test that the fix corrects the bug

For me, and for this blog post, *debugging* refers to the second point, the
finding of the bug in the source code.  There are many useful tools for
identifying the existence of a bug, among them full code coverage testing and
flaking tools.  Only the simplest bugs can be fixed automatically, especially
in Python where there is not an abundance of easy to fix "compiler
warnings".  And testing that a fix is correct depends a great deal on the bug
itself, and your testing methodology.

While each of the four points above can present challenges, often the most
difficult is the second point. Once a bug is identified, how do we determine
its source.  The problem is inherent in the fact that the code being run is
hidden when it is running.  If we were able to act as both human and computer,
both executing the code and maintaining a high-level understanding of it,
debugging is not necessary.  In fact, we might say that the goal of a good
debugging tool is to allow us to see a sufficient portion of the code's
execution while maintaining, or in many cases, growing, our high-level
understanding of what it does.

# Tools that come with the standard library

## Looking at the code

This is such a simple method that it hardly even counts.  The first thing I do
when I encounter a bug in my code is to look at the code, trying to guess what
is going wrong.  If I have a high level of context for the code and a good
understanding of what is going on, I can often spot the issue right away.

This method is much faster than any of the below methods when it works.  The
tricky thing is knowing when to stop using this method and start using a real
debugging tool.

## `print` statements

`print` statements (or functions if you're using Python 3 like you're supposed
to be) are the second simplest method of debugging. `print` is always there,
and it's easy to type.  They will let you peak into a very specific part of
your code (whatever specific part you want), and tell you anything whenever it
is run. They also tell you how many times something is run.

Some useful tricks for print:

- If your code is outputting a lot with your print, pipe into `less`.  This
  will let you interactively see what is coming out, and you can do things
  like regex search (`/`).

- Get into the habit of printing a little header with each item. That is,
  instead of just writing

```python
print(x)
```

write

  ```py
  print('x', x)
  ```

## raise an exception

## `traceback.print_stack`

## `faulthandler`

## Writing to another terminal

# Third-party tools

## PuDB

## `IPython.embed`

## git bisect
