Title: SymPy 0.7.0 released
Date: 2011-06-29 08:00
Author: asmeurer
Category: Uncategorized
Slug: sympy-0-7-0-released

*Cross posted on the [official SymPy blog][]*

SymPy 0.7.0 has been released on June 28, 2011.
<span class="Apple-style-span" style="font-family:'Trebuchet MS', Verdana, Arial, sans-serif;font-size:13px;color:rgb(51,51,51);line-height:18px;">It
is available at  
[  
http://sympy.org][]

The source distribution can be downloaded from:  
[http://sympy.googlecode.com/files/sympy-0.6.7.tar.gz][]

You can get the Windows installer here:  
[http://sympy.googlecode.com/files/sympy-0.6.7.win32.exe][]

And the html documentation here:  
[http://sympy.googlecode.com/files/sympy-0.6.7-docs-html.zip][]</span>

<div>
</div>
<div>
<span class="Apple-style-span" style="font-family:'Trebuchet MS', Verdana, Arial, sans-serif;font-size:13px;color:rgb(51,51,51);line-height:18px;"><span style="font-weight:bold;font-size:16px;">About
SymPy</span>

</p>
<p>
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.
SymPy is written entirely in Python.  
<span style="font-size:16px;"><span class="Apple-style-span" style="font-size:13px;"><span style="font-size:16px;"><span style="font-weight:bold;">  
</span></span></span></span></span>

</div>
<div>
<span class="Apple-style-span" style="font-family:'Trebuchet MS', Verdana, Arial, sans-serif;font-size:13px;color:rgb(51,51,51);line-height:18px;"><span style="font-size:16px;"><span class="Apple-style-span" style="font-size:13px;"><span style="font-size:16px;"><span style="font-weight:bold;">Changes
since last stable release</span></span>  
</span></span></span>

</div>
<div>
<span class="Apple-style-span" style="font-family:helvetica, arial, freesans, clean, sans-serif;font-size:6px;"><span class="Apple-style-span" style="font-size:22px;">**<span class="Apple-style-span" style="font-family:'Trebuchet MS', Verdana, Arial, sans-serif;font-weight:normal;font-size:13px;color:rgb(51,51,51);line-height:18px;">  
</span>**</span></span>

</div>
<div>
<span class="Apple-style-span" style="font-family:helvetica, arial, freesans, clean, sans-serif;font-size:6px;"><span class="Apple-style-span" style="font-size:22px;">**<span class="Apple-style-span" style="font-family:'Trebuchet MS', Verdana, Arial, sans-serif;font-weight:normal;font-size:13px;color:rgb(51,51,51);line-height:18px;">(from
<https://github.com/sympy/sympy/wiki/Release-Notes-for-0.7.0>)</span>**</span></span>

</div>
<div>
<span class="Apple-style-span" style="font-family:'Trebuchet MS', Verdana, Arial, sans-serif;color:rgb(51,51,51);line-height:18px;">**<span class="Apple-style-span" style="color:rgb(0,0,0);font-family:helvetica, arial, freesans, clean, sans-serif;font-weight:normal;line-height:23px;font-size:14px;">  
**

 {style="line-height:normal;border-top-width:4px;border-top-style:solid;border-top-color:rgb(204,204,204);font-size:22px;display:inline!important;margin:22px 0 0;padding:7px 0 0;"}

<p>
</span></b></span>

</div>
<div>
<span class="Apple-style-span" style="font-family:'Trebuchet MS', Verdana, Arial, sans-serif;color:rgb(51,51,51);line-height:18px;">**<span class="Apple-style-span" style="color:rgb(0,0,0);font-family:helvetica, arial, freesans, clean, sans-serif;font-weight:normal;line-height:23px;font-size:14px;">  
**

Backwards compatibility breaks {style="line-height:normal;border-top-width:4px;border-top-style:solid;border-top-color:rgb(204,204,204);font-size:22px;display:inline!important;margin:22px 0 0;padding:7px 0 0;"}
------------------------------

<p>
</span></b></span>

</div>
<div>
<span class="Apple-style-span" style="font-family:'Trebuchet MS', Verdana, Arial, sans-serif;color:#333333;"><span class="Apple-style-span" style="line-height:18px;">**<span class="Apple-style-span" style="color:rgb(0,0,0);font-family:helvetica, arial, freesans, clean, sans-serif;font-weight:normal;line-height:23px;font-size:14px;">**

-   This will be the last release of SymPy to support Python 2.4.
    Dropping support for Python 2.4 will let us move forward with things
    like supporting Python 3, and will let us use things that were
    introduced in Python 2.5, like with-statement context managers.
-   no longer support creating matrices without brackets (see: issue
    930)
-   Renamed
    `sum()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    to
    `summation()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: 3e763a8, issues 1376, 1727). This was changed so that it no
    longer overrides the built-in
    `sum()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}.
    The unevaluated summation is still called
    `Sum()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}.
-   Renamed
    `abs()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    to
    `Abs()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: 64a12a4, issue 1727). This was also changed so that it no
    longer overrides the built-in
    `abs()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}.
    Note that because of
    `__abs__`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    magic, you can still do
    `abs(expr)`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    with the built-in
    `abs()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"},
    and it will return
    `Abs(expr)`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}.
-   Renamed
    `max_()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `min_()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    to now
    `Max()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `Min()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: 99a271e, issue 2153)
-   Changed behaviour of
    `symbols()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}.
    `symbols('xyz')`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    gives now a single symbol
    (`'xyz'`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}),
    not three
    (`'x'`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"},
    `'y'`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `'z'`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"})
    (see: f6452a8).
    Use`symbols('x,y,z')`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    or
    `symbols('x y z')`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    to get three symbols. The 'each\_char' option will still work but is
    being deprecated.
-   Split class
    `Basic`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    into new classes
    `Expr`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"},
    `Boolean`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: a0ab479, 635d89c). Classes that are designed to be part of
    standard symbolic expressions (like
    `x**2*sin(x)`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"})
    should subclass from
    `Expr`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}.
    More generic objects that do not work in symbolic expressions but
    still want the basic SymPy structure like
    `.args`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and basic methods like
    `.subs()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    should only subclass from
    `Basic`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}.
-   `as_basic()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    method was renamed to
    `as_expr()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    to reflect changes in the core (see: e61819d, 80dfe91)
-   Methods
    `as_coeff_terms`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `as_coeff_factors`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    were renamed to
    `as_coeff_mul`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `as_coeff_add`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"},
    respectively.
-   Removed the
    `trim()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    function. The function is redundant with the new polys (see below).
    Use the
    `cancel()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    function instead.

Major Changes {style="line-height:normal;border-top-width:4px;border-top-style:solid;border-top-color:rgb(204,204,204);font-size:22px;margin:22px 0 0;padding:7px 0 0;"}
-------------

### Polys {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   New internal representations of dense and sparse polynomials (see:
    6aecdb7, 31c9aa4)
-   Implemented algorithms for real and complex root isolation and
    counting (see: 3acac67, 4b75dae, fa1206e, 103b928, 45c9b22, 8870c8b,
    b348b30)
-   Improved Gröbner bases algorithm (see: ff65e9f, 891e4de, 310a585)
-   Field isomorphism algorithm (see: b097b01, 08482bf)
-   Implemented efficient orthogonal polynomials (see: b8fbd59)
-   Added configuration framework for polys (see: 33d8cdb, 7eb81c9)
-   Function for computing minimal polynomials (see: 88bf187, f800f95)
-   Function for generating Viete's formulas (see: 1027408)
-   `roots()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    supports more classes of polynomials (e.g. cyclotomic) (see:
    d8c8768, 75c8d2d)
-   Added a function for recognizing cyclotomic polynomials (see:
    b9c2a9a)
-   Added a function for computing Horner form of polynomials (see:
    8d235c7)
-   Added a function for computing symmetric reductions of polynomials
    (see: 6d560f3)
-   Added generators of Swinnerton-Dyer, cyclotomic, symmetric, random
    and interpolating polynomials (see: dad03dd, 6ccf20c, dc728d6,
    2f17684, 3004db8)
-   Added a function computing isolation intervals of algebraic numbers
    (see: 37a58f1)
-   Polynomial division
    (`div()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"},
    `rem()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"},
    `quo()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"})
    now defaults to a field (see: a72d188)
-   Added wrappers for numerical root finding algorithms (see: 0d98945,
    f638fcf)
-   Added symbolic capabilities to
    `factor()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"},
    `sqf()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and related functions (see: d521c7f, 548120b, f6f74e6, b1c49cd,
    3527b64)
-   `together()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    was significantly improved (see: dc327fe)
-   Added support for iterable containers to
    `gcd()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `lcm()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: e920870)
-   Added a function for constructing domains from coefficient
    containers (see: a8f20e6)
-   Implemented greatest factorial factorization (see: d4dbbb5)
-   Added partial fraction decomposition algorithm based on undetermined
    coefficient approach (see: 9769d49, 496f08f)
-   `RootOf`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `RootSum`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    were significantly improved (see: f3e432, 4c88be6, 41502d7)
-   Added support for gmpy (GNU Multiple Precision Arithmetic Library)
    (see: 38e1683)
-   Allow to compile
    `sympy.polys`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    with Cython (see: afb3886)
-   Improved configuration of variables in
    `Poly`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: 22c4061)
-   Added documentation based on Wester's examples (see: 1c23792)
-   Irreducibility testing over finite fields (see: 17e8f1f)
-   Allow symmetric and non-symmetric representations over finite fields
    (see: 60fbff4)
-   More consistent factorization forms from
    `factor()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `sqf()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: 5df77f5)
-   Added support for automatic recognition algebraic extensions (see:
    7de602c)
-   Implemented Collins' modular algorithm for computing resultants
    (see: 950969b)
-   Implemented Berlekamp's algorithm for factorization over finite
    fields (see: 70353e9)
-   Implemented Trager's algorithm for factorization over algebraic
    number fields (see: bd0be06)
-   Improved Wang's algorithm for efficient factorization of
    multivariate polynomials (see: 425e225)

### Quantum {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Symbolic, abstract dirac notation in
    `sympy.physics.quantum`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}.
    This includes operators, states (bras and kets), commutators,
    anticommutators, dagger, inner products, outer products, tensor
    products and Hilbert spaces
-   Symbolic quantum computing framework that is based on the general
    capabilities in
    `sympy.physics.quantum`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}.
    This includes qubits
    (`sympy.physics.quantum.qubit`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}),
    gates
    (`sympy.physics.quantum.gate`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}),
    Grover's algorithm
    (`sympy.physics.quantum.grover`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}),
    the quantum Fourier transform
    (`sympy.physics.quantum.qft`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}),
    Shor's algorithm
    (`sympy.physics.quantum.shor`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"})
    and circuit plotting
    (`sympy.physics.quantum.circuitplot`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"})
-   Second quantization framework that inclues creation/anihilation
    operators for both Fermions and Bosons and Wick's theorem for
    Fermions
    (`sympy.physics.secondquant`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}).
-   Symbolic quantum angular momentum (spin) algebra
    (`sympy.physics.quantum.spin`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"})
-   Hydrogen wave functions (Schroedinger) and energies (both
    Schroedinger and Dirac)
-   Wave functions and energies for 1D harmonic oscillator
-   Wave functions and energies for 3D spherically symmetric harmonic
    oscillator
-   Wigner and Clebsch Gordan coefficients

Everything else {style="line-height:normal;border-top-width:4px;border-top-style:solid;border-top-color:rgb(204,204,204);font-size:22px;margin:22px 0 0;padding:7px 0 0;"}
---------------

-   Implement symarray, providing numpy nd-arrays of symbols.
-   update mpmath to 0.16
-   Add a tensor module (see:
    <http://code.google.com/p/sympy/wiki/CodeGenerationReport>)
-   A lot of stuff was being imported with
    `from sympy import *`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    that shouldn't have been (like
    `sys`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}).
    This has been fixed.

### Assumptions: {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Refine
-   Added predicates (see: 7c0b857, 53f0e1a, d1dd6a3..)
-   Added query handlers for algebraic numbers (see: f3bee7a)
-   Implement a SAT solver (see:
    <http://code.google.com/p/sympy/wiki/SuperchargingAssumptionsReport>,
    2d96329, acfbe75, etc.)

### Concrete {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Finalized implementation of Gosper's algorithm (see: 0f187e5,
    5888024)
-   Removed redundant
    `Sum2`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and related classes (see: ef1f6a7)

### Core: {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Split
    `Atom`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    into
    `Atom`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `AtomicExpr`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: 965aa91)
-   Various
    `sympify()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    improvements
-   Added functionality for action verbs (many functions can be called
    both as global functions and as methods e.g.
    `a.simplify() == simplify(a)`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"})
-   Improve handling of rational strings (see: 053a045, issue 1778)
-   Major changes to factoring of integers (see: 273f450, issue 2003)
-   Optimized
    `.has()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: c83c9b0, issue 1980; d86d08f)
-   Improvements to power (see: c8661ef, issue 1963)
-   Added range and lexicographic syntax to
    `symbols()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `var()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: f6452a8, 9aeb220, 957745a)
-   Added
    `modulus`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    argument to
    `expand()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: 1ea5be8)
-   Allow to convert
    `Interval`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    to relational form (see: 4c269fe)
-   SymPy won't manipulate minus sign of expressions any more (see:
    6a26941, 9c6bf0f, e9f4a0a)
-   `Real`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `.is_Real`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    were renamed to
    `Float`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `.is_Float`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}.
    `Real`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `.is_Real`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    still remain as deprecated shortcuts to
    `Float`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and`is_Float`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    for backwards compatibility. (see: abe1c49)
-   Methods coeff and as\_coefficient are now non-commutative aware.
    (see a4ea170)

### Geometry: {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Various improvements to Ellipse
-   Updated documentation to numpy standard
-   Polygon and Line improvements
-   Allow all geometry objects to accept a tuple as
    `Point`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    args

### Integrals: {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Various improvements (see eg. issues 1772, 1999, 1992, 1987.. etc)

### isympy {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Fixed the
    `-p`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    switch (see: e8cb04a)
-   Caching can be disabled using
    `-C`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    switch (see: 0d8d748)
-   Ground types can be set using
    `-t`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    switch (see: 75734f8)
-   Printing ordering can be set using
    `-o`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    switch (see: fcc6b13, 4ec9dc5)

### Logic {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   implies object adheres to negative normal form
-   Create new boolean class,
    `logic.boolalg.Boolean`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
-   Added XOR operator (\^) support
-   Added If-then-else (ITE) support
-   Added the dpll algorithm

### Functions: {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Added Piecewise, B-splines
-   Spherical Bessel function of the second kind implemented
-   Add series expansions of multivariate functions (see: d4d351d)

### Matrices: {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Add elementwise product (Hadamard product)
-   Extended QR factorization for general full ranked mxn matrices
-   Remove deprecated functions
    `zero()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"},
    `zeronm()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"},
    `one()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: 5da0884)
-   Added cholesky and LDL factorizations, and respective solves.
-   Added functions for efficient triangular and diagonal solves.
-   `SMatrix`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    was renamed to
    `SparseMatrix`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: acd1685)

### Physics {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   See the Quantum section

### Printing: {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Implemented pretty printing of binomials (see: 58c1dad)
-   Implemented pretty printing of Sum() (see: 84f2c22, 95b4321)
-   `sympy.printing`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    now supports ordering of terms and factors (see: 859bb33)
-   Lexicographic order is now the default. Now finally things will
    print as
    `x**2 + x + 1`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    instead of
    `1 + x + x**2`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"},
    however series still print using reversed ordering, e.g.
    `x - x**3/6 + O(x**5)`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}.
    You can get the old order (and other orderings) by setting the
    `-o`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    option to isympy (see: 08b4932, a30c5a3)

### Series: {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Implement a function to calculate residues,
    `residue()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
-   Implement nseries and lseries to handle
    `x0 != 0`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"},
    series should be more robust now (see: 2c99999, issues 2122-2124)
-   Improvements to Gruntz algorithm

### Simplify: {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Added
    `use()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: 147c142)
-   `ratsimp()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    now uses
    `cancel()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    and
    `reduced()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: 108fb41)
-   Implemented EPath (see: 696139d, bf90689)
-   a new keyword
    `rational`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    was added to nsimplify which will replace Floats with Rational
    approximations. (see: 053a045)

### Solvers: {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   ODE improvements (see: d12a2aa, 3542041; 73fb9ac)
-   Added support for solving inequalities (see: 328eaba, 8455147,
    f8fcaa7)

### Utilities: {style="line-height:26px;font-size:16px;margin:0;padding:26px 0 0;"}

-   Improve cartes, for generating the Cartesian product (see: b1b10ed)
-   Added a function computing topological sort of graphs (see: b2ce27b)
-   Allow to setup a customized printer in
    `lambdify()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    (see: c1ad905)
-   `flatten()`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
    was significantly improved (see: 31ed8d7)
-   Major improvements to the Fortran code generator (see:
    <http://code.google.com/p/sympy/wiki/CodeGenerationReport>, 3383aa3,
    7ab2da2, etc.)

In addition to the more noticeable changes listed above, there have been
numerous other smaller additions, improvements and bug fixes in the
\~2000 commits in this release. See the git log for a full list of all
changes. The command
`git log sympy-0.6.7..sympy-0.7.0`{style="font:normal normal normal 12px/normal 'Bitstream Vera Sans Mono', Courier, monospace;line-height:1.4em;background-color:rgb(248,248,248);font-size:13px;border-top-left-radius:3px 3px;border-top-right-radius:3px 3px;border-bottom-right-radius:3px 3px;border-bottom-left-radius:3px 3px;border-color:rgb(222,222,222);border-style:solid;border-width:1px;margin:0;padding:0;"}
will show all commits made between this release and the last. You can
also see the issues closed since the last release [here][].

Authors {style="line-height:normal;border-top-width:4px;border-top-style:solid;border-top-color:rgb(204,204,204);font-size:22px;margin:22px 0 0;padding:7px 0 0;"}
-------

The following people contributed at least one patch to this release
(names are given in alphabetical order by last name). A total of 64
people contributed to this release. People with a \* by their names
contributed a patch for the first time for this release. Thirty-seven
people contributed for the first time for this release. Over half of the
people who contributed to this release contributed for the first time!

Thanks to everyone who contributed to this release!

-   Tom Bachmann\*
-   Tomas Bambas\*
-   Matthew Brett\*
-   Ondřej Čertík
-   Renato Coutinho
-   Addison Cugini\*
-   Matt Curry\*
-   Raffaele De Feo\*
-   Mark Dewing
-   Thomas Dixon\*
-   Harold Erbin
-   Pavel Fedotov\*
-   Gilbert Gede\*
-   Oleksandr Gituliar\*
-   Brian Granger
-   Alexey U. Gudchenko\*
-   Øyvind Jensen
-   Fredrik Johansson
-   Felix Kaiser
-   Yuri Karadzhov\*
-   Gary Kerr\*
-   Kibeom Kim\*
-   Nicholas J.S. Kinar\*
-   Anatolii Koval\*
-   Sebastian Krämer
-   Ryan Krauss
-   Gregory Ksionda\*
-   Priit Laes
-   Vladimir Lagunov
-   Ronan Lamy
-   Tomo Lazovich\*
-   Saptarshi Mandal\*
-   David Marek
-   Jack McCaffery\*
-   Benjamin McDonald\*
-   Aaron Meurer
-   Christian Muise\*
-   Óscar Nájera\*
-   Jezreel Ng\*
-   Sherjil Ozair\*
-   Mateusz Paprocki
-   James Pearson
-   Fernando Perez
-   Vladimir Perić\*
-   Mario Pernici\*
-   Nicolas Pourcelot
-   rayman\*
-   Matthew Rocklin\*
-   Christian Schubert
-   Andre de Fortier Smit\*
-   Chris Smith
-   Cristóvão Sousa\*
-   Akshay Srinivasan
-   Vinzent Steinberg
-   Prafullkumar P. Tale\*
-   Andy R. Terrel
-   Kazuo Thow\*
-   Toon Verstraelen
-   Sean Vig\*
-   Luca Weihs\*
-   Thomas Wiecki
-   Shai 'Deshe' Wyborski\*
-   Jeremias Yehdegho\*

<p>
</span></b></span></span>

</div>

  [official SymPy blog]: http://sympy.blogspot.com/2011/06/sympy-070-released.html
  [  
 http://sympy.org]: http://sympy.org/
  [http://sympy.googlecode.com/files/sympy-0.6.7.tar.gz]: http://sympy.googlecode.com/files/sympy-0.6.6.tar.gz
  [http://sympy.googlecode.com/files/sympy-0.6.7.win32.exe]: http://sympy.googlecode.com/files/sympy-0.6.6.win32.exe
  [http://sympy.googlecode.com/files/sympy-0.6.7-docs-html.zip]: http://sympy.googlecode.com/files/sympy-0.6.6-docs-html.zip
  [here]: http://code.google.com/p/sympy/issues/list?can=1&q=closed-after%3A2010%2F3%2F17+closed-before%3A2011%2F6%2F13&sort=-closed&colspec=ID+Type+Status+Priority+Milestone+Owner+Summary+Stars+Closed&cells=tiles
