import os
from collections import defaultdict

import pandas as pd
from datetime import datetime
import yaml

class EventVolunteering:
    def __init__(self, row):
        self.event = row['Event'].strip()
        self.program = row['Program'].strip()
        self.season = row['Season']
        if any([(p in self.program) for p in ['FLL', 'FTC']]):
            # for some reason this uses season start
            # instead, normalize to championship year
            self.season += 1
        self.event_start = row['Event Start'].strip()
        # get the start time for sorting
        self.event_start_time = datetime.strptime(self.event_start, '%m/%d/%Y')
        self.event_end = row['Event End'].strip()
        self.roles = [row['Role'].strip()]

    def event_key(self):
        return f'{self.program}_{self.season}_{self.event}'

    def as_dict(self):
        return {
            'event': self.event,
            'program': self.program,
            'season': self.season,
            'event_start': self.event_start,
            'event_end': self.event_end,
            'roles': self.roles
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
    flattened_seasons = [{
        'season': season,
        'events': events
    } for season, events in season_map.items()]
    with open(f'{dir_path_parent}/_data/first.yml', 'w') as f:
        yaml.dump(flattened_seasons, f)

if __name__ == '__main__':
    main()