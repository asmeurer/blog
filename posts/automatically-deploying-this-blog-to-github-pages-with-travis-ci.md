This blog, as I've outlined in
the [past](moving-to-github-pages-with-nikola/), is built with
the [Nikola](https://getnikola.com/) static blogging engine. I really like
Nikola because it uses Python, has lots of nice extensions, and is [sanely
licensed](https://github.com/getnikola/nikola/blob/master/LICENSE.txt).

Most importantly, it is a static site generator, meaning I write my posts in
Markdown, and Nikola generates the site as static web content ("static" means no web server
is required to run the site). This means that the site can be hosted for free
on [GitHub pages](https://pages.github.com/). This is how this site has been
hosted since I started it. I have
a [GitHub repo](http://github.com/asmeurer/blog) for the site, and the content
itself is deployed to
the [gh-pages](https://github.com/asmeurer/blog/tree/gh-pages) branch of the
repo. But until now, the deployment has happened only manually with the
`nikola github_deploy` command.

A much better way is to deploy automatically using Travis CI. That way, I do
not need to run any software on my computer to deploy the blog.

The steps outlined here will work for any static site generator. They assume
you already have one set up and hosted on GitHub.

## Step 1: Create a .travis.yml file

Create a `.travis.yml` file like the one below

``` yaml
sudo: false
language: python

python:
  - 3.6

install:
  - pip install "Nikola[extras]" doctr

script:
  - set -e
  - nikola build
  - doctr deploy . --built-docs output/
```

- If you use a different static site generator, replace `nikola` with that
  site generator's command.
- If you have Nikola configured to output to a different directory, or use a
  different static site generator, replace `--built-docs output/` with the
  directory where the site is built.
- Add any extra packages you need to build your site to the `pip install`
  command. For instance, I use the `commonmark` extension for Nikola, so I
  need to install `commonmark`.

Then go to [https://travis-ci.org/profile/](http://www.asmeurer.com/blog/) and enable Travis for your blog
repo.

## Step 2: Run doctr

The key here is [doctr](https://drdoctr.github.io/doctr/), a tool I wrote with
[Gil Forsyth](https://github.com/gforsyth) that makes deploying anything from
Travis CI to GitHub Pages a breeze. It automatically handles creating and
encrypting a deploy SSH key for GitHub, and the syncing of files to the
`gh-pages` branch.

First install doctr. `doctr` requires
Python 3.5+, so you'll need that. You can install it with conda:

```bash
conda install -c conda-forge doctr
```

or if you don't use conda, with pip

```bash
pip install doctr
```

Then run

```bash
doctr configure
```

in your blog repo.  This will ask you for your GitHub username and password,
and for the name of the repo you are deploying from and to (for instance, for
my blog, I entered `asmeurer/blog`). The output will look something like this:

<!-- http seems to give the least amount of highlighting. text is -->
<!-- supposed to work, but doesn't render correctly. -->
```http
$ doctr configure
What is your GitHub username? asmeurer
Enter the GitHub password for asmeurer:
A two-factor authentication code is required: app
Authentication code: 911451
What repo do you want to build the docs for (org/reponame, like 'drdoctr/doctr')? asmeurer/blog
What repo do you want to deploy the docs to? [asmeurer/blog] asmeurer/blog
Generating public/private rsa key pair.
Your identification has been saved in github_deploy_key.
Your public key has been saved in github_deploy_key.pub.
The key fingerprint is:
SHA256:4cscEfJCy9DTUb3DnPNfvbBHod2bqH7LEqz4BvBEkqc doctr deploy key for asmeurer/blog
The key's randomart image is:
+---[RSA 4096]----+
|    ..+.oo..     |
|     *o*..  .    |
|      O.+  o o   |
|     E + o  B  . |
|      + S .  +o +|
|       = o o o.o+|
|        * . . =.=|
|       . o ..+ =.|
|        o..o+oo  |
+----[SHA256]-----+

The deploy key has been added for asmeurer/blog.

You can go to https://github.com/asmeurer/blog/settings/keys to revoke the deploy key.

================== You should now do the following ==================

1. Commit the file github_deploy_key.enc.

2. Add

    script:
      - set -e
      - # Command to build your docs
      - pip install doctr
      - doctr deploy <deploy_directory>

to the docs build of your .travis.yml.  The 'set -e' prevents doctr from
running when the docs build fails. Use the 'script' section so that if
doctr fails it causes the build to fail.

3. Put

    env:
      global:
        - secure: "Kf8DlqFuQz9ekJXpd3Q9sW5cs+CvaHpsXPSz0QmSZ01HlA4iOtdWVvUttDNb6VGyR6DcAkXlADRf/KzvAJvaqUVotETJ1LD2SegnPzgdz4t8zK21DhKt29PtqndeUocTBA6B3x6KnACdBx4enmZMTafTNRX82RMppwqxSMqO8mA="

in your .travis.yml.
```

Follow the steps at the end of the command:

1. Commit the file `github_deploy_key.enc`.
2. You already have `doctr deploy` in your `.travis.yml` from step 1 above.
3. Add the `env` block to your `.travis.yml`. This will let Travis CI decrypt
the SSH key used to deploy to `gh-pages`.


## That's it

Doctr will now deploy your blog automatically. You may want to look at the
Travis build to make sure everything works. Note that `doctr` only deploys
from `master` by default (see below). You may also want to look at the
other
[command line flags](https://drdoctr.github.io/doctr/commandline.html#doctr-deploy) for
`doctr deploy`, which let you do things such as to deploy to `gh-pages` for a
different repo than the one your blog is hosted on.


I recommend these steps over the ones in
the
[Nikola manual](https://getnikola.com/blog/automating-nikola-rebuilds-with-travis-ci.html) because
doctr handles the SSH key generation for you, making things more secure. I
also found that the `nikola github_deploy` command
was [doing too much](https://github.com/getnikola/nikola/issues/2847), and
`doctr` handles syncing the built pages already anyway. Using `doctr` is much
simpler.


## Extra stuff

### Reverting a build

If a build goes wrong and you need to revert it, you'll need to use git to
revert the commit on your `gh-pages` branch. Unfortunately, GitHub doesn't
seem to have a way to revert commits in their web interface, so it has to be
done from the command line.

### Revoking the deploy key

To revoke the deploy key generated by doctr, go your repo in GitHub, click on
"settings" and then "deploy keys". Do this if you decide to stop using this,
or if you feel the key may have been compromised. If you do this, the
deployment will stop until you run step 2 again to create a new key.

### Building the blog from branches

You can also build your blog from branches, e.g., if you want to test things
out without deploying to the final repo.

We will use the steps
outlined
[here](https://drdoctr.github.io/doctr/recipes.html#deploy-docs-from-any-branch).

Replace the line

```yaml
  - doctr deploy . --built-docs output/
```

in your `.travis.yml` with something like

```yaml
  - if [[ "${TRAVIS_BRANCH}" == "master" ]]; then
      doctr deploy . --built-docs output/;
    else
      doctr deploy "branch-$TRAVIS_BRANCH" --built-docs output/ --no-require-master;
    fi
```

This will deploy your blog as normal from `master`, but from a branch it will
deploy to the `branch-<branchname>` subdir. For instance, my blog is at
[http://www.asmeurer.com/blog/](http://www.asmeurer.com/blog/), and if I had a branch called `test`, it would
deploy it to [http://www.asmeurer.com/blog/branch-test/]().

Note that it will not delete old branches for you from `gh-pages`. You'll need
to do that manually once they are merged.

This only works for branches in the same repo. It is not possible to deploy
from a branch from pull request from a fork, for security purposes.

### Enable build cancellation in Travis

If you go the Travis page for your blog and choose "settings" from the
hamburger menu, you can enable auto cancellation for branch builds. This will
make it so that if you push many changes in succession, only the most recent
one will get built. This makes the changes get built faster, and lets you
revert mistakes or typos without them ever actually being deployed.
