import json
import sys
from geohelper import distance


def load_data(filepath):
    with open(filepath, "r", encoding='utf-8') as input_file:
        raw_data = input_file.read()
    try:
        return json.loads(raw_data)
    except ValueError:
        print('JSON syntax error')
        raise SystemExit


def get_biggest_bar(json_data):
    biggest_bar = max(json_data, key=lambda x: x['SeatsCount'])
    return biggest_bar['Name']


def get_smallest_bar(json_data):
    smallest_bar = min(json_data, key=lambda x: x['SeatsCount'])
    return smallest_bar['Name']


def get_closest_bar(json_data, user_longitude, user_latitude):
    min_dist = float("inf")
    for bar in json_data:
        bar_longitude = bar['geoData']['coordinates'][0]
        bar_latitude = bar['geoData']['coordinates'][1]
        dist = distance.get_distance(bar_latitude, bar_longitude, user_latitude, user_longitude)
        if dist < min_dist:
            min_dist = dist
            bar_name = bar['Name']
    return bar_name


if __name__ == '__main__':
    filepath = sys.argv[1]
    longitude = float(sys.argv[2])
    latitude = float(sys.argv[3])
    print('The biggest Bar: ', get_biggest_bar(load_data(filepath)))
    print('The smallest Bar: ', get_smallest_bar(load_data(filepath)))
    print('The closest Bar: ', get_closest_bar(load_data(filepath), longitude, latitude))
