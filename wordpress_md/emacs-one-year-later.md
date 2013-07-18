Title: Emacs: One year later
Date: 2013-01-01 09:51
Author: asmeurer
Category: Uncategorized
Slug: emacs-one-year-later

As readers of this blog may remember, back in 2011, I decided to move to
a command-line based editor. For roughly two weeks in December, 2011, I
exclusively used Vim, and for the same amount of time in January, 2012,
I used exclusively Emacs. I had used a little of each editor in the
past, but this was my first time using them to do true editing work. My
experiences are chronicled in my blog posts (parts [1][], [2][], [3][],
and [7 months later follow up][]).

To summarize, I decided to use Emacs, as I found it to be much more
intuitive, and much more user-friendly. Today, January 1, marks the
one-year point of my using Emacs as my sole text editor, with some
exceptions (notably, I'm currently writing this blog post in the
browser). So I'd like to make some observations:

<li>
Either one of these editors (Vim or Emacs) is going to really suck
unless you are willing to make a serious investment in customizing them
and installing nice addons. For the second point, Emacs has an
advantage, because the philosophy of Vim is to be barebones whereas the
philosophy of Emacs is to be featureful, so that in particular many
things that were once addons of Emacs are now included in the standard
installation. For customization, on the one hand, Emacs is easier,
because it has a nice interface (`M-x customize`), but on the other
hand, Vim's scripting language is much easier to hack on than Emacs lisp
(I still can't code in Lisp to save my life; it's a very challenging
programming language).

But my point here is that neither has really great defaults. For
example, in Emacs, `M-space` is bound to `just-one-space`, which is
great for programming. What it does is remove all spaces around the
cursor, except for one. But to be really useful, it also should include
newlines. It doesn't do this by default. Rather, you have to call it
with a negative argument. So to be really useful, you have to add

[sourcecode]  
(defun just-one-space-with-newline ()  
"Call just-one-space with a negative argument"  
(interactive)  
(just-one-space -1))

(global-set-key (kbd "M-SPC") 'just-one-space-with-newline)  
[/sourcecode]

<p>
to your `.emacs` file.

</li>
<li>
Emacs has great features, but I always have to look them up. Or rather,
I have to look up the keyboard shortcuts for them. I only have the
keyboard shortcuts memorized for the things I do every day. I even ended
up forgetting really important ones, like `M-w` (Emacs version of copy).
And if a feature involves several keystrokes to access, forget about it
(for example, rectangular selection, or any features of special modes).
If I use a new mode, e.g., for some file type that I rarely edit (like
HTML), I might as well not have any of the features, other than the
syntax highlighting, because I either don't know what they are, or even
if I know that they should exist (like automatic tag completion for
html), I have no idea how to access them.

There's really something to be said about GUI editors, which give these
things to users in a way that they don't have to memorize anything.
Perhaps I should try to use the menu more. Or maybe authors of addons
should aim to make features require as little cognitive user interaction
as possible (such as the excellent [`auto-complete-mode`][] I mentioned
in [part 3][]).

<p>
I mention this because it is one of the things I complained about with
Vim, that the keybindings were too hard to memorize. Of course, the
difference with Vim is that one has to memorize keybindings to do even
the most basic of editing tasks, whereas with Emacs one can always fall
back to more natural things like `Shift-Arrow Key` to select text or
`Delete` to delete the character under the cursor (and yes, I know you
can rebind this stuff in Vim; I refer you to the previous bullet point).

</li>
<li>
I mentioned at the end of part 3 that Vim might still be useful to
learn, as vi is available literally anywhere that you have POSIX. I
honestly don't think I would be able to use vi or vim if I had to,
customization or no, unless I had my keyboard cheat sheet and a decent
amount of time. If I'm stuck on a barebones system and I can't do
anything about it, I'll use nano/pico before I use vi. It's not that I
hate vi. I just can't do anything with it. It is the same to me now as
it was before I used it in-depth. I have forgotten all the keyboard
shortcuts, except for `ESC` and `i`.

</li>
<li>
I don't use `emacsclient` any more. Ever since I got my new retina
MacBook Pro, I don't need it any more, because with the solid state
drive starting Emacs from scratch is instantaneous. I'm glad to get rid
of it, because it had some seriously annoying glitches.

</li>
<li>
Add `alias e=emacs` to your Bash config file (`.profile` or `.bashrc`).
It makes life much easier. "emacs" is not an easy word to type, at least
on QWERTY keyboards.

</li>
<li>
I still feel like I am not nearly as efficient in Emacs as I could be.
On the one hand, I know there are built-in features (like rectangular
selection) that I do not take advantage of enough. I have been a bit
lazy with customization: there are a handful of things that I do often
that require several keystrokes, but I still haven't created custom
keyboard shortcuts for (off the top of my head: copying and pasting
to/from the Mac OS X clipboard and rigidly indenting/dedenting a block
of text (`C-u 4 C-x TAB`, actually `C-c u 4 C-x TAB`, since I did the
sensible thing and rebound `C-u` to clear to the previous newline, and
bound `universal-argument` to `C-c u`) come to mind).

<p>
I feel as if I were to watch someone who has used Emacs for a long time
that I would learn a lot of tricks.

</li>
<li>
I really should learn Emacs lisp. There are a lot of little
customizations that I would like to make, but they are really niche, and
can only be done programmatically. But who has the time to learn a
completely new programming language (plus a whole library, as just
knowing Lisp is useless if you don't know the proper Emacs funtions and
variables and coding styles)?

</li>
<li>
I've still not found a good visual browser for jumping to function
definitions in a file (mostly Python function definitions, but also
other kinds of headers for other kinds of files). The best I've found is
`imenu`. If you know of anything, please let me know. One thing I really
liked about Vim was the [tag list][] extension, which did this perfectly
(thanks to commenter [Scott][] for pointing it out to me). I've been
told that Cedet has something like this, but every time I try to install
it, I run into some issues that just seem like way too much work (I
don't remember what they are, it won't compile or something, or maybe it
just wants to do just way too much and I can't figure out how to disable
everything except for the parts I want).

</li>
<li>
If you ever code in C, add the following to your Makefile

[code]  
check-syntax:  
\$(CC) -o nul \$(FLAGS) -S \$(CHK\_SOURCES)  
[/code]

(and if you don't use a Makefile, start using one now). This is assuming
you have `CC` and `FLAGS` defined at the top (generally to something
like `cc` and `-Wall`, respectively). Also, add the following to your
`.emacs`

[code]  
;; ===== Turn on flymake-mode ====

(add-hook 'c-mode-common-hook 'turn-on-flymake)  
(defun turn-on-flymake ()  
"Force flymake-mode on. For use in hooks."  
(interactive)  
(flymake-mode 1))

(add-hook 'c-mode-common-hook 'flymake-keyboard-shortcuts)  
(defun flymake-keyboard-shortcuts ()  
"Add keyboard shortcuts for flymake goto next/prev error."  
(interactive)  
(local-set-key "\\M-n" 'flymake-goto-next-error)  
(local-set-key "\\M-p" 'flymake-goto-prev-error))  
[/code]

<p>
The last part adds the useful keyboard shortcuts `M-n` and `M-p` to move
between errors. Now, errors in your C code will show up automatically as
you type. If you use the command line version of emacs like I do, and
not the GUI version, you'll also need to install the [flymake-cursor][]
module, which makes the errors show up in the mode line, since otherwise
it tries to use mouse popups. You can change the colors using
`M-x customize-face` (search for "flymake").

</li>
<li>
I never got flymake to work with LaTeX. Does anyone know how to do it?
It seems it is hardcoded to use MikTeX, the Windows version of LaTeX. I
found some stuff, but none of it worked.

<p>
Actually, what I really would like is not syntax checking (I rarely make
syntax mistakes in LaTeX any more), but rather something that
automatically builds the PDF constantly as I type. That way, I can just
look over at the PDF as I am writing (I use an external monitor for
this. I highly recommend it if you use LaTeX, especially one of those
monitors that swivels to portrait mode).

</li>
<li>
If you use Mac OS X, you can use the very excellent [KeyRemap4MacBook][]
program to make regular Mac OS X programs act more like Emacs. Mac OS X
already has many Emacs shortcuts built in (like `C-a`, `C-e`, etc.), but
that only works in Cocoa apps, and it doesn't include any meta key
shortcuts. This lets you use additional shortcuts literally everywhere
(don't worry, it automatically doesn't use them in the Terminal),
including an emulator for `C-space` and some `C-x` commands (like
`C-x C-s` to `Command-s`). It doesn't work on context sensitive
shortcuts, unfortunately, unless the operating system already supports
it with another keyboard shortcut (e.g., it can map `M-f` to
`Option-right arrow`). For example, it can't enable moving between
paragraphs with `C-S-{` and `C-S-}`. If anyone knows how to do that, let
me know.

</li>
<li>
For about a month this summer, I had to use a Linux laptop, because my
Mac broke and my new Mac took a month to arrive (the downside to
ordering a new computer immediately after it is announced by Apple). At
this point, my saving of all my customizations to
[GitHub][KeyRemap4MacBook] really helped a lot. I created a new branch
for the Linux computer (because several things in my customizations were
Mac specific), and just symlinked the files I wanted. A hint I can give
to people using Linux is to use Konsole. The Gnome terminal sucks. One
thing I never figured out is how to make Konsole (or any other Terminal
for that matter) to send Control-Shift shortcuts to Emacs (see
http://superuser.com/q/439961/39697). I don't use Linux any more at the
moment, but if anyone knows what was going on there, add an answer to
that question.

</li>
<li>
In [part 3][] mentioned that [predictive mode][] was cool, but not very
useful. What it does is basically add tab completion for every word in
the English language. Actually, I've found using auto-complete-mode even
when editing text (or LaTeX) to be very useful. Unlike predictive mode,
it only guesses words that you've already typed (it turns out that you
tend to type the same words over and over, and doubly so if those words
are LaTeX math commands). Also, predictive mode has a set order of
words, which supposedly helps to use it with muscle memory, whereas
auto-complete-mode tries to learn what words you are more likely to use
based on some basic statistical machine-learning. Also,
auto-complete-mode has a much better visual UI and smarter defaults than
predictive mode. The result is that it's actually quite useful and makes
typing plain text, as well as LaTeX (actually, pretty much anything, as
long as you tend to use the same words repeatedly) much faster. I
recommend enabling auto-complete-mode almost everywhere using hooks,
like

[code]  
(add-hook 'latex-mode-hook 'auto-complete-mode)  
(add-hook 'LaTeX-mode-hook 'auto-complete-mode)  
(add-hook 'prog-mode-hook 'auto-complete-mode)  
;; etc.  
[/code]

</li>
<li>
At the end of the day, I'm pretty happy with Emacs. I've managed to fix
most of the things that make it annoying, and it is orders of magnitude
more powerful than any GUI editor or IDE I've ever seen, especially at
just basic text editing, which is the most important thing (I can always
use another program for other things, like debugging or whatever). The
editor uses the basic shortcuts that I am used to, and is quite
efficient to write in. Extensions like auto-complete-mode make using it
much faster, though I could use some more extensions to make it even
better (namely, a better isearch and a better imenu). Regarding Vim vs.
Emacs, I'd like to quote something I said back in my [first blog post][]
about Vim over a year ago:  

> Vim is great for text *editing*, but not so hot for text *writing*
> (unless you always write text perfectly, so that you never need to
> leave insert mode until you are done typing). Just the simple act of
> deleting a mistyped word (yes, word, that happens a lot when you are
> decently fast touch typist) takes several keystrokes, when it should
> in my opinion only take one (two if you count the meta-key).

<p>
Needless to say, I find Emacs to be great for both text editing and text
writing.

</li>

  [1]: http://asmeurersympy.wordpress.com/2011/12/20/vim-vs-emacs-part-1/
    "1"
  [2]: http://asmeurersympy.wordpress.com/2012/01/03/vim-vs-emacs-part-2/
    "2"
  [3]: http://asmeurersympy.wordpress.com/2012/01/13/vim-vs-emacs-part-3/
    "3"
  [7 months later follow up]: http://asmeurersympy.wordpress.com/2012/07/09/emacs-7-months-later/
    "7 months later follow up"
  [`auto-complete-mode`]: http://cx4a.org/software/auto-complete/manual.html
  [part 3]: http://asmeurersympy.wordpress.com/2012/01/13/vim-vs-emacs-part-3/
  [tag list]: http://www.vim.org/scripts/script.php?script_id=273
  [Scott]: http://asmeurersympy.wordpress.com/2011/12/20/vim-vs-emacs-part-1/#comment-424
  [flymake-cursor]: http://www.emacswiki.org/emacs/flymake-cursor.el
  [KeyRemap4MacBook]: http://pqrs.org/macosx/keyremap4macbook/
  [predictive mode]: http://www.dr-qubit.org/predictive/predictive-user-manual/html/index.php
  [first blog post]: http://asmeurersympy.wordpress.com/2011/12/20/vim-vs-emacs-part-1
