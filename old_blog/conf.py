# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

# Configuration, please edit

# Data about this site
BLOG_AUTHOR = "Aaron Meurer"
BLOG_TITLE = "Aaron Meurer's SymPy Blog"
# This is the main URL for your site. It will be used
# in a prominent link
SITE_URL = "http://asmeurersympy.wordpress.com/"
# This is the URL where nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "http://asmeurersympy.wordpress.com/"
BLOG_EMAIL = "asmeurer@gmail.com"
BLOG_DESCRIPTION = "My blog on my work on SymPy and other fun stuff."

# Nikola is multilingual!
#
# Currently supported languages are:
# bg     Bulgarian
# ca     Catalan
# cs     Czech [ALTERNATIVELY cz]
# de     German
# el     Greek [NOT gr!]
# en     English
# eo     Esperanto
# es     Spanish
# et     Estonian
# eu     Basque
# fa     Persian
# fi     Finnish
# fr     French
# hi     Hindi
# hr     Croatian
# it     Italian
# ja     Japanese [NOT jp!]
# nb     Norwegian Bokmål
# nl     Dutch
# pt_br  Portuguese (Brasil)
# pl     Polish
# ru     Russian
# sl     Slovenian [NOT sl_si!]
# tr     Turkish (Turkey) [NOT tr_tr!]
# ur     Urdu
# zh_cn  Chinese (Simplified)
#
# If you want to use Nikola with a non-supported language you have to provide
# a module containing the necessary translations
# (cf. the modules at nikola/data/themes/base/messages/fr.py).
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.

# What is the default language?
DEFAULT_LANG = "en"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# What will translated input files be named like?

# If you have a page something.rst, then something.rst.pl will be considered
# its Polish translation.
#     (in the above example: path == "something", lang == "pl", ext == "rst")
# this pattern is also used for metadata:
#     something.meta -> something.meta.pl

TRANSLATIONS_PATTERN = "{path}.{ext}.{lang}"

# If you don't want your Polish files to be considered Perl code, use this:
# TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"
#     Note that this pattern will become the default in v7.0.0.

# Links for the sidebar / navigation bar.
# You should provide a key-value pair for each used language.
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/archive.html', 'Archives'),
        ('/categories/index.html', 'Tags'),
        ('/rss.xml', 'RSS'),
    ),
}

# Below this point, everything is optional

# While nikola can select a sensible locale for each language,
# sometimes explicit control can come handy.
# In this file we express locales in the string form that
# python's locales will accept in your OS, by example
# "en_US.utf8" in unix-like OS, "English_United States" in Windows.
# LOCALES = dict mapping language --> explicit locale for the languages
# in TRANSLATIONS. You can ommit one or more keys.
# LOCALE_FALLBACK = locale to use when an explicit locale is unavailable
# LOCALE_DEFAULT = locale to use for languages not mentioned in LOCALES; if
# not set the default Nikola mapping is used.

# POSTS and PAGES contains (wildcard, destination, template) tuples.
#
# The wildcard is used to generate a list of reSt source files
# (whatever/thing.txt).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and optionally translated files (example for spanish, with code "es"):
#     whatever/thing.txt.es and whatever/thing.meta.es
#
#     This assumes you use the default TRANSLATIONS_PATTERN.
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combinated with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds and are considered part of a blog, while PAGES are
# just independent HTML pages.
#

POSTS = (
            ("posts/*.wp", "posts", "post.tmpl"),
        )
PAGES = (
            ("stories/*.wp", "stories", "story.tmpl"),
        )

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of "source" "relative destination".
# Default is:
# FILES_FOLDERS = {'files': '' }
# Which means copy 'files' into 'output'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is html and just copies it
COMPILERS = {
        "rest": ('.txt', '.rst'),
        "markdown": ('.md', '.mdown', '.markdown', '.wp'),
        "html": ('.html', '.htm')
        }


# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# If this is set to True, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# If set to False, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# HIDE_UNTRANSLATED_POSTS = False

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
# TAG_PATH = "categories"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = True

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# INDEX_PATH = ""

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
# CREATE_SINGLE_ARCHIVE = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# Number of posts in RSS feeds
# FEED_LENGTH = 10

# Slug the Tag URL easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = [('2011/07/30/sympy-0-7-1-released/index.html', '//posts/2011/07/30/sympy-0-7-1-released.html'), ('2011/03/18/sympy-is-a-google-summer-of-code-2011-mentoring-organization/index.html', '//posts/2011/03/18/sympy-is-a-google-summer-of-code-2011-mentoring-organization.html'), ('2012/09/19/infinitely-nested-lists-in-python/index.html', '//posts/2012/09/19/infinitely-nested-lists-in-python.html'), ('2011/07/25/merging-integration3-with-sympy-0-7-0-nightmare/index.html', '//posts/2011/07/25/merging-integration3-with-sympy-0-7-0-nightmare.html'), ('2010/06/15/a-weeklog/index.html', '//posts/2010/06/15/a-weeklog.html'), ('2009/07/20/modifying-a-list-while-looping-through-it-in-python/index.html', '//posts/2009/07/20/modifying-a-list-while-looping-through-it-in-python.html'), ('2010/06/26/quick-update/index.html', '//posts/2010/06/26/quick-update.html'), ('2011/12/20/vim-vs-emacs-part-1/index.html', '//posts/2011/12/20/vim-vs-emacs-part-1.html'), ('2009/04/26/git-tutorial/index.html', '//posts/2009/04/26/git-tutorial.html'), ('2009/06/13/vacation/index.html', '//posts/2009/06/13/vacation.html'), ('2013/08/22/python-3-single-codebase-vs-2to3/index.html', '//posts/2013/08/22/python-3-single-codebase-vs-2to3.html'), ('2010/04/06/latest-sympy-makes-it-to-fink/index.html', '//posts/2010/04/06/latest-sympy-makes-it-to-fink.html'), ('2011/08/08/hacking-pudb-now-an-even-better-python-debugger/index.html', '//posts/2011/08/08/hacking-pudb-now-an-even-better-python-debugger.html'), ('2009/07/06/update/index.html', '//posts/2009/07/06/update.html'), ('2009/07/16/constant-stuff/index.html', '//posts/2009/07/16/constant-stuff.html'), ('2011/06/29/sympy-0-7-0-released/index.html', '//posts/2011/06/29/sympy-0-7-0-released.html'), ('2009/08/12/testing-implicit-solutions-to-odes/index.html', '//posts/2009/08/12/testing-implicit-solutions-to-odes.html'), ('2010/06/30/the-risch-algorithm-part-1/index.html', '//posts/2010/06/30/the-risch-algorithm-part-1.html'), ('2011/01/02/2010-in-review/index.html', '//posts/2011/01/02/2010-in-review.html'), ('2010/07/12/integration-of-exponential-functions/index.html', '//posts/2010/07/12/integration-of-exponential-functions.html'), ('2010/05/26/more-information-on-my-google-summer-of-code-project-this-year/index.html', '//posts/2010/05/26/more-information-on-my-google-summer-of-code-project-this-year.html'), ('2009/05/31/first-order-differential-equations-with-homogeneous-coefficients/index.html', '//posts/2009/05/31/first-order-differential-equations-with-homogeneous-coefficients.html'), ('2010/06/11/integration-of-rational-functions/index.html', '//posts/2010/06/11/integration-of-rational-functions.html'), ('2009/05/25/one-problem-solved/index.html', '//posts/2009/05/25/one-problem-solved.html'), ('2011/08/18/sqrtx-now-prints-as-sqrtx/index.html', '//posts/2011/08/18/sqrtx-now-prints-as-sqrtx.html'), ('2013/08/09/using-python-3-as-my-default-python/index.html', '//posts/2013/08/09/using-python-3-as-my-default-python.html'), ('2011/06/13/sympy-0-7-0-rc1-is-out/index.html', '//posts/2011/06/13/sympy-0-7-0-rc1-is-out.html'), ('2011/05/26/update-for-the-beginning-of-the-summer/index.html', '//posts/2011/05/26/update-for-the-beginning-of-the-summer.html'), ('2013/01/28/tip-for-debugging-sympy-with-pudb/index.html', '//posts/2013/01/28/tip-for-debugging-sympy-with-pudb.html'), ('2009/09/07/google-summer-of-code-2009-wrap-up/index.html', '//posts/2009/09/07/google-summer-of-code-2009-wrap-up.html'), ('2009/08/17/undetermined-coefficients/index.html', '//posts/2009/08/17/undetermined-coefficients.html'), ('2009/06/22/how-to-permanently-lose-data-with-git-and-then-retrieve-it-again/index.html', '//posts/2009/06/22/how-to-permanently-lose-data-with-git-and-then-retrieve-it-again.html'), ('2012/06/14/how-to-install-the-development-version-of-ipython-qtconsole-and-notebook-in-ubuntu/index.html', '//posts/2012/06/14/how-to-install-the-development-version-of-ipython-qtconsole-and-notebook-in-ubuntu.html'), ('2011/04/27/advice-for-future-prospective-gsoc-students/index.html', '//posts/2011/04/27/advice-for-future-prospective-gsoc-students.html'), ('2013/07/02/scipy-2013/index.html', '//posts/2013/07/02/scipy-2013.html'), ('2009/04/22/first-post/index.html', '//posts/2009/04/22/first-post.html'), ('2013/03/03/when-does-xlogy-ylogx/index.html', '//posts/2013/03/03/when-does-xlogy-ylogx.html'), ('2009/12/29/automatically-remove-trailing-whitespace-in-xcode/index.html', '//posts/2009/12/29/automatically-remove-trailing-whitespace-in-xcode.html'), ('2011/07/17/the-scipy-2011-conference/index.html', '//posts/2011/07/17/the-scipy-2011-conference.html'), ('2009/08/17/los-alamos-sprint/index.html', '//posts/2009/08/17/los-alamos-sprint.html'), ('2011/03/15/true-is-true-is-false-is-true-is-false/index.html', '//posts/2011/03/15/true-is-true-is-false-is-true-is-false.html'), ('2009/05/31/separable-next/index.html', '//posts/2009/05/31/separable-next.html'), ('2013/04/06/how-to-make-attributes-un-inheritable-in-python-using-descriptors/index.html', '//posts/2013/04/06/how-to-make-attributes-un-inheritable-in-python-using-descriptors.html'), ('2011/04/27/accepted-gsoc-students-announced/index.html', '//posts/2011/04/27/accepted-gsoc-students-announced.html'), ('2012/01/03/vim-vs-emacs-part-2/index.html', '//posts/2012/01/03/vim-vs-emacs-part-2.html'), ('2010/06/16/strange-python-behavior-can-someone-please-explain-to-me-what-is-going-on-here/index.html', '//posts/2010/06/16/strange-python-behavior-can-someone-please-explain-to-me-what-is-going-on-here.html'), ('2013/01/01/emacs-one-year-later/index.html', '//posts/2013/01/01/emacs-one-year-later.html'), ('2009/08/01/variation-of-parameters-and-more/index.html', '//posts/2009/08/01/variation-of-parameters-and-more.html'), ('2010/07/31/integration-of-primitive-functions/index.html', '//posts/2010/07/31/integration-of-primitive-functions.html'), ('2011/06/17/fixing-bugs-in-the-release-candidate/index.html', '//posts/2011/06/17/fixing-bugs-in-the-release-candidate.html'), ('2010/04/26/gsoc-2010/index.html', '//posts/2010/04/26/gsoc-2010.html'), ('2010/07/17/a-hard-week/index.html', '//posts/2010/07/17/a-hard-week.html'), ('2011/01/09/i-am-now-the-sympy-project-leader/index.html', '//posts/2011/01/09/i-am-now-the-sympy-project-leader.html'), ('2009/05/08/my-gsoc-proposal/index.html', '//posts/2009/05/08/my-gsoc-proposal.html'), ('2011/06/24/import_module-the-hopefully-last-fix-for-0-7-0/index.html', '//posts/2011/06/24/import_module-the-hopefully-last-fix-for-0-7-0.html'), ('2010/06/04/pudb-a-better-python-debugger/index.html', '//posts/2010/06/04/pudb-a-better-python-debugger.html'), ('2009/05/25/patch-problems-and-updates/index.html', '//posts/2009/05/25/patch-problems-and-updates.html'), ('2010/08/14/the-risch-algorithm-part-3-liouvilles-theorem/index.html', '//posts/2010/08/14/the-risch-algorithm-part-3-liouvilles-theorem.html'), ('2010/06/04/update-for-this-week/index.html', '//posts/2010/06/04/update-for-this-week.html'), ('2009/08/10/homogeneous-coefficients-corner-case/index.html', '//posts/2009/08/10/homogeneous-coefficients-corner-case.html'), ('2009/06/21/refactoring-expand/index.html', '//posts/2009/06/21/refactoring-expand.html'), ('2013/07/07/automating-the-sympy-release-process/index.html', '//posts/2013/07/07/automating-the-sympy-release-process.html'), ('2012/01/01/2011-in-review/index.html', '//posts/2012/01/01/2011-in-review.html'), ('2009/06/05/git-stash/index.html', '//posts/2009/06/05/git-stash.html'), ('about/index.html', '//stories/about.html'), ('2012/08/21/sympy-live-sphinx-extension/index.html', '//posts/2012/08/21/sympy-live-sphinx-extension.html'), ('2010/08/05/prototype-risch_integrate-function-ready-for-testing/index.html', '//posts/2010/08/05/prototype-risch_integrate-function-ready-for-testing.html'), ('2009/05/30/just-finished-a-new-bit/index.html', '//posts/2009/05/30/just-finished-a-new-bit.html'), ('2010/12/27/major-api-change-for-the-risch-algorithm-functions/index.html', '//posts/2010/12/27/major-api-change-for-the-risch-algorithm-functions.html'), ('2010/07/24/the-risch-algorithm-part-2-elementary-functions/index.html', '//posts/2010/07/24/the-risch-algorithm-part-2-elementary-functions.html'), ('2009/07/13/meeting-ondrej-in-los-alamos/index.html', '//posts/2009/07/13/meeting-ondrej-in-los-alamos.html'), ('2012/12/30/2012-in-review/index.html', '//posts/2012/12/30/2012-in-review.html'), ('2012/01/13/vim-vs-emacs-part-3/index.html', '//posts/2012/01/13/vim-vs-emacs-part-3.html'), ('2011/06/05/nondeterminism/index.html', '//posts/2011/06/05/nondeterminism.html'), ('2012/08/31/isympy-i-a-saner-interactive-environment/index.html', '//posts/2012/08/31/isympy-i-a-saner-interactive-environment.html'), ('2009/11/13/how-to-get-both-32-bit/index.html', '//posts/2009/11/13/how-to-get-both-32-bit.html'), ('2012/07/09/emacs-7-months-later/index.html', '//posts/2012/07/09/emacs-7-months-later.html'), ('2009/05/16/work-started-exact-differential-equations/index.html', '//posts/2009/05/16/work-started-exact-differential-equations.html')]

# Commands to execute to deploy. Can be anything, for example,
# you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola install_plugin ping`).
# To do manual deployment, set it to []
# DEPLOY_COMMANDS = []

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, there are no filters.
#
# Many filters are shipped with Nikola.  A list is available in the manual:
# <http://getnikola.com/handbook.html#post-processing-filters>
# FILTERS = {
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# Compiler to process LESS files.
# LESS_COMPILER = 'lessc'

# Compiler to process Sass files.
# SASS_COMPILER = 'sass'

# #############################################################################
# Image Gallery Options
# #############################################################################

# Galleries are folders in galleries/
# Final location of galleries will be output / GALLERY_PATH / gallery_name
# GALLERY_PATH = "galleries"
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []
#
# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to 'old posts, page %d' or 'page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
# INDEXES_TITLE = ""         # If this is empty, defaults to BLOG_TITLE
# INDEXES_PAGES = ""         # If this is empty, defaults to '[old posts,] page %d' (see above)
# INDEXES_PAGES_MAIN = False # If True, INDEXES_PAGES is also displayed on
                             # the main (the newest) index page (index.html)

# Name of the theme to use.
THEME = "bootstrap3"

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of autumn borland bw colorful default emacs friendly fruity manni
# monokai murphy native pastie perldoc rrt tango trac vim vs
# CODE_COLOR_SCHEME = 'default'

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONFIG_SUBTHEME = 'sky'
# You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions
# between the slides
# THEME_REVEAL_CONFIG_TRANSITION = 'cube'
# You can also use: page/concave/linear/none/default

# date format used to display post dates.
# (str used by datetime.datetime.strftime)
# DATE_FORMAT = '%Y-%m-%d %H:%M'

# FAVICONS contains (name, file, size) tuples.
# Used for create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# For creating favicons, take a look at:
# http://www.netmagazine.com/features/create-perfect-favicon
# FAVICONS = {
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# }

# Show only teasers in the index pages? Defaults to False.
# INDEX_TEASERS = False

# A HTML fragment with the Read more... link.
# The following tags exist and are replaced for you:
# {link}        A link to the full post page.
# {read_more}   The string “Read more” in the current language.
# {{            A literal { (U+007B LEFT CURLY BRACKET)
# }}            A literal } (U+007D RIGHT CURLY BRACKET)
# READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'

# A HTML fragment describing the license, for the sidebar.
LICENSE = ""
# I recommend using the Creative Commons' wizard:
# http://creativecommons.org/choose/
# LICENSE = """
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/2.5/ar/">
# <img alt="Creative Commons License BY-NC-SA"
# style="border-width:0; margin-bottom:12px;"
# src="http://i.creativecommons.org/l/by-nc-sa/2.5/ar/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
# Default is ''
CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="http://getnikola.com" rel="nofollow">Nikola</a>         {license}'
CONTENT_FOOTER = CONTENT_FOOTER.format(email=BLOG_EMAIL,
                                       author=BLOG_AUTHOR,
                                       date=time.gmtime().tm_year,
                                       license=LICENSE)

# To use comments, you can choose between different third party comment
# systems, one of "disqus", "livefyre", "intensedebate", "moot",
#                 "googleplus", "facebook" or "isso"
# COMMENT_SYSTEM = "disqus"
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
# COMMENT_SYSTEM_ID = "nikolademo"

# Enable annotations using annotateit.org?
# If set to False, you can still enable them for individual posts and pages
# setting the "annotations" metadata.
# If set to True, you can disable them for individual posts and pages using
# the "noannotations" metadata.
# ANNOTATIONS = False

# Create index.html for story folders?
# STORY_INDEX = False
# Enable comments on story pages?
# COMMENTS_IN_STORIES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
# INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
# (Note: This was briefly STRIP_INDEX_HTML in v 5.4.3 and 5.4.4)
# Default = False
# STRIP_INDEXES = False

# Should the sitemap list directories which only include other directories
# and no files.
# Default to True
# If this is False
# e.g. /2012 includes only /01, /02, /03, /04, ...: don't add it to the sitemap
# if /2012 includes any files (including index.html)... add it to the sitemap
# SITEMAP_INCLUDE_FILELESS_DIRS = True

# Instead of putting files in <slug>.html, put them in
# <slug>/index.html. Also enables STRIP_INDEXES
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata
# PRETTY_URLS = False

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts by default
# SCHEDULE_ALL = False
# If True, schedules post to today if possible, even if scheduled hour is over
# SCHEDULE_FORCE_TODAY = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you are using the compile-ipynb plugin, just add this one:
#MATHJAX_CONFIG = """
#<script type="text/x-mathjax-config">
#MathJax.Hub.Config({
#    tex2jax: {
#        inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#        displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ]
#    },
#    displayAlign: 'left', // Change this to 'center' to center equations.
#    "HTML-CSS": {
#        styles: {'.MathJax_Display': {"margin": 0}}
#    }
#});
#</script>
#"""

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuracion you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter':{'template_file': 'toggle'}}

# What MarkDown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite']

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty.
# SOCIAL_BUTTONS_CODE = """
# <!-- Social buttons -->
# <div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">
# <a class="addthis_button_more">Share</a>
# <ul><li><a class="addthis_button_facebook"></a>
# <li><a class="addthis_button_google_plusone_share"></a>
# <li><a class="addthis_button_linkedin"></a>
# <li><a class="addthis_button_twitter"></a>
# </ul>
# </div>
# <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>
# <!-- End of social buttons -->
# """

# Hide link to source for the posts?
# HIDE_SOURCELINK = False
# Copy the source files for your pages?
# Setting it to False implies HIDE_SOURCELINK = True
# COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a feedburner feed or something else.
# RSS_LINK = None

# Show only teasers in the RSS feed? Default to True
# RSS_TEASERS = True

# A search form to search this site, for the sidebar. You can use a google
# custom search (http://www.google.com/cse/)
# Or a duckduckgo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
#SEARCH_FORM = """
#<!-- Custom search -->
#<form method="get" id="search" action="http://duckduckgo.com/"
# class="navbar-form pull-left">
#<input type="hidden" name="sites" value="%s"/>
#<input type="hidden" name="k8" value="#444444"/>
#<input type="hidden" name="k9" value="#D51920"/>
#<input type="hidden" name="kt" value="h"/>
#<input type="text" name="q" maxlength="255"
# placeholder="Search&hellip;" class="span2" style="margin-top: 4px;"/>
#<input type="submit" value="DuckDuckGo Search" style="visibility: hidden;" />
#</form>
#<!-- End of custom search -->
#""" % SITE_URL
#
# If you prefer a google search form, here's an example that should just work:
#SEARCH_FORM = """
#<!-- Custom search with google-->
#<form id="search" action="http://google.com/search" method="get" class="navbar-form pull-left">
#<input type="hidden" name="q" value="site:%s" />
#<input type="text" name="q" maxlength="255" results="0" placeholder="Search"/>
#</form>
#<!-- End of custom search -->
#""" % SITE_URL

# Also, there is a local search plugin you can use, based on Tipue, but it requires setting several
# options:

# SEARCH_FORM = """
# <span class="navbar-form pull-left">
# <input type="text" id="tipue_search_input">
# </span>"""
#
# BODY_END = """
# <script type="text/javascript" src="/assets/js/tipuesearch_set.js"></script>
# <script type="text/javascript" src="/assets/js/tipuesearch.js"></script>
# <script type="text/javascript">
# $(document).ready(function() {
    # $('#tipue_search_input').tipuesearch({
        # 'mode': 'json',
        # 'contentLocation': '/assets/js/tipuesearch_content.json',
        # 'showUrl': false
    # });
# });
# </script>
# """

# EXTRA_HEAD_DATA = """
# <link rel="stylesheet" type="text/css" href="/assets/css/tipuesearch.css">
# <div id="tipue_search_content" style="margin-left: auto; margin-right: auto; padding: 20px;"></div>
# """
# ENABLED_EXTRAS = ['local_search']
#


# Use content distribution networks for jquery and twitter-bootstrap css and js
# If this is True, jquery is served from the Google CDN and twitter-bootstrap
# is served from the NetDNA CDN
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Extra things you want in the pages HEAD tag. This will be added right
# before </HEAD>
# EXTRA_HEAD_DATA = ""
# Google analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# BODY_END = ""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Twitter Card summaries / Open Graph.
# Twitter cards make it possible for you to attach media to Tweets
# that link to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit
# https://dev.twitter.com/form/participate-twitter-cards
#
# Uncomment and modify to following lines to match your accounts.
# Specifying the id for either 'site' or 'creator' will be preferred
# over the cleartext username. Specifying an ID is not necessary.
# Displaying images is currently not supported.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards / Open Graph
#     # 'site': '@website',  # twitter nick for the website
#     # 'site:id': 123456,  # Same as site, but the website's Twitter user ID
#                           # instead.
#     # 'creator': '@username',  # Username for the content creator / author.
#     # 'creator:id': 654321,  # Same as creator, but the Twitter user's ID.
# }


# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (eg. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use W3C-DTF Format (ex. 2012-03-30T23:00:00+02:00)
#
# TIMEZONE = 'UTC'

# If webassets is installed, bundle JS and CSS to make site loading faster
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
# EXTRA_PLUGINS_DIRS = []

# Experimental plugins - use at your own risk.
# They probably need some manual adjustments - please see their respective
# readme.
# ENABLED_EXTRAS = [
#     'planetoid',
#     'ipynb',
#     'local_search',
#     'render_mustache',
# ]

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
# DEMOTE_HEADERS = 1

# You can configure the logging handlers installed as plugins or change the
# log level of the default stdout handler.
LOGGING_HANDLERS = {
    'stderr': {'loglevel': 'WARNING', 'bubble': True},
    #'smtp': {
    #    'from_addr': 'test-errors@example.com',
    #    'recipients': ('test@example.com'),
    #    'credentials':('testusername', 'password'),
    #    'server_addr': ('127.0.0.1', 25),
    #    'secure': (),
    #    'level': 'DEBUG',
    #    'bubble': True
    #}
}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.

GLOBAL_CONTEXT = {}
