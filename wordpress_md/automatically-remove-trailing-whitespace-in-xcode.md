Title: Automatically Remove Trailing Whitespace in XCode
Date: 2009-12-29 23:56
Author: asmeurer
Category: Uncategorized
Slug: automatically-remove-trailing-whitespace-in-xcode

I like XCode, and I use it to edit all of my source for SymPy. But, like
many editors, it likes to auto-indent new lines to the level of
indentation of the previous line. This is a useful feature, but it makes
for training whitespace out the wazoo, since blank lines will be
indented in. I am constantly finding myself using SymPy's
strip\_whitespace script to clean up my files.

This bugged me enough that I Googled a solution, and found [this][]. It
is a simple XCode plugin that, among other things, adds an option to
strip trailing whitespace on save. Just install in the PlugIns folder in
the XCode package and enable the option in the new Google pane of the
XCode preferences.

  [this]: http://code.google.com/p/google-toolbox-for-mac/wiki/GTMXcodePlugin
