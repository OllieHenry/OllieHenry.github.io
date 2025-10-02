---
layout: default
title: "Transcendental"
date: 2025-10-02
---

# Constructing a transcendental number, easily

Near the beginning of your maths degree, you'll meet transcendental numbers. These are
numbers which aren't the root of any polynomial with rational coefficients
(as opposed to algebraic numbers, which are the roots of such polynomials), and it's not
obvious that they exist at all.

To show they exist, you'll likely see two proofs. The original, constructive proof, shows that
Liouville's constant $$\alpha$$ is transcendental, where

$$ \alpha = \sum_{n=1}^{\infty} 10^{-n!} $$

$$\alpha$$ is the simplest of a [class of transcendental numbers](https://en.wikipedia.org/wiki/Liouville_number),
and while the proof of its transcendence is (relatively) short, and very beautiful, it's also
the first 'difficult' proof you'll meet in your degree.

The easier proof which you're likely to meet is non-constructive: you don't get a transcendental number,
you just show they exist. This proof relies on the notion of countability. A countable set is one
whose elements can be listed one by one (possibly in an infinitely long list), without missing any; for example,

$$\mathbb{N} = \{(0), 1, 2, 3, \dots\}$$

and

$$\mathbb{Z} = \{0, 1, -1, 2, -2, \dots\}$$

are countable, while [Cantor's diagonal argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument#Real_numbers)
shows that $$\mathbb{R}$$ is not. So if we can show that the set of algebraic numbers is countable, then
$$\mathbb{R}$$ can't consist only of algebraic numbers (otherwise we could list $$\mathbb{R}$$ by listing
the algebraic numbers). Therefore, if the algebraic numbers are countable, transcendental numbers
must exist.

We can easily find a way to list the algebraic numbers: just list all the rational-coefficient polynomials, since every
algebraic number is a root of such a polynomial, then list each polynomial's roots.

Instead of rational-coefficient polynomials, we can consider only integer-coefficient polynomials, because
a root of a rational-coefficient polynomial will also be a root of the integer-coefficient polynomial
obtained by multiplying out all the denominators. There are many ways of doing this; for example

1. Start with $$n=1$$
2. List the integers from $$-n$$ to $$n$$
3. List the polynomials with $$1 \leq $$ degree $$\leq n$$ with coefficients in your list of integers
4. Add $$1$$ to $$n$$ and return to step 2

For step 3, you can list in this order: start with the smallest degree,
then the smallest $$x^0$$ coefficient,
then the smallest $$x^1$$ coefficient, and so on. So our list should start like this:

- firstly, $$n=1$$
    - coefficients = $$\{-1, 0, 1\}$$; degree $$=1$$
        - polynomials: $$-1-x, \quad -1+x, \quad -x, \quad x, \quad 1-x, \quad 1+x$$
- next, $$n=2$$
    - coefficients = $$\{-2, -1, 0, 1, 2\}$$; degree $$=1,2$$
        - polynomials: $$-2-2x, \quad \dots, \quad 2+2x, \quad -2-2x-2x^2, \quad -2-2x-x^2, \quad \dots, \quad 2+2x+x^2, \quad 2+2x+2x^2$$

Then, for each polynomial, list its real roots in order. We end up with a list containing all algebraic numbers
(including repeats, since we didn't constrain the polynomials in our list to be irreducible). That means
the algebraic numbers are countable, so there must exist transcendental numbers.

You may notice that for each step, the polynomials from every previous step are generated again, which leads
to a lot of repeats. We can remove repeated polynomials from the list, but we'll still get repeated algebraic
numbers, because we still have reducible polynomials.

### A non-constructive proof?

We've proven transcendental numbers exist without showing one, but this proof
[isn't fundamentally non-constructive](https://en.wikipedia.org/wiki/Cantor%27s_first_set_theory_article#A_misconception_about_Cantor's_work).
We can easily get a concrete transcendental number out of it just by applying the diagonal argument 
directly to our list, instead of applying it to $$\mathbb{R}$$. With the diagonal argument,
we construct a number not in the list containing all algebraic numbers, which must therefore be transcendental.

I wrote this short post because I wanted to compute such a number. Rewriting the algorithm above in Python,
and removing the repeated polynomials, we