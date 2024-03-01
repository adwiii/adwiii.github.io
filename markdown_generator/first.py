import os
from collections import defaultdict

import pandas as pd
from datetime import datetime
import yaml

class EventVolunteering:
    def __init__(self, row):
        self.event = row['Event'].strip()
        self.program = row['Program'].strip()
        if self.program == 'FLL Challenge':
            self.program = 'FLL-C'
        self.season = row['Season']
        if any([(p in self.program) for p in ['FLL-C', 'FTC']]):
            # for some reason this uses season start
            # instead, normalize to championship year
            self.season += 1
        self.event_start = row['Event Start'].strip()
        self.event_end = row['Event End'].strip()
        self.event_start_time = datetime.strptime(self.event_start, '%m/%d/%Y')
        self.event_end_time = datetime.strptime(self.event_end, '%m/%d/%Y')
        self.roles = [row['Role'].strip()]
        self.num_days = 1
        if self.event_start != self.event_end:
            self.num_days = (self.event_end_time - self.event_start_time).days

    def event_key(self):
        return f'{self.program}_{self.season}_{self.event}'

    def as_dict(self):
        return {
            'event': self.event,
            'program': self.program,
            'season': self.season,
            'event_start': self.event_start,
            'event_end': self.event_end,
            'roles': self.roles,
            'num_days': self.num_days,
            'in_future': self.event_start_time > datetime.now()
        }

    def merge(self, other):
        self.roles.extend(other.roles)


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path_parent = os.path.dirname(dir_path)
    csv_file = f'{dir_path}/first_volunteer_history.csv'
    data = pd.read_csv(csv_file)
    event_map = {}
    for index, row in data.iterrows():
        event = EventVolunteering(row)
        if event.event_key() in event_map:
            event_map[event.event_key()].merge(event)
        else:
            event_map[event.event_key()] = event
    season_map = defaultdict(list)
    event_list = sorted(list(event_map.values()), key=lambda x: x.event_start_time)
    for event in event_list:
        season_map[event.season].append(event.as_dict())
    # total_days_happened = sum([event.num_days for event in event_list if not event])
    flattened_seasons = [{
        'season': season,
        'events': events,
        'num_events_happened': len([event for event in events if not event['in_future']]),
        'num_days': sum([event['num_days'] for event in events if not event['in_future']])
    } for season, events in season_map.items()]
    total_days_happened = sum([season['num_days'] for season in flattened_seasons])
    num_events_happened = sum([season['num_events_happened'] for season in flattened_seasons])
    with open(f'{dir_path_parent}/_data/first.yml', 'w') as f:
        yaml.dump(flattened_seasons, f)
    tex_string = f'\subsubsection*{{Volunteering at \\textit{{FIRST}} Events -- {num_events_happened} Events spanning {total_days_happened} Days across {len(flattened_seasons)} Seasons}}\n'
    # tex_string +=  ('I volunteer at as many \\textit{FIRST} events as I can each season. Events are listed under each season based on what game was played at the event;'
    #                 ' accordingly, summer and fall off season events show in the previous season.\\\\ \n')
    tex_string += 'I volunteer at as many \\textit{FIRST} events as I can each season. Below is a summary of my event involvement each season.\n'
    tex_string += 'You can find a full list of events, including future events, on my website: \\url{https://treywoodlief.com/first/}.\\\\ \n'
    prog_map = {
        'FRC': '\\FRC',
        'FTC': '\\FTC',
        'FLL-C': '\\FLLC',
    }
    for season in reversed(flattened_seasons):
        # tex_string += f'\\subsubsection*{{{season["season"] - 1} -- {season["season"]} ({len(season["events"])} Events; {season["num_days"]} Days) }}\n'
        tex_string += f'\\years{{{season["season"] - 1} -- {season["season"]}}} \\textbf{{Volunteered at {season["num_events_happened"]} Events over {season["num_days"]} Days}}\\\\ \n'
        # tex_string += '\\begin{longtable}{p{0.13\\textwidth}p{0.08\\textwidth}p{0.52\\textwidth}p{0.15\\textwidth}}\n'
        # tex_string += '\\textbf{Dates} & \\textbf{Program} & \\textbf{Event} & \\textbf{Role(s)} \\\\ \n'
        roles_held = {}
        for event in season['events']:
            if event['in_future']:
                continue
            # TODO aggregate roles by program
        # for event in season['events']:
        #     if event['event_start'] == event['event_end']:
        #         date_string = event['event_start'][:event['event_start'].rfind('/')]
        #     else:
        #         date_string = event['event_start'][:event['event_start'].rfind('/')] + '--' + event["event_end"][:event['event_end'].rfind('/')]
        #     # date_string = event['event_start'] + ('' if event['event_start'] == event['event_end'] else f'-- {event["event_end"]}')
        #     role_string = ', '.join(event['roles'])
        #     event_name = event["event"].replace("&", "\\&")
        #     tex_string += f'{date_string} & {prog_map[event["program"]]} & {event_name} & {role_string} \\\\ \n'
        # tex_string += '\\end{longtable}\n\\FloatBarrier\n'
    with open(f'{dir_path}/first.tex', 'w') as f:
        f.write(tex_string)

if __name__ == '__main__':
    main()