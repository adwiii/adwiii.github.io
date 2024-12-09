---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign venues = '' | split: '' %}
{% for pub in site.publications reversed %}
  {% if pub.journal != true %}
    {% assign venueName = pub.series | split: '_' %}
    {% assign venues = venues | concat: venueName %}
  {% endif %}
{% endfor %}
{% assign venues = venues | uniq %}

{% assign journals = '' | split: '' %}
{% for pub in site.publications reversed %}
  {% if pub.journal == true %}
    {% assign venueName = pub.venue | split: 'ZZQXZZ' %}
    {% assign journals = journals | concat: venueName %}
  {% endif %}
{% endfor %}
{% assign journals = journals | uniq %}

My work has appeared in the following venues:

Conferences:
<ul>
{% for venue in venues %}

  <li>{{venue}}:
  {% for pub in site.publications %}
    {% if pub.series == venue and pub.journal != true %}
    <a href="{{pub.permalink}}">{{pub.short_year}}</a>
    {% endif %}
  {% endfor %}
  </li>
{% endfor %}
</ul>


Journals:
<ul>
{% for journal in journals %}
  <li>{{journal}}:
  {% for pub in site.publications %}
    {% if pub.venue == journal and pub.journal == true %}
    <a href="{{pub.permalink}}">{{pub.year}}</a>
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
