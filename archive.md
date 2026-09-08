---
layout: page
title: Archive
permalink: /archive/
---

<ul class="post-list">
  {% for post in site.posts %}
  <li>
    <a class="post-link" href="{{ post.url | relative_url }}">{% include issue-label.html post=post %}</a>
  </li>
  {% endfor %}
</ul>
