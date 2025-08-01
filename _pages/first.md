---
layout: archive
title: "<i>FIRST</i> Robotics"
permalink: /first/
author_profile: true
---

I am an active volunteer for [*FIRST*](https://www.firstinspires.org/), a non-profit organization that provides grade-school students around the world with hands-on STEM education opportunities through robotics competitions. I am an alum of *FIRST* Robotics Competition Team 1533 [Triple Strange](https://ecgrobotics.org/), and credit my experience with *FIRST* as a high school student for pushing me to pursue the field of robotics and my current line of research. Since graduating, I have volunteered at every level of *FIRST* as a referee. I am the co-creator and developer of the *FIRST* Tech Challenge Scoring System, [FTCLive](https://github.com/FIRST-Tech-Challenge/scorekeeper), that provides live scoring and event management for all *FIRST* Tech Challenge events.

### Positions Held
Years given are for the spring semester of that academic year.
* *FIRST* Chesapeake *FIRST* Tech Challenge Volunteer Advisory Committee Member (2024-Present) 
* *FIRST* Chesapeake Alumni Ambassador (2020, 2022, 2023, 2024, 2025)
* [FTCLive](https://github.com/FIRST-Tech-Challenge/scorekeeper) Scoring System Co-Creator and Developer (2019-Present)
* North Carolina FTC Planning Committee Member (2018-Present)
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
I volunteer at as many *FIRST* events as I can each season. I try to keep this list updated with the events I will volunteer at in the future, so come by and say hi. Events are listed under each season based on what game was played at the event; accordingly, summer and fall off season events show in the previous season.

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

<br>
<details>
<summary>Breakdown by role</summary>
<table>
<tr><th style="text-align: center">Program</th><th>Role</th><th>Quantity</th></tr>
{% for item in site.data.first_by_role %}
    <tr>
        <td style="text-align: center"><span class="program-pill {{ item.program }}"> {{ item.program }} </span>
        </td>
        <td>{{ item.role }}</td>
        <td>{{ item.count }}</td>
    </tr>
{% endfor %}
</table>
</details>
<details>
<summary>Breakdown by type</summary>
<table>
<tr><th style="text-align: center">Program</th><th>Role</th><th>Quantity</th></tr>
{% for item in site.data.first_by_role_type %}
    <tr>
        <td style="text-align: center"><span class="program-pill {{ item.program }}"> {{ item.program }} </span>
        </td>
        <td>{{ item.role }}</td>
        <td>{{ item.count }}</td>
    </tr>
{% endfor %}
</table>
</details>