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
## University of Virginia 2019-2025 (Expected)
* Ph.D. Computer Science
* Co-advised Dr. [Sebastian Elbaum](https://www.cs.virginia.edu/~se4ja/) and Dr. [Kevin Sullivan](https://engineering.virginia.edu/faculty/kevin-sullivan)

## University of Virginia 2019-2022
* M. Computer Science (MCS)

## North Carolina State University 2015-2019
* B.S. in Computer Science
* B.S. in Electrical Engineering
* B.S. in Computer Engineering
* Minor in Mathematics

*Honors*: Graduated Valedictorian and Summa Cum Laude

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

Full publication list:
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
* Copenhaver Charitable Trust Bicentennial Fellowship (2024-2025)
  * University of Virginia School of Engineering and Applied Science
* Outstanding Graduate Research Award (2024)
  * University of Virginia Department of Computer Science
* All-University Graduate Teaching Award (2022-2023)
  * University of Virginia
* Most Promising Research Award (2022)
  * University of Virginia Computer Science Research Symposium
* Best Presentation Award (2020)
  * University of Virginia Computer Science Research Symposium
* Dean's Scholar Fellowship (2019-2024)
  * University of Virginia School of Engineering and Applied Science
* Dr. Donald L. Bitzer Creativity Award (2019)
  * North Carolina State University Department of Computer Science
* University Honors Program (2019)
  * North Carolina State University
* Computer Science Honors Program (2019)
  * North Carolina State University Department of Computer Science
* Phi Kappa Phi Honor Society (2018)
* Tau Beta Pi Engineering Honor Society (2017)
* IEEE-Eta Kappa Nu Honor Society (IEEE-HKN) (2016)

## Extracurricular
* [*FIRST* Tech Challenge](https://www.firstinspires.org/robotics/ftc) Global Volunteer of the Year<sup>[1](https://www.firstinspires.org/sites/default/files/uploads/annual-report/fy2021-annual-impact-report.pdf#page=34), [2](http://firsttechchallenge.blogspot.com/2021/07/congratulations-to-our-amazing-2020.html)</sup> (2021)
* *FIRST* North Carolina [Guilford County District Event](https://youtu.be/UJb6Lta9QqI?si=BZfyL70L6zd9tMVL&t=60) Volunteer Award (2019)
* Eagle Scout (2013)

---

# Service
## Mentorship
* Johann Mission, Mathushan Mathyvannan, Yili Bai, Zachariah Risheq
  * Supported undergrad research on benchmarking autonomous systems; manuscript under submission
* [Garrett Christian](https://www.linkedin.com/in/garrett-christian/)
  * Master's at UVA - Work culminated in [ICSE'23 Publication](/publication/2023-5-20-semantic-lidar-fuzzing)

## Academic
* **Program Committee** 2025 ICSE'25 Software Engineering for Autonomous Driving Systems Workshop (SE4ADS'25)
* **Reviewer** 2025 International Conference on Software Engineering Research Track Shadow Program Committee (ICSE-Shadow'25)
* **Reviewer** 2024 IEEE Transactions on Software Engineering (TSE)
* **Reviewer** 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS'24)
* **Reviewer** 2024 International Journal of Robotics Research (IJRR)
* **Reviewer** 2022 IEEE International Conference on Robotics and Automation (ICRA'22)

## *FIRST* Robotics

{% capture source %}{% include_relative first.md %}{% endcapture %}
{{ source | split: "---" | last }}