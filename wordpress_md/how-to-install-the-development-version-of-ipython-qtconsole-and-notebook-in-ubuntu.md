Title: How to install the development version of IPython Qtconsole and Notebook in Ubuntu
Date: 2012-06-14 05:49
Author: asmeurer
Category: Uncategorized
Slug: how-to-install-the-development-version-of-ipython-qtconsole-and-notebook-in-ubuntu

Both the awesome [IPython notebook][] and [Qtconsole][] are in the
Ubuntu repositories, so if you just want to use the stable released
versions, you can just do

[code language="bash"]  
sudo apt-get install ipython-notebook ipython-qtconsole  
[/code]

and be on your way. But the git development version has a lot of cool
new features, and you may not want to wait for 0.13 to be released and
make its way to the Ubuntu repos. But you may be thinking that to use
those you will have to figure out all the dependencies yourself.
Actually, it's pretty easy:

[code language="bash"]  
\# First install git, if you don't already have it  
sudo apt-get install git  
\# Then, clone the IPython repo, if you haven't already.  
git clone git://github.com/ipython/ipython.git  
cd ipython  
\# Now just install IPython with apt, then uninstall it. The
dependencies will remain  
sudo apt-get install ipython-notebook ipython-qtconsole  
sudo apt-get remove ipython-notebook ipython -qtconsole ipython  
\# Now install the IPython git version in such a way that will keep up
to date when you pull  
sudo python setup.py develop  
[/code]

To update, just cd into that ipython directory and type `git pull`.
That's it. Now type `ipython notebook` or `ipython qtconsole` to get the
magic.

EDIT: After you do this, `apt-get` will start bugging you every time
that you use it that a bunch of packages are no longer needed. These are
the ones that you do need for the qtconsole and the notebook, so you
should not autoremove them as it says. Rather, set them as manually
installed by copying the list of packages that it tells you about and
`sudo apt-get install`ing them.

  [IPython notebook]: http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html
  [Qtconsole]: http://ipython.org/ipython-doc/stable/interactive/qtconsole.html
