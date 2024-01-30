---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

My legal name is Alan, which may appear in some places that show given name, e.g. [ORCID](https://orcid.org/0000-0001-9803-8303); I have always gone by Trey.

---

# Education
* Master of Computer Science (MCS), University of Virginia, 2022
* B.S. in Computer Science, North Carolina State University, 2019
* B.S. in Electrical Engineering, North Carolina State University, 2019
* B.S. in Computer Engineering, North Carolina State University, 2019
  * Minor in Mathematics
  * Graduated Valedictorian and Summa Cum Laude
  * University Honors Program, Computer Science Honors Program
  * Phi Kappa Phi, Eta Kappa Nu (IEEE-HKN)

---

# Work experience
* Fall 2019-Present: Research Assistant 
  * [LESS Lab](https://less-lab-uva.github.io/) at University of Virginia
  * Co-advised by Dr. [Sebastian Elbaum](https://www.cs.virginia.edu/~se4ja/) and Dr. [Kevin Sullivan](https://engineering.virginia.edu/faculty/kevin-sullivan)

* Spring 2018-Spring 2019: Research Assistant
  * [Theory in Practice Lab](https://www.cs.utah.edu/~sullivan/#!/) at North Carolina State University
  * Advised by Dr. Blair D. Sullivan

* Summer 2016, Summer 2017: Software Development Internship
  * Fidelity Investments, Durham, NC
  * Java development, unit testing, and performance analysis
  
* November 2015-May 2019: Android Developer
  * Bamboo Mobile Health, Raleigh, NC
  * Developed and maintained the MS101.me app

---

# [Publications](/publications)

{% assign venues = '' | split: '' %}
{% for pub in site.publications reversed %}
{% assign venueName = pub.series | split: '_' %}
{% assign venues = venues | concat: venueName %}
{% endfor %}
{% assign venues = venues | uniq %}
I have been fortunate to publish in the following venues:
<ul class="no-bullets">
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

  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
---

# [Talks](/talks)
<p>
  <details>
    <summary>Show {{ site.talks.size }} Talks</summary>
    <ul>{% for post in site.talks reversed %}
      {% include archive-single-talk-cv.html %}
    {% endfor %}</ul>
  </details>
</p>
  
---

# [Teaching](/teaching)
<p>
<details>
    <summary>Show {{ site.teaching.size }} Courses</summary>
    <ul>{% for post in site.teaching reversed %}
      {% include archive-single-teaching.html %}
    {% endfor %}</ul>
  </details>
</p>

---

# Awards
## Academic
* University of Virginia All-University Graduate Teaching Award (2022-2023)
* University of Virginia School of Engineering and Applied Science Dean's Scholar Fellowship (2019-2024)
* NC State Computer Science Dr. Donald L. Bitzer Creativity Award (2019)

## Extracurricular
* [*FIRST* Tech Challenge](https://www.firstinspires.org/robotics/ftc) Global Volunteer of the Year<sup>[1](https://www.firstinspires.org/sites/default/files/uploads/annual-report/fy2021-annual-impact-report.pdf#page=34), [2](http://firsttechchallenge.blogspot.com/2021/07/congratulations-to-our-amazing-2020.html)</sup> (2021)
* *FIRST* North Carolina [Guilford County District Event](https://youtu.be/UJb6Lta9QqI?si=BZfyL70L6zd9tMVL&t=60) Volunteer Award (2019)
* Eagle Scout (2013)

---

# Service
## Mentorship
* [Garrett Christian](https://www.linkedin.com/in/garrett-christian/) - Master's at UVA - Work culminated in [ICSE'23 Publication](/publication/2023-5-20-semantic-lidar-fuzzing)

## Academic
* ICRA'22 Reviewer

[//]: # (<details>)
[//]: # (<summary>Expand</summary>)
[//]: # (<ul>)
[//]: # (<li>ICRA'22 Reviewer</li>)
[//]: # (</ul>)
[//]: # (</details>)

## *FIRST* Robotics

{% capture source %}{% include_relative first.md %}{% endcapture %}
{{ source | split: "---" | last }}