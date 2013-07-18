Tip for debugging SymPy with PuDB
#################################
:date: 2013-01-28 00:43
:author: asmeurer
:category: Uncategorized
:slug: tip-for-debugging-sympy-with-pudb

Usually, when I debug SymPy code with `PuDB`_, I create a script that
calls the code, then I put a

| [code language="py"]
|  import pudb; pudb.set\_trace()
|  [/code]

in the SymPy library code where I want to start debugging. But this is
annoying, first because I have to create the script, and second, because
I have to modify the library code, and there's always the risk of
accidentally commiting that. Also, if I want to start debugging
somewhere else, I have to edit the files and change it.

Well, I just figured out a better way. [STRIKEOUT:First, if you haven't
already, add an alias like this in your bash config file (``~/.profile``
or ``~/.bashrc``):\ ``alias pudb='python -m pudb.run``.] *As of `this
pull request`_, this is no longer necessary. A ``pudb`` script is
installed automatically with PuDB.*

This will let you run ``pudb script.py`` to debug ``script.py``.
[STRIKEOUT:Next, start PuDB. It doesn't matter with what. You can just
run ``touch test.py``, and then ``pudb test.py``.] *It occured to me
that you can just set the breakpoint when starting isympy with PuDB.*

Now, press ``m``, and navigate to where in the library code you want to
start debugging. It also helps to use ``/`` to search the current file
and ``L`` to jump to a specific line. When you get to the line where you
want to start debugging, press ``b`` to set a breakpoint. You can do
this in multiple places if you want.

Now, you just have to start ``isympy`` from within PuDB. Just run
``pudb bin/isympy``, and immediately press ``c`` to jump to the
interactive prompt. Now, run whatever code you want to debug. When it
gets to the breakpoint, PuDB will open, and you can start debugging. If
you type ``c`` to continue, it will go back to isympy. But the next time
you run something that hits the breakpoint, it will open PuDB again.

This trick works because breakpoints are saved to file (at
``~/.config/pudb/saved-breakpoints``). In fact, if you want, you can
just modify that file in the first step. You can edit your saved
breakpoints in the bottom right pane of PuDB.

When you are done and you type ``Ctrl-D`` PuDB will pop-up again, asking
if you want to quit. That's because it was running the whole time,
underneath isympy. Just press ``q``. Note that you should avoid pressing
``q`` while debugging, or else PuDB will quit, and you will be left with
just normal isympy (it won't break at your breakpoints any more).
Actually, if you do this, but doing ``Ctrl-D`` still opens the PuDB
prompt, you can just press "Restart", and it should start working again.
Note that "Restart" will not actually reset isympy: all your saved
variables will still be the same, and any changes to the library code
will not be reloaded. To do that, you have to completely exit and start
over again.

Of course, there is nothing SymPy specific about this trick. As long as
you have a script that acts as an entry point to an interactive console
for your application, you can use it. If you just use IPython, you can
use something like ``pudb /bin/ipython`` (replace ``/bin/ipython`` with
the output of ``which ipython``).

.. _PuDB: http://asmeurersympy.wordpress.com/2010/06/04/pudb-a-better-python-debugger/
.. _this pull request: https://github.com/inducer/pudb/pull/54
