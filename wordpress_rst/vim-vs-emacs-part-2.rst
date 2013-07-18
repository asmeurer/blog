Vim vs. Emacs (Part 2)
######################
:date: 2012-01-03 07:30
:author: asmeurer
:category: Uncategorized
:slug: vim-vs-emacs-part-2

As I noted in `part 1`_, I have decided to switch to a command line text
editor. I decided that, to be fair, I would try both vim and emacs. And
to force myself to learn them, I decided to use them cold-turkey.

Since I'm going cold-turkey, I am doing this over my break from classes,
so that I can weed out any difficulties during a period when I can live
with slow text editing if necessary. This is a one month break. I have
reached (roughly) the half way point. For the first half, I used nothing
but vim to edit text. Now, I will use nothing but emacs.

Now that I've stopped using vim (for now anyway), my view of it isn't
much different from what I wrote in the first part. A lot of things
there were addressed by commenters (or rather commenter). I still feel
that it's not an a method of text editing that fits my head. My entire
life, I've used text editors where typing inserts text, and various
control characters do things like move around faster.

Enter emacs. It does exactly this. Also a ton more.

I've only been using emacs for two days, but here are my impressions so
far:

.. raw:: html

   <li>

**The tutorial is better.** When you start emacs, it tells you how to
start the tutorial. Just type ``C-h t`` (if you don't already know, in
emacs ``C-`` means ``CTRL-`` and ``M-`` means ``ALT-``). Like I said
last time, the very first thing you learn is how to scroll by more than
one line at a time. That turns out to be a very useful thing to do.
Also, the emacs tutorial did a better job of explaining how to use
multiple files at once in emacs, which is something that I still don't
really know how to do very well in vim.

I have to give the vim tutorial some credit for one thing, though. It
has better interactive examples. For example, in the vim tutorial, you
have stuff like

| [code]
|  1. Move the cursor to the second line in the phrase below.
|  2. Type dd to delete the line.
|  3. Now move to the fourth line.
|  4. Type 2dd to delete two lines.

| ---> 1) Roses are red,
|  ---> 2) Mud is fun,
|  ---> 3) Violets are blue,
|  ---> 4) I have a car,
|  ---> 5) Clocks tell time,
|  ---> 6) Sugar is sweet
|  ---> 7) And so are you.
|  [/code]

whereas in the emacs tutorial, you just have

| [code]
|  >> Kill a line, move around, kill another line.
|  Then do C-y to get back the second killed line.
|  Then do M-y and it will be replaced by the first killed line.
|  Do more M-y's and see what you get. Keep doing them until
|  the second kill line comes back, and then a few more.
|  If you like, you can try giving M-y positive and negative
|  arguments.
|  [/code]

.. raw:: html

   <p>

which is a little more vague. So I have to give vim credit for that.

.. raw:: html

   </li>

.. raw:: html

   <li>

**Everything's a buffer.** This line from the emacs tutorial really
stuck with me: "ANY text you see in an Emacs window is always part of
some buffer." Emacs has really a awesome editing model, even simple
things like ``M-f`` and ``M-b`` to move around words at a time, or
``M-DEL`` to delete whole words make things **way** faster. Vim of
course has all of these too, albiet in a different way, but they aren't
everywhere. In emacs, everything is a buffer, which just means that
everything supports all the standard emacs commands. So if you type
``M-x`` (roughly the equivalent of vim's ``:``) and start typing a
command, you can move around and edit your command with emacs commands.
One of the things that bothered me about vim was that when I was typing
something with ``:``, I couldn't use vim's text moving/modifying
commands to manipulate the text. Typing ESC just canceled the command.

Exceptions: There are at least two exceptions I've found to this rule.
First, if you do a search with ``C-s`` or ``C-r``, no control commands
work. If you type a search string, and then type ``M-DEL`` to try to
delete the last word in your search string, you will instead delete the
word where the cursor is! The solution I think is to use something like
``M-x re-builder`` instead. This was a little slow in my tests.

.. raw:: html

   <p>

Second, the emacs manual is presented in the ``info`` program, which
uses completely different key commands from every other program. This
irked me quite a bit, because as soon as I finished the emacs tutorial,
it pointed me to the manual, which was in ``info``. Then, the first
thing in ``info`` is a tutorial on how to use ``info``! I opted to skip
this. If I need any information on emacs, I'll just do a Google search
anyway, so I found this to be a waste of time.

.. raw:: html

   </li>

.. raw:: html

   <li>

**It's a little slower.** I do notice a speed difference between emacs
and vim. vim is much more lightweight, and it shows. Starting up emacs
takes a second or two. Also, since a lot of the features are more
interactive, they suffer from a speed delay. It's not nearly slow enough
to be a serious issue, though, and it's still way faster than the GUI
program I was using before (start up time).

The emacs tutorial suggests using ``C-z`` whenever you want to only
temporarily close emacs. This seems like a good idea, and has worked
pretty well for me so far (though I still usually close the whole thing
with ``C-x C-c`` out of habit).

.. raw:: html

   <p>

On a related note, I noticed that doing type-ahead while waiting for
emacs to start up didn't always work, whereas it always worked in vim (I
do this, e.g., when waiting for the editor to start up when writing
commit messages).

.. raw:: html

   </li>

.. raw:: html

   <li>

**It's way more user-friendly.** Note that this is of course a relative
term. I mean more user-friendly than vim, and pretty user-friendly for a
command line program. Obviously, the most user-friendly text editors are
the GUI ones used by the majority of the population (for that very
reason). Actually, both vim and emacs are user-unfriendly in that if you
accidentally open them and don't know what they are or how to use them,
you have no idea how to close them. But even ``less`` (i.e., ``man``) is
technically like this.

I'm not even referring to the different editing "modes" of the two
editors, though you could easily argue that emacs style editing is more
user-friendly than vim style editing. What I mean here is that emacs
interaction is nice. When you type ``:`` in vim, start typing a command,
and type ``TAB``, it enters the first completion, regardless if it's
unique. Pressing ``TAB`` multiple times give the rest. In emacs, if you
type ``M-x`` and start typing a command and type ``TAB``, it pops up a
temporary window with the list of all completions. It even colors the
next character, so you can easily see what to type next to get what you
want. As soon as you enter the command, the window disappears. (yes, I
know about ``CTRL-D`` in vim, but to me tab completion should *always*
work like it does in bash: complete characters if and only if they are
unique in the list of completions)

.. raw:: html

   <p>

By the way, when I said everything's a buffer, I mean everything. If you
want, you can exit the ``M-x`` entry (type ``C-g``), type ``C-x C-b`` to
show the list of buffers, ``C-x o`` to switch to it, scroll down to
"Completions", press Enter, and actually get in the completion list, as
a buffer (there's probably a less complicated way to get to it, by the
way). You can then do whatever your heart fancies with it (save it to a
file, copy it, whatever).

.. raw:: html

   </li>

.. raw:: html

   <li>

**Customization is harder.** This was expected, since I already knew
that emacs used lisp. vim uses a language that is really easy to
understand. I was able to modify all the vim plugins I installed very
easily. If you want to change a setting globally in vim, just Google it
and add one line to your .vimrc. In emacs, everything is in Emacs Lisp.
I suppose prior experience with Lisp would probably help here.

In the vim tutorial, near the end, it told how to create a .vimrc file,
and even gave a very useful sample one as a starter. In emacs, it took
me a while to figure out how to do the equivalent (it took me a few
Google searches just to figure out that the name of the configuration
file in emacs is .emacs).

.. raw:: html

   <p>

Actually, the emacs equivalent is way better than in vim, but it isn't
really mentioned anywhere. It took me probably a dozen Google searches
before I learned about it (granted, I was looking for things in the same
way I did for vim, lines to add to .emacs). What you have to do is type
``M-x configure``. This opens what is basically a huge preferences
dialog for emacs. You can then go through and set just about every
settable emacs setting from there. The interface is very nice, as it's
interactive and tells you all about each setting. And you never have to
touch Lisp. I'm still going through it, so I can't comment more on it
yet. But I recommend doing ``M-x configure`` as soon as you have
finished the tutorial and have gotten used to editing with emacs, as you
are invariably going to want to change some things (though I should note
that emacs generally has nicer defaults than vim).

.. raw:: html

   </li>

.. raw:: html

   <li>

**Better text editing methodology?** Like I've already mentioned a bunch
of times, the emacs editing model seems to fit my head better than the
vim model. In emacs, you type text, and it inserts the text. If you want
to do some advanced modification or move around, you type a control
sequence. In vim, you type characters, and it does modifications or
moves around. If you want to type text, you type ``i`` (or one of a few
other characters) and type it. Then, if you want to move around or
modify the text, you have to press ``ESC``. This so-called "modular
editing" doesn't seem to work for me. For one thing, I like to rapidly
switch back and forth between these two "modes" (editing and inserting)
when I write things. I type too fast and write something wrong, and have
to delete some stuff. The ``M-DEL`` emacs command is probably my most
used (this also works in Mac OS X text dialogs, so I'm used to it
already). In vim, there is ``CTRL-w`` and a few others, but if I want to
do something more advanced, like rearranging a sentence, then half of my
key presses would be ``ESC`` or ``i``, i.e., just moving between the
modes. In emacs, I can always have my pinky by Control and Alt
(especially as soon as I remap CAPS-LOCK to Control).

.. raw:: html

   <p>

Also, it really irks me how in vim, if you are at the end of a line and
press ``l`` (or right-arrow), instead of moving to the beginning of the
next line, it beeps! In emacs, if you are at the end of a the line and
type ``C-f``, it moves to the beginning of the next line (actually, it
technically moves just beyond the line, in case you want to append,
which is another annoying thing about vim: you have to use ``A``, not
``i``, to add text to the end of a line).

.. raw:: html

   </li>

Well, that's it for now. I will hold off on the questions until after I
go through all the customizations, as it seems that, unlike vim, emacs
has many things already built-in (but we already knew that, didn't we
:). So I have just one question for readers: does anyone know of a
really good emacs cheatsheet? The `one I used for vim`_ was really
awesome, but I haven't found anything equal for emacs. I find myself
searching the tutorial whenever I forget something, which is not very
efficient, so I would appreciate something better. Otherwise, I'll just
find something decent and print it out, as it would be better than
nothing.

And if anyone cares, you can see what I've got for my .emacs file so far
at https://github.com/asmeurer/dotfiles/blob/master/.emacs.

.. _part 1: http://asmeurersympy.wordpress.com/2011/12/20/vim-vs-emacs-part-1/
.. _one I used for vim: http://www.viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html
