SymPy Live Sphinx Extension
###########################
:date: 2012-08-21 05:09
:author: asmeurer
:category: Uncategorized
:slug: sympy-live-sphinx-extension

I didn't blog about SymPy all summer, so I thought I would write a post
about my favorite feature of the upcoming SymPy 0.7.2 release.  In fact,
this feature has got me more excited than any other feature from any
version of SymPy.  Yeah, it's that good.

The feature is the SymPy Live Sphinx extension.  To start, if you don't
know about it, check out `SymPy Live`_.  This is a console that runs on
the `App Engine`_.  We've actually had this for quite some time, but
this winter, it got a huge upgrade thanks to the contribution of some
`GCI`_ students.  Basically, SymPy Live lets you try out SymPy in your
browser completely for free, because it runs all the code on the App
Engine.  Actually, the console is a full Python console, so you can
actually run any valid Python command on it.  This past winter, GCI
students upgraded the look of the site, added a mobile version (visit
live.sympy.org on your phone), and added other neat features like search
history and autocompletion.

Now, `Sphinx`_ is the documentation system that we use to generate
`SymPy's html documentation`_. Last year, when I was at the \ `SciPy
Conference`_, Mateusz had an idea at the sprints to create an extension
linking SymPy Live and Sphinx, so that the examples in Sphinx could be
easily run in SymPy Live.  He didn't finish the extension, but I'm happy
to report that thanks to David Li, who was also one of
the aforementioned GCI students, the extension is now complete, and is
running live on our `development docs`_.  When SymPy 0.7.2 is released
(soon I promise), it will be part of the oficial documentation.

The best way to see how awesome this is is to visit the website and
check it out.  You will need a modern browser (the latest version of
Firefox, Safari, or Chrome will work, IE might work too).  Go to a page
in the development docs with documentation examples, for
example, \ http://docs.sympy.org/dev/tutorial.html#algebra, and click on
one of the examples (or click on one of the green "Run code block in
SymPy Live" buttons). You should see a console pop up from the
bottom-right of the screen, and run your code.  For example:

[caption id="attachment\_1149" align="alignnone" width="450"]\ |image0|
Example of the SymPy Live Sphinx extension at
http://docs.sympy.org/dev/tutorial.html#algebra. Click for larger
image.[/caption]

 

You can access or hide the console at any time by clicking on the green
box at the bottom-right of the page.  If you click on "Settings", you
will see that you can change all the same settings as the regular SymPy
Live console, such as the printer type, and the keys for execution and
autocompletion.  Additionally, there is a new setting, "Evaluation
Mode", which changes how the Sphinx examples are evaluated.  The default
is "Evaluate".  In this mode, if you click on an example, it is executed
immediately.  The other option is "Copy".  In this mode, if you click an
example, it is copied to the console, but not executed right away. This
way, you can edit the code to try something different.  Remember, this
is a full fledged Python console running SymPy, so you can try literally
anything

So play with this and `let us know`_ what you think.  We would love to
hear ways that we can improve the experience even further.  In
particular, I think we should think about ways to make the "Copy" mode
more user-friendly.  Suggestions welcome!  Also, please `report any
bugs`_.

And one word of warning:  even though these are the development docs,
SymPy Live is still running SymPy 0.7.1.  So some examples may not work
until 0.7.2 is released, at which point we will update SymPy Live.

I believe that this extension represents the future of interactive
documentation. I hope you enjoy.

.. _SymPy Live: http://live.sympy.org/
.. _App Engine: https://developers.google.com/appengine/
.. _GCI: http://www.google-melange.com/gci/homepage/google/gci2011
.. _Sphinx: http://sphinx.pocoo.org/
.. _SymPy's html documentation: http://docs.sympy.org/
.. _SciPy Conference: http://asmeurersympy.wordpress.com/2011/07/17/the-scipy-2011-conference/
.. _development docs: http://docs.sympy.org/dev/
.. _let us know: http://groups.google.com/group/sympy
.. _report any bugs: http://code.google.com/p/sympy/issues

.. |image0| image:: http://asmeurersympy.files.wordpress.com/2012/08/sympy-live-sphinx.png
   :target: http://asmeurersympy.files.wordpress.com/2012/08/sympy-live-sphinx.png
