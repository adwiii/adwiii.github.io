---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign venues = '' | split: '' %}
{% for pub in site.publications reversed %}
  {% assign venueName = pub.series | split: '_' %}
  {% assign venues = venues | concat: venueName %}
{% endfor %}
{% assign venues = venues | uniq %}
My work has appeared in the following venues:
<ul>
{% for venue in venues %}

  <li>{{venue}}:
  {% for pub in site.publications %}
    {% if pub.series == venue %}
    <a href="{{pub.permalink}}">{{pub.short_year}}</a>
    {% endif %}
  {% endfor %}
  </li>
{% endfor %}
</ul>
{% if site.author.googlescholar %}
  You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.
{% endif %}

---

{% include base_path %}

{% for post in site.publications reversed %}

  {% include archive-single.html %}

{% endfor %}
