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
## Academic
* ICRA'22 Reviewer

[//]: # (<details>)
[//]: # (<summary>Expand</summary>)
[//]: # (<ul>)
[//]: # (<li>ICRA'22 Reviewer</li>)
[//]: # (</ul>)
[//]: # (</details>)

## *FIRST* Robotics
I am an active volunteer for [*FIRST*](https://www.firstinspires.org/), a non-profit organization that provides grade-school students around the world with hands-on STEM education opportunities through robotics competitions. I am an alum of *FIRST* Robotics Competition Team 1533 [Triple Strange](https://ecgrobotics.org/), and credit my experience with *FIRST* as a high school student for pushing me to pursue the field of robotics and my current line of research. Since graduating, I have volunteered at every level of *FIRST* as a referee. I am the co-creator and developer of the *FIRST* Tech Challenge Scoring System, [FTCLive](https://github.com/FIRST-Tech-Challenge/scorekeeper), that provides live scoring and event management for all *FIRST* Tech Challenge events.

### Positions Held
Years given are for the spring semester of that academic year.
* *FIRST* Chesapeake Alumni Ambassador 2020, 2022, 2023, 2024
* [FTCLive](https://github.com/FIRST-Tech-Challenge/scorekeeper) Scoring System Co-Creator and Developer 2019-Present
* North Carolina FTC Planning Committee Member 2018-Present
* FRC Head Referee (2022-Present) and Referee (2016-Present)
* FTC Head Referee (2016-Present) and Referee (2016-Present)
* FLL Challenge Head Referee (2017-2019) and Referee (2016-2019)


{% assign total_event_count = 0 %}
{% assign number_of_seasons = 0 %}
{% assign total_day_count = 0 %}
{% for season in site.data.first %}
{% assign number_of_seasons = number_of_seasons | plus: 1 %}
{% assign total_event_count = total_event_count | plus: season.events.size %}
{% assign total_day_count = total_day_count | plus: season.num_days %}
{% endfor %}
### Volunteering at *FIRST* Events ({{ total_event_count }} Events spanning {{ total_day_count }} Days across {{ number_of_seasons }} Seasons)
I volunteer at as many *FIRST* events as I can each season. I try to keep this list updated with the events I will volunteer at in the future, so come by and say hi.

{% for season in site.data.first %}
  {% assign season_start_year = season.season | minus: 1 %}
  <details>
  <summary>{{ season_start_year }}-{{ season.season }} Season ({{ season.events.size }} Events; {{season.num_days}} Days)</summary>
  <table>
  <tr><th>Event Date</th><th style="text-align: center">Program</th><th>Event</th><th>Role(s)</th></tr>
  {% for event in season.events %}
    <tr>
    <td>{{ event.event_start }}
    {% if event.event_start != event.event_end %}
    - {{ event.event_end }}
    {% endif %}
    </td>
    <td style="text-align: center"><span class="program-pill {{ event.program }}"> {{ event.program }} </span>
    </td>
    <td>{{ event.event }}</td>
    <td>{% for role in event.roles %}{{ role }}{% if forloop.last %}{% else %}, {% endif %}{% endfor %}</td>
  </tr>
  {% endfor %}
  </table>
  </details>
{% endfor %}