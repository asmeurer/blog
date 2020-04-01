So I've finally decided to move my blog from Wordpress to GitHub pages.  I
highly recommend it if you are technically skilled enough to do it. I was
getting pretty annoyed at Wordpress. It forces you to write your posts in
html (or else using their WYSIWYG editor), the wordpress.com is locked down,
so you can't add any Javascript, their math is stuck in the past rendering png
instead of using MathJax. The list goes on.

With GitHub pages, I can write my posts in Markdown, and I have full control
over everything. And there is no lock in. If I decide I don't like the
software that is generating the posts, I can easily move to something else,
since the post content itself is all Markdown (or the occasional rst or
IPython notebook if I want to do something that Markdown doesn't support). I
can use MathJax for math (like $ e^{i\pi} + 1 = 0 $). Wordpress.com
doesn't let you install abtirary Javascript on your blog, so you can't do
things like install MathJax or enable some cool sidebar thing (like a Twitter
feed).

# Setting up GitHub Pages

First, you need to set up GitHub pages. This is a bit confusing, because there
are actually two kinds of GitHub pages, user pages and project pages. User
pages are if you have a repo named `username.github.io` (or `.com`). The pages
are served from the `master` branch.

For project pages, you add a `gh-pages` branch to any one of your projects,
and GitHub hosts the content automatically at
`username.github.io/projectname`. I originally had my blog content at
`asmeurer.github.io`, but I didn't like that I had to do everything in master,
both the generated and original content. So instead I created a repo called
`blog`. I have my content in the `master` branch and the generated pages in
the `gh-pages` branch (more on this later). At my
[`asmeurer.github.com`](https://github.com/asmeurer/asmeurer.github.com) repo,
I just have for now a basic redirect to the blog. In the future, I may want to
put additional, non-blog content on the website, and it would go there (or in
a separate project repo with its own `gh-pages` branch).

# Nikola

I had initially planned on using
[Pelican](http://blog.getpelican.com/). However, I got stalled on the
Wordpress import. I like that Pelican is written in Python, but I was not too
keen on their abrasive
[license](https://github.com/getpelican/pelican/blob/master/LICENSE). Frankly,
I shouldn't say too many bad things about Pelican because I never really tried
that hard with it.

I have decided to try [Nikola](http://getnikola.com/) instead. It's also
written in Python. It has a very nice
[license](https://github.com/getnikola/nikola/blob/master/LICENSE.txt). I like
the philosophy of the [manual](http://getnikola.com/handbook.html):

> DON'T READ THIS MANUAL. IF YOU NEED TO READ IT I FAILED, JUST USE THE THING.

I've also discovered that the
[Nikola community](https://groups.google.com/forum/#!forum/nikola-discuss) is
*very* nice. And of course, even if Nikola ends up not being for me, it will
be easy to switch, because my actual content is just some Markdown files that
I own.

## Getting started

Getting started with Nikola is pretty easy. First, you need to install it. It
has a *ton* of dependencies (fortunately all Python, so it won't be that
hard). In addition to the ones in the requirements.txt, you should also
install `markdown` and `webassets`. While using `nikola`, it will tell you if
you don't have something installed that you should, so if you see that, just
install what it tells you to.  If you use `conda` and Mac OS X, I have
uploaded all the dependencies to my [Binstar](https://binstar.org/asmeurer/),
so you can just `conda install -c asmeurer nikola`. Oh and don't worry, Nikola
and its dependencies fully support Python 3 (I wouldn't be using it if they
didn't).

Then you just run the commands from
http://getnikola.com/handbook.html#all-you-need-to-know.

One thing that doesn't tell you is that after you init the site, you should
walk through `conf.py` and change the settings to your liking.

Another trick not there is that you can add

```bash
eval "`nikola tabcompletion`"
```

to your Bash profile to get tab completion.

## Tricks

Here are some useful tricks:

- To enable MathJax, you have to type `mathjax` in a line by itself in the
metadata file. There are some bugs right now, but ideally you could do inline
math with `$math$` and display math with `$$math$$`. `$math$` doesn't work
currently, but you can do `\\(math\\)` (both `\`s are required, although this
is likely a bug). You can do `\\[math\\]` for display math.  Here are some
examples. Inline: $ \sin ^2{x} + \cos^2{x} = 1$. Display: $$ e^{i\pi} + 1 = 0 .$$

- Your one-stop command when blogging is `nikola auto`. This requires
  `livereload`. This will serve the blog on localhost, and automatically
  rebuild it when any change is made (and I really mean *any* change: it can
  even detect when you change Nikola itself).

- I have the following in my conf.py to deploy:

```python
DEPLOY_COMMANDS = [
    "git checkout gh-pages",
    "rsync -rPv --delete-after --exclude old_blog --exclude .git --exclude .gitignore --exclude cache/ --exclude .doit.db.db output/ .",
    "git add -A",
    "git commit -a -m 'Updating blog content'",
    "git push",
    "git checkout master",
]
```

WARNING: These commands are dangerous. If you don't properly exclude things
like `.git`, you will wipe your entire git history. I *highly* recommend
committing everything and pushing to GitHub before deploying.

- Use

```
_site/
*.pyc
.DS_Store
.doit.db.db
cache/
output/
```

for your `.gitignore`.

- Despite what it says on the Nikola page, be sure to read the docs, because
there are a lot of cool features you won't know about unless you read about
them. Also be sure to read through `conf.py`.

## Wordpress import

**This is something that I am still figuring out. You can see the progress at
  [http://asmeurer.github.io/blog/old_blog](http://asmeurer.github.io/blog/old_blog)**

Importing from Wordpress is pretty easy actually (at least in theory). First
you need to go to the Wordpress site dashboard and go to "Export" from the
"Tools" menu. From here you can download an XML file with all your
content. Then just do

```
nikola import_wordpress export_file.xml
```

Note that the current version of Nikola as of this writing (6.3.0) doesn't do
this right, so you'll need to use the
[git master](https://github.com/getnikola/nikola). There are some issues with
the import, since Wordpress has its own markup that it doesn't know everything
about, so you may need to go in and fix things. Or report them as bugs to
Nikola and reimport when they are fixed.

You'll need to go through the posts and make sure that they are rendered
correctly (this is one reason I haven't finished doing it yet).

For comments, you first need to create a Disqus account, and enable it in your
conf.py. You should then upload the xml file that you exported from Wordpress
to Disqus. At this point, the comments should just work, because Nikola sets
the Disqus url for the imported comments to the old Wordpress url (look at the
Disqus section of one of the built pages).

I don't know how to automatically backlink from Wordpress back to
Nikola. Maybe I should just automatically generate some links and paste them
in manually.
