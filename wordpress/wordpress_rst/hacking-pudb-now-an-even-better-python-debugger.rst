Hacking PuDB: Now an even better Python debugger
################################################
:date: 2011-08-08 03:16
:author: asmeurer
:category: Uncategorized
:slug: hacking-pudb-now-an-even-better-python-debugger

Readers of this blog may remember last year when I `wrote`_ about this
awesome visual console Python debugger called `PuDB`_. I suggest you
read that post if you haven't.

At the end of that post, I noted that Ondřej and I had hacked it to make
the colors more livable. Well, a couple of weeks ago, GitHub user
`jtriley`_ sent me an email asking me to back port my changes.

A lot has changed since I wrote my blog post last year. PuDB now has an
official `mailing list`_ and an official `GitHub repo`_.

So I deleted my `GitHub clone`_ and reforked from the official version.

A lot has also changed in the official code. Andreas had added config
support, including a built-in prefs dialog that lets you set a few
settings: the ability to turn on or off line numbers and the ability to
change themes.

So I took the new code and added my theme as an official theme. This was
pretty straight forward to do.

But then, I got a little carried away.

I noticed that it was difficult to choose a theme with the built-in
prefs window because you had to close and reopen the window each time
you made a change. So I added code to make it auto-update your changes
as you made them.

Then I went back and looked at my original blog post and looked at the
things that I didn't like. There were two things. First, the default
stringifier for variables is ``type``, which is completely useless. This
is because ``type`` is very fast and stable to compute. I had previously
hacked this to be ``str``, but now that there was an official config
file with a prefs dialog, I figured it should go there.

So I added support to change this setting. But this wasn't enough for
me. I also added the ability to define your own custom stringifier. You
just create a Python file that defines a function called
``pudb_stringifier(obj)``, which converts ``obj`` into the desired
string representation. I included an `example file`_ that gives a fancy
example that uses signals to compute the string value, but times out
after one second and falls back to the type. This alleviates one of the
problems of using ``str``, which is that it can be slow for objects with
large string expressions, especially SymPy objects, where sometimes the
printer can be slow.

The second thing I didn't like was that although you can change the
width of the right-hand side bar, you could not change the relative
heights of the variables, stack, and breakpoints boxes. I never use
breakpoints, and rarely use the stack, so I would prefer to have those
smaller and the variables larger. So I implemented it so that the ``[``
and ``]`` keys make the selected view smaller or larger. This
information is all saved in the config file, so it's remembered when you
close and reopen PuDB.

There was one other thing that I didn't like, which a change since my
last blog post that reversed the order of the stack variables from what
it was. It used to be most recent at the bottom, but it was changed to
most recent at the top. This perhaps makes more sense, but the buttons
to move around the stack, ``u`` and ``d``, were still the same: ``u``
moves down the stack (i.e., less recent), and ``d`` moves up. These keys
were already well established—indeed, these are the same keys used in
Python's built-in debugger pdb—so I added a setting to change the stack
order. This was an easy change to make at this point, as I was already
well aquatinted with the settings code, and only two lines of code
needed to be changed when the setting changed. Like all other settings,
this uses the cool magic that changes the setting in real time, so you
can see the effect without closing the settings window.

Then someone on the mailing list requested a feature that I realized I
also wanted, the ability to wrap variables. Previously, any variable
that was longer than the variable view would just be cut off. You could
make it wider, but that only helped a little bit. Otherwise, if you
wanted to see the whole variable, you had to open IPython by pressing
``!`` and view it there.

So, I implemented this. This was definitely the hardest thing to
implement. I found out that it's ironically very difficult to debug PuDB
itself. You can't run PuDB inside of PuDB if PuDB crashes, as both
instances will just crash. Also, PuDB eats any print statements. The
solution, suggested by PuDB author Andreas Klöckner, was to get the ttys
file of another terminal (e.g., ``/dev/ttys012``) and write the output
to that.

I also made it so that non-wrapped variables show ``...`` at the end, at
Andreas's suggestion. I wanted to use the unicode ``…``, but this was
not working at all. I discovered how much unicode really is a mess in
Python 2. The problem has something to do with … being a three byte
character, and I think it also has to do with the color codes that urwid
uses. I'll try it again once PuDB is ported to Python 3, but for now, we
are going to have to do with the three ascii dots.

The wrapping code is waiting for merge, but the rest are already in.
Here is a screen shot demonstrating some of the things I did:

[caption id="attachment\_1021" align="alignnone" width="300"
caption="Click for full size image"]\ |image0|\ [/caption]

Things that I implemented to notice here:

| - The midnight theme.
|  - The stack and breakpoints views have been shrunken.
|  - The variables are wrapped.
|  - Wrapping for the variable ``fourhundred`` has been turned off (you
can turn wrapping on or off on a per-variable basis by selecting the
variable and pressing ``w``). Notice that there is an ellipsis at the
end to note it has been cut off.
|  - Nested variables now have ``|`` before them, to distinguish them
from wrapped variables, which are also indented. This change may or may
not be accepted by Andreas.

Here's a screen shot showing the prefs window. I did not implement this,
but I did implement all but the first two preferences in the window.
I've made my window tall so you can see all the options. You really have
to get the code and try it to see the auto-update awesomeness. You can
open the prefs window by pressing ``Ctrl-p`` (this was not at all
obvious to me the first time I used it, so I also submitted a patch that
makes it open the first time you use PuDB).

[caption id="attachment\_1023" align="alignnone" width="243"
caption="Click to see full size image"]\ |image1|\ [/caption]

So if you're not already using this awesome Python debugger, you should.
You can ``pip install pudb``, or `fork it`_ at GitHub.

Running it in your code is very easy. Just add

| [code lang="py"]
|  import pudb;pudb.set\_trace()
|  [/code]

in your code wherever you want to set a break point, or you can do
``python -m pudb.run script.py``.

This awesome tool has increased my productivity tenfold since I
discovered it, and has helped me track down bugs that would have
otherwise extremely difficult if not impossible to find. And now, it's
just better.

PuDB uses the `urwid library`_ to do all its console GUI magic. This
library makes it pretty easy to do a lot of stuff. For example, it
automatically does relative sizing of widgets, so, for example, when you
resize the variables, stack, or breakpoints views, you are actually
increasing the relative size of each, not the size in characters. This
makes it portable against any terminal size. The library also made
coding the prefs window autoupdate magic very easy.

Also, I just want to note that git and GitHub make collaboration like
this very easy. I just forked his project, made some improvements, and
submitted them as pull requests. Then it was easy to discuss the
changes. If the code had not been on GitHub and especially if it had not
been in git, I probably would have never bothered to submit my
contributions upstream. I highly recommend that every open source
project use git and GitHub.

.. _wrote: http://asmeurersympy.wordpress.com/2010/06/04/pudb-a-better-python-debugger/
.. _PuDB: http://pypi.python.org/pypi/pudb
.. _jtriley: https://github.com/jtriley
.. _mailing list: http://lists.tiker.net/listinfo/pudb
.. _GitHub repo: https://github.com/inducer/pudb
.. _GitHub clone: https://github.com/asmeurer/pudb
.. _example file: https://github.com/inducer/pudb/blob/master/example-stringifier.py
.. _fork it: https://github.com/inducer/pudb
.. _urwid library: http://excess.org/urwid/

.. |image0| image:: http://asmeurersympy.files.wordpress.com/2011/08/screen-shot-2011-08-07-at-8-28-11-pm.png?w=300
   :target: http://asmeurersympy.files.wordpress.com/2011/08/screen-shot-2011-08-07-at-8-28-11-pm.png
.. |image1| image:: http://asmeurersympy.files.wordpress.com/2011/08/screen-shot-2011-08-07-at-8-41-30-pm.png?w=243
   :target: http://asmeurersympy.files.wordpress.com/2011/08/screen-shot-2011-08-07-at-8-41-30-pm.png
