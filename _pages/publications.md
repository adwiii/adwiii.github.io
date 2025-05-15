---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign full_venues = '' | split: '' %}
{% for pub in site.publications reversed %}
  {% if pub.journal != true and pub.paper_type == 'FULL' %}
    {% assign venueName = pub.series | split: '_' %}
    {% assign full_venues = full_venues | concat: venueName %}
  {% endif %}
{% endfor %}
{% assign full_venues = full_venues | uniq %}

{% assign short_venues = '' | split: '' %}
{% for pub in site.publications reversed %}
  {% if pub.journal != true and pub.paper_type != 'FULL' %}
    {% assign venueName = pub.series | split: '_' %}
    {% assign short_venues = short_venues | concat: venueName %}
  {% endif %}
{% endfor %}
{% assign short_venues = short_venues | uniq %}

{% assign journals = '' | split: '' %}
{% for pub in site.publications reversed %}
  {% if pub.journal == true %}
    {% assign venueName = pub.venue | split: 'ZZQXZZ' %}
    {% assign journals = journals | concat: venueName %}
  {% endif %}
{% endfor %}
{% assign journals = journals | uniq %}

My work has appeared in the following venues:

# Full Papers:
## Conferences:
<ul>
{% for venue in full_venues %}

  <li>{{venue}}:
  {% for pub in site.publications %}
    {% if pub.series == venue and pub.journal != true and pub.paper_type == 'FULL' %}
    <a href="{{pub.permalink}}">{{pub.short_year}}</a>
    {% endif %}
  {% endfor %}
  </li>
{% endfor %}
</ul>


## Journals:
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

# Short Papers:
<ul>
{% for venue in short_venues %}

  <li>{{venue}}:
  {% for pub in site.publications %}
    {% if pub.series == venue and pub.journal != true and pub.venue_type != 'FULL' %}
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
