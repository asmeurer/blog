Vim vs. Emacs (Part 3)
######################
:date: 2012-01-13 23:01
:author: asmeurer
:category: Uncategorized
:slug: vim-vs-emacs-part-3

See parts `1`_ and `2`_.

Some more comments after using emacs for a while:

.. raw:: html

   <li>

I finally found the perfect tab completion solution. It took way too
much searching for how awesome it is. It's called `auto-complete-mode`_.
The best way to get an idea of what this is is to watch `this
screencast`_. Basically, it shows you a completion list automatically.
It uses the *TAB* key to do completion (to me, this is a no brainer, but
for some reason, no other completion extension that I found did this,
requiring you to do all kinds of nonsense in your .emacs file). It's got
cool features like simple fuzzy matching and intelligent matching (so
the first completion is what you tend to use, instead of just the first
one that matches). To quote the author, "a goal of auto-complete-mode is
to provide a system that does what users want without any command." I
couldn't agree with that goal more. If you install it, I recommend
adding ``(define-key ac-mode-map (kbd "M-TAB") 'auto-complete)`` to your
.emacs, so that you can use M-TAB to force the completion menu to come
up. This generally happens automatically, but I think this is the only
way to get fuzzy matching, for example. Actually, you can also just use
``(ac-set-trigger-key "TAB")``, which intelligently sets TAB to complete
or indent, based on which one you more likely want. This seems to work
pretty well to me.

.. raw:: html

   </li>

.. raw:: html

   <li>

Speaking of indenting, emacs has a pretty nice indentation feature for
Python. You just press ``TAB`` repeatedly, and it cycles through all the
syntactically legal indentations. I find this to be more useful than the
usual ``TAB`` indents behavior of most editors. Note that by default, it
won't automatically indent, even with trivial indentations (i.e.,
keeping the previous indentation). This is easy to fix, though. Just add
``(define-key global-map (kbd "RET") 'newline-and-indent)`` to your
.emacs file. This will make ``RET`` do the same thing as ``C-j``, i.e.,
basically the equivalent of ``RET TAB``.

.. raw:: html

   </li>

.. raw:: html

   <li>

emacs comes with an extension that lets you work with version control
systems, called VC. I don't use it. I don't like stuff messing with my
git stuff behind my back (sounds like a good way to lose data to me),
and I'm good enough with git commands straight that I don't need the
help.

But unlike all the other hundreds of emacs features that I don't use,
this one was seriously slowing down my workflow. It adds three or four
seconds to the startup time of emacs when loading from within a git
repository. So I did some Googling and added this to my .emacs file:

| [code]
|  ;; Disable all the version control stuff
|  ;; Makes emacs load much faster inside git repos

| (setq vc-handled-backends nil)
|  [/code]

(*unrelated: Why doesn't WordPress support lisp as a language for syntax
highlighting?*)

.. raw:: html

   <p>

This disables the version control stuff, making emacs load fast again
(virtually as fast as vim, actually).

.. raw:: html

   </li>

.. raw:: html

   <li>

Speaking of making emacs go faster, make sure you compile all your
extensions into byte code. For whatever reason, emacs doesn't do this
automatically, even though compiled files run much faster, and it
doesn't take very long. The easiest way is to use
``M-x byte-compile-file`` from within emacs. Just make sure that if you
modify the .el file that you recompile the byte code, or it will
continue to use the old version.

.. raw:: html

   </li>

.. raw:: html

   <li>

I finally figured out how to enable mouse support. For whatever reason,
Googling got me nowhere with this, so I ended up asking on the
`help-gnu-emacs`_ list, which was very helpful. The solution is to put

| [code]
|  ;; ===== Enable mouse support ====

| (require 'xt-mouse)
|  (xterm-mouse-mode)
|  [/code]

.. raw:: html

   <p>

in your .emacs file. And then it just works. It needs some tweaking
(e.g., it doesn't play so well with momentum scrolling), but at least it
works. I thought I was going to hang myself without mouse support.
Because frankly, as good as the movement commands are, moving with the
mouse is so much easier sometimes (the same is true for vim too, btw).

.. raw:: html

   </li>

.. raw:: html

   <li>

I compiled the git version of emacs (it's not very hard btw). I did this
to see if the mouse suport "bug" was fixed there, but I've gone ahead
and kept using it, as it's nicer. But I didn't figure out how to
configure it to not load in an X window. So for now, I've aliased
``emacs`` to ``emacs -nw``. I'm sure I just need to add some flag to
``configure``, but I haven't gotten around to looking it up yet.

.. raw:: html

   </li>

.. raw:: html

   <li>

I found out how to allow editing in the Isearch mode (again, thanks to
the help-gnu-emacs list). You need to install the `isearch+`_ extension,
add the following to your .emacs,

| [code]
|  ;; ===== isearch+ =====

| (require 'isearch+)
|  [/code]

.. raw:: html

   <p>

and most importantly, you need to edit the file and uncomment all the
commmands you want to allow. If you follow my link above, it goes to my
personal dotfiles repo, where I've already done that.

.. raw:: html

   </li>

.. raw:: html

   <li>

On a related note, this is the first of several emacs extensions I've
installed that I've edited the extension file itself for. The rest, I
just had to add some code to .emacs. In most cases, there was already a
variable or suggested code snippet to add to .emacs to get what I
wanted.

.. raw:: html

   <p>

On the other hand, with vim, I had to edit virtually every extension I
installed to make it do what I want. I'm not sure what this means,
though. It could be a statement about one of many things: how the emacs
community provides nicer defaults, how the vim language is easier to
use, and hence more inviting for me to edit the files, or how I haven't
gotten around to messing with certain things yet.

.. raw:: html

   </li>

.. raw:: html

   <li>

If you do a lot of work with LaTeX, check out `AUCTeX`_. I haven't used
it enough yet to say much about it, but from what I've played around
with, it's pretty awesome. And if you use a windowed version of emacs,
it's got a really awesome preview mode.

.. raw:: html

   </li>

.. raw:: html

   <li>

If you're bored, check out the `predictive`_ extension. It's actually
not as helpful as you'd think (unlike the very similar
auto-complete-mode module mentioned above). But it's kind of cool to
turn on and play around with when you're typing something. Maybe you'll
learn new words or something.

.. raw:: html

   </li>

.. raw:: html

   <li>

I could go on and on. I haven't mentioned the most basic customizations
(like how to setup four-space tabs). If you are starting to use emacs, I
recommend going through ``M-x customize``, and reading my ```.emacs```_
file. And my best advice: if you want emacs to do something, first do
``M-x customize`` and search for what you want (EDIT: apparently
searching customize requires emacs 24, i.e., the development version).
If you don't find what you want there (and you will surprisingly often),
search Google. There are so many emacs users, that the chances of
someone else wanting what you want are very likely. I've found the
results from the `emacs wiki`_ to be particularly helpful. And one more
thing: if you find an extension you like, double check first to see if
it's not already included in emacs. Emacs seems to like including good
extensions in future releases, so an older extension has a good chance
of already being included.

.. raw:: html

   </li>

Some emacs questions:

.. raw:: html

   <li>

I tried ``(define-abbrev global-abbrev-table "Ondrej" "Ondřej")``, so
that when I type Ondrej it give me Ondřej. But it doesn't work. Is this
a bug or what? If I do
``(define-abbrev global-abbrev-table "foo" "bar")`` and type "foo", it
turns into "bar", but the above leaves Ondrej alone. *EDIT: I guess this
was an emacs bug. It doesn't seem to be there any more (perhaps it was
fixed with the git version or something).*

.. raw:: html

   </li>

.. raw:: html

   <li>

Is there a way to reload .emacs without closing emacs? I'm doing that a
lot these days. *EDIT: I found it. Do ``M-x load-file RET ~/.emacs``*

.. raw:: html

   </li>

.. raw:: html

   <li>

Is there a good emacs equivalent of the vim `tag list plugin`_ (thanks
for commenter Scott for pointing me to that in the first place)? I just
want something that lists all the class and function definitions in a
Python file in order, so I can easily jump to the one I want, or just
get an overview of the file.

.. raw:: html

   </li>

This Tuesday will mark the point where I will have spend as long using
emacs as I did using vim. But already, I feel more competent with emacs.
I won't repeat what I said in my last post, but I just want to say that
the ability to edit and write at the same time makes me way more
productive. The fact that it uses keyboard shortcuts that I'm already
used to probably helps a lot too. Even so, I've not used any kind of
cheat sheet for emacs (since I never really found any that were any
good), and yet I feel like I've memorized more key commands now than I
ever did with vim, for which I did use a `cheat sheet`_.

So I really don't see myself going back to vim at this point.

I'm actually surprised. Virtually everyone I know who uses a command
line editor uses vim. It's definitely the more popular of the two. But
having tried both, I can only speculate as to why. Vim has a much higher
learning curve than emacs. Everybody grows up learning how to write text
in editors like Microsoft Word, TextEdit, Notepad, etc., that all work
fundamentally like emacs: if you type text, it enters the text. If you
want to do advanced editing with the keyboard, you hold down some meta
keys and type chorded keyboard shortcuts. The vim modal editing
methodology is so different from this, that it surprises me that so many
people go to the trouble of learning it (I mean, to the point that they
are more efficient with it). I can see the benefit over GUI editors,
which have nothing on either vim or emacs with regards to customization,
or just the plain editing power that is really necessary for coding. My
guesses why people use vim:

.. raw:: html

   <li>

They are shown vim first, so just use it.

.. raw:: html

   </li>

.. raw:: html

   <li>

They are turned off by the massiveness of emacs (it seems contradictory
to me, since the whole point of using a command line editor is to get
more power, but I could see it).

.. raw:: html

   </li>

.. raw:: html

   <li>

They are turned off by emacs lisp.

.. raw:: html

   </li>

.. raw:: html

   <li>

Some combination of those.

.. raw:: html

   </li>

Maybe the vim users out there could comment why they use vim. Am I
missing something? Or are your heads just wired differently from mine?
And if you use emacs (or anything else), I'd love to hear from you too?

At any rate, I recommend that anyone who wants to give command line
editors a chance do what I did: learn both vim and emacs. My blog posts
should be enough to give you some good advice. I went cold-turkey, and I
recommend that you do too, but only do it if you won't have any
important editing to do for a few weeks, as your editing rate will slow
down a lot as you are learning for both editors. And even though I think
I am going to stick with emacs, learning vim was still valuable. Unlike
emacs, vi is part of the POSIX standard, so it's included in pretty much
every UNIX distribution. I'll be glad when I find myself on a minimal
command line and know how to use a decent text editor. And anyway, you
can't really know which one will be your way until you try them both. I
really thought I would end up using vim, as it was so popular among all
the people I know who use command line editors. But I guess there is
only `One True Editor`_.

**EDIT:** I found out how to make emacs really fast. The key is to run
one process of emacs in daemon mode, and have the rest connect to that.
Then you only have to wait for the startup once (per computer session).
To do it, just set your ``EDITOR`` to ``'emacsclient -a "" -nw'`` (and
you might also want to alias ``emacs`` to that as well). What this does
is connect to the emacs daemon. The ``-a ""`` starts one if it isn't
already started (you can also do this yourself with ``emacs --daemon``.
If you only want to use the daemon version if you've specifically
started it, replace ``""`` with ``emacs``. This will connect to the
daemon if it's running, and otherwise just start a new emacs process.

The ``-nw`` keeps it from running in window mode. Remove this if you use
the GUI version of emacs. This is necessary to make it work correctly
with multiple tabs. This is so fast that you should never really even
need to use ``C-z`` to quickly exit emacs. ``C-x C-c`` is just fine,
because reopening will be instantaneous. I like this because I was
starting to accumulate background emacs processes that I forgot about.

This probably requires a fairly new version of emacs, possibly even the
development version.

.. _1: http://asmeurersympy.wordpress.com/2011/12/20/vim-vs-emacs-part-1/
.. _2: http://asmeurersympy.wordpress.com/2012/01/03/vim-vs-emacs-part-2/
.. _auto-complete-mode: http://cx4a.org/software/auto-complete/manual.html
.. _this screencast: http://www.youtube.com/watch?v=rGVVnDxwJYE
.. _help-gnu-emacs: https://lists.gnu.org/mailman/listinfo/help-gnu-emacs
.. _isearch+: https://github.com/asmeurer/dotfiles/blob/master/.emacs.d/lisp/isearch%2B.el
.. _AUCTeX: http://www.gnu.org/software/auctex/
.. _predictive: http://www.dr-qubit.org/predictive/predictive-user-manual/html/index.php
.. _``.emacs``: https://github.com/asmeurer/dotfiles/blob/master/.emacs
.. _emacs wiki: http://www.emacswiki.org/
.. _tag list plugin: http://www.vim.org/scripts/script.php?script_id=273
.. _cheat sheet: http://www.viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html
.. _One True Editor: http://www.dina.dk/~abraham/religion/
