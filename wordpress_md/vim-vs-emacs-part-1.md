Title: Vim vs. Emacs (Part 1)
Date: 2011-12-20 08:17
Author: asmeurer
Category: Uncategorized
Slug: vim-vs-emacs-part-1

So about a month or so ago, I decided that I needed to start learning a
command line text editor. XCode, the editor I had been using for Python
files, didn't work very well with the new version (in particular, the
[essential plugin][] that I'd been using to clear trailing whitespace on
save doesn't yet work in XCode 4). I'd been using TextWrangler for other
things, and started to switch to it for Python editing too. As far as
free GUI text editors on the Mac go, TextWrangler is the best.

But I'd seen some of the nice features that vim has, like automatically
keeping all lines under 80 characters, on a friend's computer, and I
decided that I should try it.

Now, I had had a little prior experience with both vim and emacs, but
all that I remembered was for vim that `i` inserts and `ZZ` quits (for
when I accidentally open it) and for emacs, that `M-X doctor` starts the
psychiatrist.

So I've decided to try them out, doing it cold turkey. To make sure that
I choose the better one, I've decided to try both. So, starting about a
week ago, I've been using nothing but vim for all my text editing.
Starting in January, I will try using emacs, and after two weeks, I will
see what I like better.

My opinions so far on vim:

<li>
The tutorials suck. The best tutorial is `vimtutor` (type that in the
command line), which I think comes with vim. It's not bad, but it leaves
out a few things that I would consider to be essential to a tutorial,
for example, how to scroll (answer: use CTRL-D and CTRL-U). I started
the emacs tutorial a while back, and while I never finished it, from
what I remember, it was much better (and I also remember that the first
thing it talked about was how to scroll by more than one line at a
time). It also left out the `.` command, which I think is rather useful.
I did print out [this cheatsheet][] and have it sitting next to me on my
desk. That has helped a lot. I hope I can find something similar for
emacs when I get to it.

</li>
<li>
vim is too line oriented. vi started out as an extension to ed, the line
editor, so this is not surprising. But I still can't understand why
pressing `l` at the end of a line can't bring me to the beginning of the
next line. Maybe I'm just still doing it wrong (supposedly, you should
rarely use `h` and `l` over more efficient moving commands).

</li>
<li>
Somewhat related to the last point, vim really likes to ring the
terminal bell a lot. To quote [Wikipedia][], "vi has two modes – 'beep
repeatedly' and 'break everything'"

</li>
<li>
I managed to customize it to the point of usability (there are still
several things I need to go in and figure out how to fix). See
https://github.com/asmeurer/dotfiles for my .vimrc and .vim/ files. I
found a decent Python syntax file, but it's actually not that great. I
modified it to color single quoted strings different from double quoted
strings (a feature I missed from Xcode). I still need to make a better
color scheme (preferably the same as Xcode's midnight), but this is
enough work that I've put it off.

</li>
<li>
Pressing ESC all the time is really annoying. Sometimes, I just arrow
over, even though I know you're not "supposed to", just because my
fingers don't want to reach over and press ESC. I'm also really used to
using control sequences to move around while typing, which of course
doesn't work in vim. In fact, so far, I'm suspecting that I'll like
emacs better. But I've vowed to give both a fair chance. But so far, my
impression is that vim is a great for text *editing*, but not so hot for
text *writing* (unless you always write text perfectly, so that you
never need to leave insert mode until you are done typing). Just the
simple act of deleting a mistyped word (yes, word, that happens a lot
when you are decently fast touch typist) takes several keystrokes, when
it should in my opinion only take one (two if you count the meta-key).

</li>
<li>
The customizability is really nice. So far, everything that I've thought
of to change has been changeable. Also, language is easy enough to
understand that I was able to modify the Python syntax file without any
difficulty.

</li>
<li>
I like how it syntax highlights virtually everything I throw at it.

</li>
If there are any vim experts out there reading this, I have some
questions:

<li>
Is there an easy way to get a list of and jump to a function/class
definition in a Python file? In Xcode and TextWrangler, there was a nice
popup at the top of the window that I could access these from. In vim,
so far the best I've found is searching for it, which isn't very
efficient.

</li>
<li>
I got TAB to indent 4 spaces in Python, but for some reason, when I
create a new line after a `:`, it puts 8 extra spaces. I wouldn't be
surprised if this is the result of some mismatch/error in [my .vimrc or
.vim/ files][], but I don't know how to fix it

</li>
<li>
Any useful tricks to share? Especially for editing Python files.

</li>
<li>
How long did it take you to become reasonably efficient with vim?

</li>
**EDIT: I thought of some more questions:**

<li>
Is there a way to make vim consider camelCase to be word boundaries?

</li>
Finally, if anyone else is thinking of starting vim, I have some useful
things I've already found in my .vimrc. So you might take a look at
that, and add the ones that you like to your .vimrc. Finally, if you are
on Mac OS X, you should use [iTerm2][]. Actually, you should use this
regardless of what text editor you use. It's a very good Terminal.app
replacement that has virtually all the features (with a couple of
exceptions) as Terminal.app, and a ton of extra ones. The one I want to
mention here is mouse reporting support, so you can use your mouse to do
things in vim. This is very useful, as sometimes, e.g., when selecting
text, using the mouse is just more efficient. Also, if you get
frustrated trying to remember the commands that will move around you
faster than `h`, `j`, `k`, and `l`, you can just click on where you want
to go.

:wq

  [essential plugin]: http://asmeurersympy.wordpress.com/2009/12/29/automatically-remove-trailing-whitespace-in-xcode/
  [this cheatsheet]: http://www.viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html
  [Wikipedia]: http://en.wikipedia.org/wiki/Editor_war
  [my .vimrc or .vim/ files]: https://github.com/asmeurer/dotfiles
  [iTerm2]: http://www.iterm2.com/#/section/home
