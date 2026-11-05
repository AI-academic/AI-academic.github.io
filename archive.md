---
layout: page
title: Archive
permalink: /archive/
---

<div class="archive">

{% include nav-style.html %}
<style>
  .archive-month { margin-top: 1.25rem; }
  .archive-month summary { cursor: pointer; }
  .archive-month summary h2 { display: inline; margin: 0; }
  .archive-month .post-list { margin-top: 1rem; }
  .issue-intro { margin: .25rem 0 0; }
  .issue-link { font-weight: 600; }
</style>

<p>Every issue, newest first, with a short introduction to each. Looking for a subject rather than an issue? <a href="{{ '/search/' | relative_url }}">Search</a> every story, browse <a href="{{ '/organizations/' | relative_url }}">by organization</a>, or choose a topic.</p>

{% comment %} The same topics and counts as the jump bar on /topics/. {% endcomment %}
<nav class="jump-nav">
  <span class="jump-label">Browse by topic</span>
  <div class="pill-bar">
  {%- for t in site.tag_vocabulary -%}
    {%- assign rows = site.items | where_exp: "i", "i.tags contains t" -%}
    {%- if rows.size > 0 -%}
    <a href="{{ '/topics/' | relative_url }}#{{ t | slugify }}">{{ t }} <span class="n">{{ rows.size }}</span></a>
    {%- endif -%}
  {%- endfor -%}
  </div>
</nav>

{% comment %}
  Issues are grouped by month, in sections that open and close on a click with
  no script involved. Only the newest month starts open. The introductions come
  from _data/archive_intros.yml, which only this page reads.
{% endcomment %}
{% assign current_month = "" %}
{% for post in site.posts %}
  {% assign month = post.date | date: "%B %Y" %}
  {% if month != current_month %}
    {% unless forloop.first %}</ul></details>{% endunless %}
    <details class="archive-month"{% if forloop.first %} open{% endif %}>
    <summary><h2>{{ month }}</h2></summary>
    <ul class="post-list">
    {% assign current_month = month %}
  {% endif %}
  <li>
    <a class="issue-link" href="{{ post.url | relative_url }}">{% include issue-label.html post=post %}</a>
    {% assign day = post.date | date: "%Y-%m-%d" %}
    {% assign intro = site.data.archive_intros[day] %}
    {% if intro %}<p class="issue-intro">{{ intro }}</p>{% endif %}
  </li>
  {% if forloop.last %}</ul></details>{% endif %}
{% endfor %}

</div>
