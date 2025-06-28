---
layout: default
title: "Ollie's Site"
---

# Ollie's Site

<p>
  Last modified 2025-06-29. Created 2025-06-07. I can be reached at
  <a href="mailto:olliehenry16@gmail.com">olliehenry16@gmail.com</a>.
</p>

## Bio

I'm Ollie, a software engineer based in Prague. I've also worked as a
data scientist and continue to develop my skills in both professions. I
graduated from Cambridge in 2022 with a BA in maths, focused mostly on pure.

I grew up in Buckingham; the closest town most people have heard of is
Oxford, 20 miles away. I left to attend Cambridge, then after five years
(three studying, two working), left England to live in the Czech Republic.

## Projects

For most of the free time I spend working on something, that something
is maths. My interests are mostly in logic and functional analysis. Some
books I'm working through (at vastly different speeds) are:

- *Fast Track to Forcing* (currently most of my time)
- *An Invitation to Model Theory* (Kirby)
- *Introduction to Modern Analysis* (Kantorovitz and Viselter)
- *Moonshine Beyond the Monster*

There are (many!) others I've started work on, but I don't spend enough
time on them to warrant mentioning.

Besides that, I've recently started a
[machine learning theory project](https://github.com/OllieHenry/overparametrized)
which explores overparametrized models.

## Posts

<a href="/posts/visa.html">How to get a Czech digital nomad visa</a>

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <small>({{ post.date | date: "%Y-%m-%d" }})</small>
    </li>
  {% endfor %}
</ul>

