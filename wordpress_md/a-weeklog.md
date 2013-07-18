Title: A Weeklog
Date: 2010-06-15 21:45
Author: asmeurer
Category: Uncategorized
Slug: a-weeklog

[These][] [seem][] [to][] [be][] all the rave these days, so I figured,
why not jump on the bandwagon:

` Aaron-Meurer:doc aaronmeurer20100615153531(integration$)$git weekreport Aaron Meurer (20):       Fix some bugs in Poly       Make Poly(sin(x)/x*t, t, domain='EX').clear_denoms() work       Fix integrate to work correctly with heurisch.py       Use more efficient gcdexdiophantine() algorithm       Add support for taking the derivation over the coefficient domain in risch.py       Add (but do not yet use) splitfactor_sqf() in risch.py       Add polynomial_reduce() to risch.py       Add tests for algorithms in risch.py in a new test_risch.py file       Only allow coercion to larger domains       Allow coercion from ZZ(a) to ZZ(a, b)       Fix doctest in new heurisch.py file       Add residue_reduce()       Formatting fixes in docstrings in sympy/polys/algebratools.py       Add includePRS option to resultant functions       Add permute method to DMP       Add a test for the includePRS option of resultant()       Have residue_reduce() make S_i monic       Rewrite polynomial_reduce() non-recursively       Add integrate_hypertangent_polynomial()       Add integrate_nonlinear_no_specials()`

  [These]: http://ondrejcertik.blogspot.com/2010/06/week-may-30-june-4.html
  [seem]: http://ondrejcertik.blogspot.com/2010/06/week-june-5-june-11.html
  [to]: http://haz-tech.blogspot.com/2010/06/plowing-forward.html
  [be]: http://ojensen.wordpress.com/2010/06/15/array-arguments/
